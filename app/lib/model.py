import config

class LatLong(object):

  def __init__(self, latitude , longitude ):
    self.latitude = latitude
    self.longitude = longitude

class Base(object):

  def __init__(self, vertical, id, title, description, item_type, company_name,
      keywords, show):
    self.id = id
    self.vertical = vertical
    self.title = title
    self.description = description
    self.type = item_type
    self.company_name = company_name
    self.keywords = keywords
    self.show = show

class Deal(Base):

  _NAME_ATTRIBUTE_NAME_MAP = {
      'partnerurl': 'partnerurl', 'address': 'address', 'mobile': 'mobile',
      'price': 'price', 'discount': 'discount', 'originalprice': 'originalprice',
      'offeredprice': 'offeredprice', 'savedpercentage': 'savedpercentage',
      'savedprice': 'savedprice', 'validity': 'validity', 'detailurl': 'detailurl',
      'landingurl': 'landingurl', 'headerimage': 'headerimage',
      'dealimage':'dealimage', 'category': 'category'
    }
  def __init__(self, item):
    super(Deal, self).__init__(
        config.DEALS_VERTICAL, item['id'], item['name'], item['description'],
        item['dealtype'], item['company'], item['feature'].split(','), 1)
    for attr_name, name in self._NAME_ATTRIBUTE_NAME_MAP.items():
      setattr(self, attr_name, item[name])
    self._populated = True

class Ad(Base):

  _NAME_ATTRIBUTE_NAME_MAP = {
      'username': 'UserName', 'rating': 'Rating', 'netprice': 'NetPrice', 'subcategory': 'SubCategory',
      'startedon': 'StartedOn', 'companycode': 'CompanyCode', 'postedon': 'PostedOn', 'advertisertype': 'AdvertiserType',
      'rank': 'Rank', 'pincode': 'PinCode', 'buidingname': 'BuidingName', 'subcategoryid': 'SubCategoryID',
      'category': 'Category', 'city': 'City', 'reposted': 'RePosted', 'locality': 'Locality', 'addesc': 'AdDesc',
      'country': 'Country', 'userid': 'UserID', 'catalogid': 'CatalogID', 'mobile': 'Mobile1', 'state': 'State',
      'cimglogo': 'CImgLogo', 'packageid': 'PackageId', 'ppcvalue': 'PpcValue', 'imgcount': 'ImgCount', 'gllid': 'GLLID'
    }

  def __init__(self, item):
    super(Ad, self).__init__(
        config.ADS_VERTICAL, item['ListingID'], item['AdTitle'], item['AdDescription'],
        item['AdType'], item['CompanyName'], [], item['ShowUp'])
    self.location = LatLong(latitude = item['Latitude'],longitude = item['Longitude'])
    for attr_name, name in self._NAME_ATTRIBUTE_NAME_MAP.items():
      setattr(self, attr_name, item[name])

class Outlet(Base):

  _NAME_ATTRIBUTE_NAME_MAP_SOURCE = {
      'pincode': 'PinCode', 'areasynonymsexact': 'AreaSynonymsExact',
      'locationdidnumber': 'LocationDIDNumber', 'area': 'Area',
      'deleteflag': 'DeleteFlag', 'companylogourl': 'CompanyLogoURL',
      'userid': 'UserID', 'areaaggr': 'AreaAggr',
      'companyaliases': 'CompanyAliases', 'locationtype': 'LocationType',
      'Locationid': 'LocationID', 'cityaggr': 'CityAggr', 'landline': 'LocationLandLine',
      'advertiserurl': 'AdvertiserURL', 'zone': 'Zone',
      'detailslug': 'DetailSlug', 'companyid': 'CompanyID', 'lastupdated': 'LastUpdated',
      'product': 'Product',
      'citysynonyms': 'CitySynonyms', 'businesstype': 'BusinessType', 'contactname': 'ContactName',
      'areaexact': 'AreaExact', 'ppcvoice': 'PPCVoice',
      'cityslug': 'CitySlug', 'country': 'Country', 'ppconline': 'PPCOnline', 'city': 'City',
      'validflag': 'ValidFlag', 'locationdescription': 'LocationDescription',
      'areaslug': 'AreaSlug', 'placeid': 'PlaceID', 'state': 'State', 'address': 'Address',
      'areasynonyms': 'AreaSynonyms', 'nowcustomertype': 'NowCustomerType',
      'zonesserved': 'ZonesServed', 'masterid': 'MasterID', 'edmslocationid': 'EDMSLocationID',
      'landmark': 'Landmark', 'sublocality': 'Sublocality', 'locationaddress': 'LocationAddress',
      'buildingname': 'BuildingName', 'tollfreenumber': 'TollFreeNumber', 'media': 'Media'
  }

  def __init__(self, item):
    super(Outlet, self).__init__(
        config.OUTLETS_VERTICAL, item['_id'], item['_source']['LocationName'],
        item['_source']['CompanyDescription'], 1 if item['_source']['CustomerType'] == 350 else 0,
        item['_source']['CompanyName'], item['_source']['CompanyKeywords'], 1)
    self.sku_ads = False
    self.locationid = item['_id'].split('L')[1]
    self.contact_nos = set(
        item['_source']['LocationMobile'] + item['_source']['ContactMobile'].split(',') if item['_source']['ContactMobile'] else [])
    self.company_email = set(
        item['_source']['LocationEmail'].split(',') if item['_source']['LocationEmail'] else [] +
        item['_source']['ContactEmail'].split(',') if item['_source']['ContactEmail'] else [])
    latilongi = item['_source']['LatLong']
    self.location = LatLong(latitude = latilongi['lat'],longitude = latilongi['lon'])
    for attr_name, name in self._NAME_ATTRIBUTE_NAME_MAP_SOURCE.items():
      setattr(self, attr_name, item['_source'][name])
    self.__clean_product()

  # Cleans up the attributes in the product property
  def __clean_product(self):
    for aproduct in self.product:
      for attr in aproduct:
        if attr in ('intattribute', 'stringattribute'):
          tmp_elements = []
          for element in aproduct[attr]:
            if element['question']:
              tmp_elements.append(element)
          aproduct[attr] = tmp_elements
