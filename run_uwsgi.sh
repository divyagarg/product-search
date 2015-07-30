#nohup /apps/.virtualenvs/product-search/bin/uwsgi --ini /apps/product-search/uwsgi.ini >product-search.out &
nohup uwsgi --ini product_search_uwsgi.ini >/tmp/product-search.out &
