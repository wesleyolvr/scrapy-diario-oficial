import scrapy


class Estado(scrapy.Spider):
    name = 'paraiba'
    start_urls = ['https://auniao.pb.gov.br/servicos/arquivo-digital/doe/2018',
                  "https://auniao.pb.gov.br/servicos/arquivo-digital/doe/2017",
                  "https://auniao.pb.gov.br/servicos/arquivo-digital/doe/2016",
                  "https://auniao.pb.gov.br/servicos/arquivo-digital/doe/2015"
                  ]

    def parse(self, response):
        urls = response.xpath('//span[@class="summary"]//a/@href').extract()
        for url in urls:
            yield scrapy.Request(url, callback=self.meses)

    def meses(self, response):
        urls = response.xpath('//span[@class="summary"]//a/@href').extract()
        for url in urls:
            yield scrapy.Request(url, callback=self.dias)

    def dias(self, response):
        link_pdf = response.xpath(
            '//span[@id="form-widgets-file"]//a/@href').extract()
        for link in link_pdf:
            yield scrapy.Request(link, callback=self.download)

    def download(self, response):
        name_file = response.url.split('/')[-1]
        path = "DiariosPB"
        self.logger.info('Saving PDF %s', name_file)
        with open('{}/{}'.format(path, name_file), 'wb') as f:
            f.write(response.body)
