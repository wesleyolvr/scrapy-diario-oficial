import scrapy
import os

class Estado(scrapy.Spider):
    name='tocatins'
    start_urls = ["https://diariooficial.to.gov.br/busca/?por=texto&texto=+&data-inicial=2000-01-01&data-final=2018-05-03",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=+&data-inicial=2000-01-01&data-final=2017-12-18",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=+&data-inicial=2000-01-01&data-final=2017-07-25",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=+&data-inicial=2000-01-01&data-final=2017-03-06",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2016-10-19",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2016-05-30",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2016-01-06",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2015-08-18",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2015-03-25",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2014-11-03",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2014-06-20",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2014-01-28",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2013-09-17",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2013-04-26",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2012-12-05",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2012-07-17",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2012-02-27",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2011-10-11",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2011-05-18",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2011-01-01",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2010-08-03",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2010-03-18",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2009-10-29",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2009-06-05",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2009-01-08",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2008-08-22",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2008-04-04",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2007-11-14",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2007-06-26",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2007-01-30",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2006-09-12",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2006-04-18",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2005-12-05",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2005-07-12",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2005-02-15",
    "https://diariooficial.to.gov.br/busca/?por=texto&texto=&data-inicial=2000-01-01&data-final=2005-01-03"]
    arquivos = os.listdir('DiariosTO')
    def parse(self,response):
        urls = response.xpath('//td/a/@href').extract()
        for url in urls:
            yield scrapy.Request(url,callback=self.download)
        
    def download(self, response):
        name_file = response.url.split('//')[-1]
        name_file = "_".join(name_file.split('/'))

        if name_file in self.arquivos:
            self.logger.info('Arquivo EXISTENTE!')
        else:
            path = "DiariosTO"
            self.logger.info('Saving PDF %s', name_file)
            with open('{}/{}.pdf'.format(path, name_file), 'wb') as f:
                f.write(response.body)