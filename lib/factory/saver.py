from ..saver.article        import ArticleSaver
from ..saver.failed_article import FailedArticleSaver

class SaverFactory:
    ARTICLE        = 0
    FAILED_ARTICLE = 1

    def __init__(self):
        pass

    @classmethod
    def get_saver(self, saver_name=None):
        assert saver_name is not None, "saver_name is not defined."

        if saver_name == SaverFactory.ARTICLE:
            return ArticleSaver()
        elif saver_name == SaverFactory.FAILED_ARTICLE:
            return FailedArticleSaver()

