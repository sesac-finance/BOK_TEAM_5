

BOT_NAME = 'hankyung_news'

SPIDER_MODULES = ['hankyung_news.spiders']
NEWSPIDER_MODULE = 'hankyung_news.spiders'


# ITEM_PIPELINES = {'hankyung_news.pipelines.CsvPipeline': 300, }

# FEED_FORMAT = "csv"
FEED_EXPORT_ENCODING = 'utf-8-sig'

FEED_EXPORT_FIELDS=["title", "date","content"]
# #Name of the file where data extracted is stored
# FEED_URI = "test.csv"

LOG_FILE = 'hankyung.log'

REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
