import json

class GoogleSearchPipeline:
    def open_spider(self, spider):
        self.file = open('result_search.json', 'w', encoding='utf-8')
        self.data = []

    def close_spider(self, spider):
        json.dump(self.data, self.file, ensure_ascii=False, indent=4)
        self.file.close()
        spider.logger.info("Data has been saved to result_search.json")

    def process_item(self, item, spider):
        self.data.append(dict(item))
        return item