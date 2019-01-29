import scrapy
from urllib.parse import urljoin
import os

class EstadoScrapy(scrapy.Spider):
    name="Alagoas"
    start_urls = ['http://www.imprensaoficialal.com.br/diario-oficial/']
    url_base='http://www.diariooficial.pi.gov.br'

    def parse(self,response):
        urls = response.xpath('//div[@class="et_pb_portfolio_items_wrapper "]//a/@href').extract()
        for url in urls:
            yield scrapy.Request(url,callback=self.parse_links)
    
    def parse_links(self,response):
        try:
            urls = response.xpath('//div[@class="et_pb_text_inner"]/p/a/@href').extract()
        except:
            urls = response.xpath('//div[@class="entry-content"]//a/@href').extract()
        for url in urls:
            yield scrapy.Request(url,callback=self.download)

    def download(self,response):
        name_file = response.url.split('/')[-1]
        path = "DiariosAL"
        self.logger.info('Saving PDF %s', name_file)
        with open('{}/{}'.format(path,name_file), 'wb') as f:
            f.write(response.body)

