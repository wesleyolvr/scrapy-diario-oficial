import scrapy

class EstadoScrapy(scrapy.Spider):
    name='Pernambuco'
    start_urls = ["https://ws.cepe.com.br/publicar/dows.php?"]
    
    def parse(self,response):
        d = {
            "PoderExecutivo":"1-PoderExecutivo",
            "TribunaldeContas":"2-TribunaldeContas",
            "MinisterioPublico":"3-MinisterioPublico",
            "PoderJudiciarioFederal":"5-PoderJudiciarioFederal",
            "PoderLegislativo":"6-PoderLegislativo",
            "DefensoriaPublica":"7-DefensoriaPublica",
            "PrefeituradoRecife":"8-PrefeituradoRecife"
        }
        todos = response.body_as_unicode().split('&')