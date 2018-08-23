""" SpandanaVemulapalli : WebScraping """
import requests,math
from tqdm import trange

class _unsplash(object):
    def __init__(self):
        self.website = "https://www.unsplash.com"
        self.session = requests.Session()
    def __call__(self,search):
        base_url   = self.website+"/napi/search/photos?query={0}&xp=&per_page=20&".format(search)
        pages      = self.session.get(base_url).json()['total_pages']
        urls=[]
        for page in trange(1,pages+5,desc = "Downloading image URLs"):
            search_url  = self.website+"/napi/search/photos?query={0}&xp=&per_page=20&page={1}".format(search,page)
            response    = self.session.get(search_url)
            if response.status_code == 200 :
                results = response.json()['results']
                urls    = urls+[(url['id'],url['urls']['raw']) for url in results]
        return list(set(urls))
unsplash = _unsplash()
## Usage : unsplash(<search_term>) ; example : unplash('mushroom')

class _stocksnap(object):
        def __init__(self):
            self.website = "https://www.stocksnap.io"
            self.session = requests.Session()
        def __call__(self,search):
            base_url   = self.website+"/api/search-photos/{0}/relevance/desc/{1}"
            urls       = []
            total       = self.session.get(base_url.format(search,1)).json()['count']
            for page in trange(1,int(math.ceil(total/40.))+1):
                search_url  = base_url.format(search,page)
                response    = self.session.get(search_url)
                if response.status_code == 200 :
                    results = response.json()
                    urls    = urls + [(url['img_id'],"https://cdn.stocksnap.io/img-thumbs/960w/"+url['img_id']+'.jpg') for url in results['results']]
            return list(set(urls))

stocksnap  = _stocksnap()
## Usage : stocksnap(<search_term>) ; example : stocksnap('mushroom')
