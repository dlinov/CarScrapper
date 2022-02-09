# CarScrapper
Simple scrapper of cars from ab.onliner.by, using Scrapy, MongoDB and Flask.

## Run
- run mongo locally, e.g. `mongod --config /usr/local/etc/mongod.conf`  
or `docker-compose up -d`
- `cd carscrapper` and `scrapy crawl cars`
- `cd webapp` and `python3 app.py`

## TODO
### venv
- Ubuntu
    - run `sudo apt install python3-venv firefox-geckodriver`
    - run `python3 -m venv ./venv`
    - run `source ./venv/bin/activate`
    - (optional) run `pip3 install --upgrade pip`. Couldn't install selenium before this.
    - (optional) run `pip3 install wheel`. Added here because there was an error "invalid command bdist-wheel" when installing scrapy

### docker-compose
- TODO

### schedule scrapy runs
- TODO
