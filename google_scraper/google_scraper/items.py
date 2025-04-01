# google_search/items.py
import scrapy

class GoogleSearchItem(scrapy.Item):
    name = scrapy.Field()               
    address = scrapy.Field()            
    rating = scrapy.Field()             
    reviews = scrapy.Field()            
    service_options = scrapy.Field()    
    place_id = scrapy.Field()            
    place_id_search = scrapy.Field()     
    gps_coordinates = scrapy.Field()     
    thumbnail = scrapy.Field()          
    type = scrapy.Field()               
    lsig = scrapy.Field()               
    description = scrapy.Field()               
