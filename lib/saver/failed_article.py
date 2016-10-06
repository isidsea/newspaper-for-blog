import pymongo
import arrow 

class FailedArticleSaver:
    def __init__(self):
        pass

    def save(self, document=None):
        assert document is not None, "documet is not defined."
        document.update({"_insert_time": arrow.utcnow().datetime})
        conn = pymongo.MongoClient("mongodb://220.100.163.132/blog_crawler")
        db   = conn["blog_crawler"]

        db.failed_urls.create_index([("permalink", pymongo.ASCENDING)], unique=True)

        try:
            db.failed_urls.insert_one(document)
        except:
            pass
        finally:
            conn.close()