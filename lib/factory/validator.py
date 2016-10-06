from ..validator.content        import ContentValidator
from ..validator.article        import ArticleValidator
from ..validator.published_date import PublishedDateValidator

class ValidatorFactory:
    CONTENT = 0
    ARTICLE = 1

    def __init__(self):
        pass

    @classmethod
    def get_validator(self, validator_name=None):
        assert validator_name is not None, "validator_name is not defined."

        if validator_name == ValidatorFactory.CONTENT:
            return ContentValidator()
        elif validator_name == ValidatorFactory.ARTICLE:
            return ArticleValidator()
        elif validator_name == ValidatorFactory.PUBLISHED_DATE:
            return PublishedDateValidator()