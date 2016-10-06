from ..parser.url     import URLParser
from ..parser.article import ArticleParser

class ParserFactory:
    URL     = 0
    ARTICLE = 1
    
    def __init__(self):
        pass

    @classmethod
    def get_parser(self, parser_name=None):
        assert parser_name is not None, "parser_name is not defined."

        if(parser_name == ParserFactory.URL):
            return URLParser()
        elif parser_name == ParserFactory.ARTICLE:
            return ArticleParser()