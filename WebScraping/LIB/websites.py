""" SpandanaVemulapalli : WebScraping """
import requests,math
from tqdm import trange

class _unsplash(object):
    def __init__(self):
        self.website = "https://www.unsplash.com"
        self.session = requests.Session()
    def __call__(self,search,pages=None):
        base_url   = self.website+"/napi/search/photos?query={0}&xp=&per_page=20&".format(search)
        if not pages:
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
        def __call__(self,search,pages=None):
            base_url   = self.website+"/api/search-photos/{0}/relevance/desc/{1}"
            urls       = []
            if not pages:
                pages       = self.session.get(base_url.format(search,1)).json()['count']
            for page in trange(1,int(math.ceil(pages/40.))+1):
                search_url  = base_url.format(search,page)
                response    = self.session.get(search_url)
                if response.status_code == 200 :
                    results = response.json()
                    urls    = urls + [(url['img_id'],"https://cdn.stocksnap.io/img-thumbs/960w/"+url['img_id']+'.jpg') for url in results['results']]
            return list(set(urls))

stocksnap  = _stocksnap()
## Usage : stocksnap(<search_term>) ; example : stocksnap('mushroom')

class _flickr(object):
    def __init__(self):
        self.website = "https://api.flickr.com"
        self.session = requests.Session()
    def __call__(self,search,pages=None):
        base_url   = self.website+"/services/rest?sort=relevance&parse_tags=1&content_type=7&extras=can_comment%2Ccount_comments%2Ccount_faves%2Cdescription%2Cisfavorite%2Clicense%2Cmedia%2Cneeds_interstitial%2Cowner_name%2Cpath_alias%2Crealname%2Crotation%2Curl_c%2Curl_l%2Curl_m%2Curl_n%2Curl_q%2Curl_s%2Curl_sq%2Curl_t%2Curl_z&per_page=25&page={1}&lang=en-US&text={0}&viewerNSID=&method=flickr.photos.search&csrf=&api_key=94378a1af11a0c3e68bc56704192ad50&format=json&hermes=1&hermesClient=1&reqId=539bc2ce&nojsoncallback=1"
        urls       = []
        if not pages:
            pages       = self.session.get(base_url.format(search,1)).json()['photos']['pages']
        for page in trange(1,pages, desc = "Downloading image URLs"):
            search_url  = base_url.format(search,page)
            response    = self.session.get(search_url)
            if response.status_code == 200 :
                try:
                    results = response.json()
                    urls    = urls + [(url['id'],url['url_m']) for url in results['photos']['photo']]
                except:
                    pass
        return list(set(urls))
flickr = _flickr()
