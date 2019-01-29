import scrapy

class Estado(scrapy.Spider):
    name='minas'
    start_urls = ["http://jornal.iof.mg.gov.br/xmlui/search?order=DESC&rpp=100&sort_by=0&page={}&query=%28%28bloco%3A%28++Di%C3%A1rio++do++Executivo%29%29+OR+%28bloco%3A%28++Di%C3%A1rio++do++Legislativo%29%29+OR+%28bloco%3A%28++Di%C3%A1rio++do++Judici%C3%A1rio%29%29++OR+%28bloco%3A%28++Di%C3%A1rio++da++Justi%C3%A7a%29%29+%29+AND++data%3A%5B20050129+TO+20190129%5D+&etal=0".format(i) for i in range(1,1329)]


    def parse(self,response):
        for i in response.xpath('//div[@id="id-resultado-pesquisa"]//a/@onclick').extract():
            url = i.split(',')[0].replace("window.open('","").replace("'","")
            yield scrapy.Request(url=url,callback=self.link_pdf)
        
    
    def link_pdf(self,response):
        urls = response.xpath('//*[@id="framePdf"]/@src').extract()
        info = response.xpath('//div[@id="id-div-nome-caderno"]//text()').extract()
        for link in urls:
            yield scrapy.Request(url=link, meta={
                "name_doc":info[0],
                "date":info[1],
            }, callback=self.download)
    
    def download(self, response):
        name = response.meta['name_doc']
        date = "_".join(response.meta['date'].split('/'))
        name_file = name+date
        path = "DiariosMG"
        self.logger.info('Saving PDF %s', name_file)
        with open('{}/{}.pdf'.format(path, name_file), 'wb') as f:
            f.write(response.body)
