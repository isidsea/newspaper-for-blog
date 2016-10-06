from lib.factory.finder import FinderFactory
from lib.factory.engine import EngineFactory
import multiprocessing

def crawl(blog):
    engine = EngineFactory.get_engine(EngineFactory.GENERIC)
    engine.crawl(blog)

if __name__ == "__main__":
    finder = FinderFactory.get_finder(FinderFactory.BLOG)
    blogs  = finder.find(is_active=True)
    
    with multiprocessing.Pool(5) as pool:
        pool.map(crawl, blogs)