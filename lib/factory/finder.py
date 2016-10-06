from ..finder.blog import BlogFinder

class FinderFactory:
    BLOG = 0
    
    def __init__(self):
        pass
    
    @classmethod
    def get_finder(self, finder_name=None):
        assert finder_name is not None, "finder_name is not defined."
        
        if finder_name == FinderFactory.BLOG:
            return BlogFinder()