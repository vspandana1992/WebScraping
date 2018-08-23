""" SpandanaVemulapalli : WebScraping : Downloading Images"""

import os
from tqdm import tqdm
import urllib
from concurrent.futures import ProcessPoolExecutor,as_completed

class _download_imgs(object):
    def __init__(self,output_dir,query):
        self.query     = query
        self.directory = output_dir+'/'+query
        if not os.path.isdir(self.directory) : os.makedirs(self.directory)
    def __call__(self,urls):
        with ProcessPoolExecutor() as pool:
            downloads = [pool.submit(urllib.urlretrieve,url[1],self.directory+'/'+url[0]+'.jpg') for url in urls]
            for download in tqdm(as_completed(downloads),total=len(downloads),desc='Downloading '+self.query+" images...."):
                pass
