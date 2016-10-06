from .content        import ContentValidator
from .published_date import PublishedDateValidator

class ArticleValidator:
    def __init__(self):
        pass

    def validate(self, article=None):        
        validator = ContentValidator()
        validator.validate(article["content"])
        
        validator = PublishedDateValidator()
        validator.validate(article["published_date"])