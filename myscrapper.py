# This program will scrape reviews and ratings for a product from a supported website.
# List of currenlty supported websites - amazon.in

import logging
import requests


class MyScrapper:
    def __init__(self, product_name, product_url):
        self.logger = logging.getLogger('customLogger')
        self.prd_name = product_name
        self.prd_url = product_url
        self.logger.info("Product Name - {}".format(self.prd_name))
        self.logger.debug("Product URL - {}".format(self.prd_url))

    def scrape_url(self):
        url_req = requests.get(self.prd_url)
        self.logger.debug("Creating a html file for the response.")
        with open('request_file.html', 'w') as fh:
            fh.write(url_req.text)




