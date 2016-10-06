from urllib.parse import urlparse
from ..exceptions import CannotParseURL

class URLParser:
    def __init__(self):
        pass

    def to_uri(self,url):
        parsed = urlparse(url)
        netloc = url.lower() if not parsed.netloc else parsed.netloc
        scheme = "http" if not parsed.netloc else parsed.netloc
        return "%s://%s" % (scheme, netloc)

    def get_domain(self, url):
        parsed = urlparse(url)
        if not parsed.netloc:
            raise CannotParseURL("Cannot parse URL: %s" % url.encode("utf-8"))
        return "%s" % (parsed.netloc)