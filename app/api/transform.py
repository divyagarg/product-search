import os
import random
import json
import urllib
import urlparse

def update_url(url, query_param):
    parsed = urlparse.urlparse(url)
    if parsed.query:
        prefix = '&'
    else:
        prefix = '?'
    return url + prefix + query_param

def transform():
    f = open('data/products_bestsellers.json')
    data = json.loads(f.read())
    f.close()
    results = data['results']
    for item in results:
        item['baseProductId'] = random.randint(100000, 999999)
        item['sellersCount'] = random.randint(1,25)
        item['category'] = random.randint(100000, 999999)
        item['media'] = [{
            'type' : 'image',
            'url' : item['img'],
            'width' : 100,
            'height' : 100,
            'alt' : item['title'],
            'id' : random.randint(100000, 999999)
        }]
        item['offerPrice'] = int(item['offerPrice'].strip())
        item['basePrice'] = int(item.get('basePrice', item['offerPrice']))
        item['discount'] = int(((float(item['basePrice']) - float(item['offerPrice']))/float(item['basePrice']))*100)
        del item['img']
        item['embedUrl'] = update_url(item['url'], 'embed=true')
    out_data = json.dumps(data)
    f = open('data/products.json', 'w')
    f.write(out_data)
    f.close()

if __name__=="__main__":
    transform()