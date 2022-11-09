import scrapy
from..items import ProductsItem

class ProductsSpiderSpider(scrapy.Spider):
    name = 'products'
    #allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?rh=n%3A16225007011&fs=true&ref=lp_16225007011_sar']

    def parse(self, response):
        items = ProductsItem()
        
        all_products = response.css('.s-search-results')
        
        for product in all_products:
            product_name = response.css('.a-size-base-plus::text').extract()
            product_price = response.css('.a-price-fraction , .a-price-whole').css('::text').extract()
            product_imagelink = response.css('.s-height-equalized .s-image::attr(src)').extract()
            
            items['product_name'] = product_name
            items['product_price'] = product_price
            items['product_imagelink'] = product_imagelink
            
            yield items
