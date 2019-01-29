import scrapy

class EstadoScrapy(scrapy.Spider):
    name='estado'
    urls = ["http://www.spdo.ms.gov.br/diariodoe#page-1"]

    def parse(self,response):
        urls = ["http://www.spdo.ms.gov.br/DiarioDOE/Index/Index/1"]
        data = {
        "Filter.Numero":'' ,
        "Filter.DataInicial":'01/01/2000',
        "Filter.DataFinal":'26/01/2019',
        "Filter.Texto":'',
        "Filter.TipoBuscaEnum": 1,
        }
        for url in urls:
            yield scrapy.FormRequest(url,formdata=data,callback=self.parse_links)
    
    def parse_links(self,response):
        pass