import scrapy
from urllib.parse import urljoin
import os

class EstadoScrapy(scrapy.Spider):
    name="diario"
    start_urls = ['http://www.diariooficial.pi.gov.br/diarios.php?dia=20190125']
    url_base='http://www.diariooficial.pi.gov.br'

    def parse(self,response):
        urls = response.xpath('//table[@width="350px"]/tr[2]//a[@class="texto2"]//@href').extract()
        for url in urls:
            yield scrapy.Request(url=urljoin(self.url_base,url),callback=self.download_pdfs)

        next_page = response.xpath('//table[@width="350px"]/tr[3]//td[@align="left"]//a[@class="texto2"]/@href').extract()
        for url in next_page:
            yield scrapy.Request(url=urljoin(self.url_base,url),callback=self.parse)

    def download_pdfs(self,response):
        name_file = response.xpath('//td[@class="titulo"]//text()').extract_first().strip()
        path= name_file.split(' ')[-1].split('.')[-1]
        url_pdf = response.xpath('//span[@class="texto_diario2"]//@href').extract()
        for url in url_pdf:
            yield scrapy.Request(url=url, meta={'name_file':name_file,
                                          'path':path},
                                          callback=self.save_pdf)
    def save_pdf(self,response):
        name_file = response.meta.get('name_file')
        path = "Diarios/"+response.meta.get('path')
        try:
            os.makedirs(path)
        except:
            pass
        self.logger.info('Saving PDF %s', name_file)
        with open('{}/{}'.format(path,name_file), 'wb') as f:
            f.write(response.body)
        
