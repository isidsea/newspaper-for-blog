from curtsies import fmtstr
import pymongo
import arrow

class ArticleSaver:
    def __init__(self):
        pass

    def save(self, article=None):
        assert article is not None, "article is not defined."
        article.update({"_insert_time" : arrow.utcnow().datetime})
        article.update({"converted": False})
        article.update({"TTL" : arrow.utcnow().datetime})

        conn = pymongo.MongoClient("mongodb://220.100.163.132/blog_crawler")
        db   = conn["blog_crawler"]
        db.data.create_index([("permalink", pymongo.ASCENDING)], unique=True)
        db.data.create_index([("TTL", pymongo.ASCENDING)], expireAfterSeconds=60*60*24*30)

        try:
            db.data.insert_one(article)
            print(fmtstr("[ArticleSaver][success] Inserted One Document!","green"))
        except pymongo.errors.DuplicateKeyError:
            print(fmtstr("[ArticleSaver][error] Duplicate Document!","red"))
        finally:
            conn.close()