import random
import json

available_brands = ['samsung', 'sony', 'apple', 'nokia', 'motorola', 'adidas', 'nike']
available_categories = ['mobile phones', 'electronics', 'gadgets', 'house hold', 'furniture', 'laptops', 'cameras']

available_product_titles = ['iPhone 5', 'Samsung Galaxy S4', 'Xiaomi mi4i', 'Samsung Gear']
available_variant_titles = ['iPhone 5 16 GB', 'iPhone 5 32 GB', 'Samsung Galaxy S4 32 GB', 'Xiaomi mi4i Red', 'Samsung Gear black']

def get_random_item(name):
  ind = random.randint(0, len(name)-1)
  return name[ind]

class Category:
  def __init__(self):
    self.id = random.randint(1000, 9999)
    self.label = get_random_item(available_categories)

class AttributeGroup:
  __all_attribs = [
      {'name' : 'height', 'display' : 'Height', 'values' : [6], 'unit' : 'cm', 'filter' : False},
      {'name' : 'width', 'display' : 'Width', 'values' : [3], 'unit' : 'cm', 'filter' : False},
      {'name' : 'depth', 'Depth' : 'Height', 'values' : [10], 'unit' : 'mm', 'filter' : False},
      {'name' : 'weight', 'display' : 'Weight', 'values' : [50], 'unit' : 'g', 'filter' : False}
    ]
  
  def __get_attributes(self):
    ind = random.randint(0, len(self.__all_attribs)-1)
    return self.__all_attribs[ind:]

  def __init__(self):
    self.name = "dimensions"
    self.attributes = self.__get_attributes()

class Variant:
  def __init__(self, productId):
    self.productId = productId
    self.variantId = random.randint(10000000, 99999999)
    self.title = get_random_item(available_variant_titles)
    self.subscriptions = [Subscription(productId = self.productId, variantId = self.variantId) for i in range(6)]
    self.media = [Media() for i in range(2)]
    self.attributes = [
      {'name' : 'RAM', 'display' : 'Memory', 'values' : [32], 'filter' : True, 'unit' : 'GB'}
    ]
  def __update_fields(self):
    # ugly hack. ideally a subscription manager should handle it
    self.subscriptions[0].buyBox = True
    self.media[0].default = True

class Subscription:
  def __init__(self, productId, variantId):
    self.subscriptionId = random.randint(10000000, 99999999)
    self.variantId = variantId
    self.productId = productId
    self.basePrice = random.randint(40000, 50000)
    self.offerPrice = random.randint(10000, 40000)
    self.offerValidTill = '2015-07-30T23:59'
    self.media = [Media() for i in range(2)]
    self.condition = ''
    self.payment = {'mode' : ['pay-now', 'pay-later']}
    self.nddCities = ['delhi']
    self.merchant = Merchant()
    self.buyBox = False #one sunscription will have buy box true
    self.shippingTimeHours = 12
    self.leadTimeHours = 12
    self.cod = True

class Media:
  def __init__(self):
    self.id = random.randint(10000000, 99999999)
    self.default = False
    self.variants = [
      {'size' : 'thumb', 'height' : 200, 'width' : 200, 'dpi' : 120, 'url' : 'http://media.askmebazaar.com/media/catalog/product/thumbnails/150x150/i/n/in_efc-1j9fbeginu_000030182_front1_white.jpg'},
    ]

class Location:
  def __init__(self):
    self.id = "361414"
    self.parent = "7992791"
    self.level = "locality"
    self.name = "M-block market"
    self.synonyms = ["M-block"]
    self.lat = "28.5502515"
    self.lon = "77.2352949"
    self.north = "28.5512599"
    self.south = "28.5492431"
    self.east = "77.2368211"
    self.west = "77.2337687"
    self.shape = []
    self.related = []
    self.created = "2010-11-12"
    self.updated = "2012-11-12"

class Contact:
  def __init__(self):
    self.id = "12323432"
    self.name = {
        "full" : "Mr. Rahul Chitale",
        "salutation" : "Mr.",
        "first" : "Rahul",
        "middle" : "",
        "last" : "Chitale",
        "suffix" : "",
        "nick"  : "Rahul"
    },
    self.designation = "CTO"
    self.department = "IT"
    self.emails = [ { "address" : "rahul.chitale@getitinfomedia.com", "verified" : "true" } ]
    self.phones = [ { "type" : "mobile", "num" : "+91-9485455455", "verified" : "true" } ]
    self.address = Address()

class Address:
  def __init__(self):
    self.id = "1232141"
    self.title = "Getit Infomedia"
    self.location = Location()
    self.lines = [ "4th Floor", "Tower-A, Iris Tech Park" ]
    self.area = "Sohna Road"
    self.city = "Gurgaon"
    self.state = "Haryana"
    self.country = "India"
    self.pincode = "122001"
    self.landmarks = [ "Next to Vipul Greens" ]
    self.phones = [
        { "type" : "landline", "num" : "+91-124-564654646" }, 
        { "type" : "fax", "num" : "+91-124-564654646" },
        { "type" : "toll-free", "num" : "1800-600-1331" } 
    ]

class Merchant:
  def __init__(self):
    self.merchantId = random.randint(10000000, 99999999)
    self.contact = Contact()
    self.address = Address()
    self.rating = random.randint(1,5)
    self.ratingCount = random.randint(10, 50)
 
class Product:
  def __init__(self):
    self.productId = random.randint(10000000, 99999999)
    self.title = get_random_item(available_product_titles)
    self.categories = []
    for i in range(3):
      self.categories.append(Category())
    self.variants = [Variant(productId = self.productId) for i in range(6)]
    self.brand = get_random_item(available_brands)
    self.media = [Media() for i in range(2)]
    self.userRating = random.randint(1,5)
    self.expertRating = random.randint(1,5)
    self.ratingCount = random.randint(1,100)
    self.description = 'blah'
    self.features = 'blah'
    self.specification = 'blah'
    self.attributeGroups = [AttributeGroup() for i in range(3)]
    self.__update_fields()

  def __update_fields(self):
    self.media[0].default = True

class Ret:
  def __init__(self, results):
    self.results = results
    self.facets = [
        {
            'brand': [
                'samsung'
            ]
        }
    ]
    self.type = 'products'
    self.total_results = len(self.results)

  def as_json(self):
    return json.dumps(self, default=lambda o: o.__dict__, 
          sort_keys=True, indent=4)

if __name__=="__main__":
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument('count', type=int, help='Number of product objects to generate')
  args = parser.parse_args()
  count = args.count
  product_list = []
  for i in range(count):
    product_list.append(Product())

  ret = Ret(product_list)
  print ret.as_json()


