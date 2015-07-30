HOME = '/tmp/apiserver'
LOG_DIR = 'logs'
LOG_FILE = 'apiserver.log'
DEBUG_LOG_FILE = 'debug_apiserver.log'
ERROR_LOG_FILE = 'error_apiserver.log'

PORT = 5000

DEALS_URL = 'http://developers.askme.com/service/service.ashx?method=searchme&app=6&actn=46&what=%s&ver=2&city=%s'
ADS_URL = 'http://developers.askme.com/ads/?q=%s&city=%s'
OUTLETS_URL = ('http://search.production.askme.com:9999/search/askme/place'
    '?kw=%s&city=%s&source=true')

ADS_IMAGES_URL = 'http://developers.askme.com/ads/activeimagebyids/listingid/%s/'
SKU_LISTING_URL = 'http://developers.askme.com/ads/aplfa/%s/'

DEALS_NO_RESULTS = 'No Result Found'

OUTLETS_VERTICAL = 'OUTLETS'
ADS_VERTICAL = 'ADS'
DEALS_VERTICAL = 'DEALS'
ALL_VERTICALS = [OUTLETS_VERTICAL, ADS_VERTICAL, DEALS_VERTICAL]

CATEGORY_FILTER = 'categories'
AREA_FILTER = 'area'
FILTERS = {
  CATEGORY_FILTER: 'categories',
  AREA_FILTER: 'area'
}

OUTLETS_PAGE_SIZE = '20'
OUTLETS_OFFSET = '0'
ADS_PAGE_SIZE = '10'