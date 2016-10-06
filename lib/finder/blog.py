import pymongo 

class BlogFinder:
    def __init__(self):
        pass

    def find(self, **kwargs):
        conn = pymongo.MongoClient("mongodb://220.100.163.132/blog_crawler")
        db   = conn["blog_crawler"]
        docs = db.blog_list.find(kwargs)
        conn.close()
        return docs