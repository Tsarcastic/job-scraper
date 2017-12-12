"""Scape them jobs real good."""

import requests
from bs4 import BeautifulSoup

paramss = div="-job-summary "
r = requests.get('https://stackoverflow.com/jobs/developer-jobs-using-python', params=paramss)
soup = BeautifulSoup(r, html-parser)
def r_print():
    print(soup)
    
if __name__ == '__main__':
    r_print()