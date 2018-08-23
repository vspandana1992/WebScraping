""" SpandanaVemulapalli : WebScraping """

from LIB.websites import *
from LIB.download import _download_imgs
import argparse

class _scrape(object):
    def __call__(self,args):
        if args.w.lower() == 'unsplash' : urls = unsplash(args.q.lower())
        if args.w.lower() == 'stocksnap'   : urls = stocksnap(args.q.lower())
        download_imgs     = _download_imgs(args.o,args.q.lower())
        download_imgs(urls)

scrape=_scrape()

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Web Scraping')
    parser.add_argument('-w', choices = ['unsplash','stocksnap'], metavar = 'website', required = True, type = str,
                        help = 'name of the website that you want to scrape data from, example: unsplash,stocksnap')
    parser.add_argument('-q', metavar = 'query', required = True, type = str,
                        help = 'search term for query, example: mushroom')
    parser.add_argument('-o', metavar = 'output directory', required = True, type = str,
                        help = 'Path to the folder where you want the data to be stored, the directory will be created if not present')
    args = parser.parse_args()
    scrape(args)


## command line usage:
#  cd /WebScraping
#  python scrape.py -w unsplash -q mushrooms -o ./Data
