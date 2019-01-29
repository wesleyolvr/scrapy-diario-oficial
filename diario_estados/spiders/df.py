import scrapy

class EstadoScrapy(scrapy.Spider):
    name= 'df'
    start_urls = ["http://www.dodf.df.gov.br/listar#2009/12_Dezembro/DODF%20252%2031-12-2009"]


    def parse(self,response):
        urls = ["http://www.dodf.df.gov.br/listar#2009/12_Dezembro/DODF%20252%2031-12-2009"]
        data= {
            "dir":"2009/12_Dezembro/DODF%20252%2031-12-2009",
        }
        for url in urls:
            yield scrapy.FormRequest(url=url, formdata=data,callback=self.parse1)
        # anos = response.xpath('//div[@class="arquivo"]/@data-file').extract()

    def parse1(self,response):
        print(response.xpath('//a/@href').extract())
        print(response.body_as_unicode())