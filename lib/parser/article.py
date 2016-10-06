from ..exceptions import ParseError
import arrow

class ArticleParser:
    def __init__(self):
        pass

    def parse(self, article=None, country=None, domain=None, **kwargs):
        assert article is not None, "article is not defined."
        assert country is not None, "country is not defined."
        assert domain  is not None, "domain is not defined."

        author_default = kwargs.get("author_default", "")

        article.download()
        if not article.html:
            raise ParseError("Cannot get HTML from: %s" % article.url)
        article.parse()
        document = {
                     "title" : article.title,
                   "content" : article.text,
                    "author" : article.authors[0] if len(article.authors)>0 else author_default,
            "published_date" : article.publish_date,
                 "permalink" : article.url,
                   "country" : country,
                    "domain" : domain
        }
        return document

    def parse_to_failed(self, article=None, reason=None):
        assert article     is not None, "article is not defined."
        assert reason      is not None, "reason is not defined."
        assert "permalink" in article , "permalink is not defined."
        assert "domain"    in article , "domain is not defined."

        document = {
            "_insert_time" : arrow.utcnow().datetime,
               "permalink" : article["permalink"],
                  "domain" : article["domain"],
                  "reason" : reason
        }
        return document