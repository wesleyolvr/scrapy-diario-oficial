import scrapy

class EstadoScrapy(scrapy.Spider):
    name='estado'
    urls = ["http://www.spdo.ms.gov.br/diariodoe#page-1"]

    def parse(self,response):
        url = "http://www.spdo.ms.gov.br/DiarioDOE/Index/Index/1"
        data = {
        "Filter.Numero":Filter.Numero: ,
        "Filter.DataInicial":Filter.DataInicial: 01/01/2000,
        "Filter.DataFinal":Filter.DataFinal: 26/01/2019,
        "Filter.Texto":Filter.Texto: ,
        "Filter.TipoBuscaEnum":Filter.TipoBuscaEnum: 1,
        }
