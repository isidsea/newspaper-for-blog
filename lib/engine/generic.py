from ..factory.parser    import ParserFactory
from ..factory.saver     import SaverFactory
from ..factory.validator import ValidatorFactory
from ..exceptions        import ParseError, ValidationError
from curtsies            import fmtstr
import newspaper

class GenericEngine:
    def __init__(self, blog=None):
        self.blog = blog

    def crawl(self, blog=None):
        self.blog = blog if blog is not None else self.blog

        assert "url" in blog, "url is not defined."

        paper = newspaper.build(blog["url"])
        for article in paper.articles:
            try:
                parser  = ParserFactory.get_parser(ParserFactory.ARTICLE)
                article = parser.parse(
                           article = article,
                           country = blog["country"],
                            domain = blog["domain"],
                    author_default = blog["domain"]
                )

                validator = ValidatorFactory.get_validator(ValidatorFactory.ARTICLE)
                validator.validate(article)

                saver = SaverFactory.get_saver(SaverFactory.ARTICLE)
                saver.save(article)
            except ParseError as ex:
                print(fmtstr("[GenericEngine][error] %s" % ex.encode("utf-8"),"red"))
            except ValidationError as ex:
                print(fmtstr("[GenericEngine][error] %s" % ex.encode("utf-8"),"red"))

                parser   = ParserFactory.get_parser(ParserFactory.ARTICLE)
                document = parser.parse_to_failed(article, reason="%s" % ex)

                saver = SaverFactory.get_saver(SaverFactory.FAILED_ARTICLE)
                saver.save(document)