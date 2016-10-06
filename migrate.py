from lib.factory.parser import ParserFactory
from curtsies           import fmtstr
import csv
import os
import pymongo
import arrow
import tomorrow

@tomorrow.threads(10)
def migrate(line):
    country = line[0]
    url     = line[2]

    # url should not inside blogspot_crawlers
    conn = pymongo.MongoClient("mongodb://220.100.163.132/blogspot_crawler")
    db   = conn["blogspot_crawler"]
    docs = db.blog_list.find({"url":url.lower()})
    conn.close()

    try:
        assert docs.count() == 0
        assert ".com" in url[-4:] or ".in" in url[-3:]
        assert " " not in url

        parser = ParserFactory.get_parser(ParserFactory.URL)
        url    = parser.to_uri(url)
        domain = parser.get_domain(url)

        # inserting to database
        conn = pymongo.MongoClient("mongodb://220.100.163.132/blog_crawler")
        db   = conn["blog_crawler"]
        db.blog_list.create_index([("domain", pymongo.ASCENDING)], unique=True)
        db.blog_list.insert_one({
            "_insert_time" : arrow.utcnow().datetime,
                     "url" : url,
                  "domain" : domain,
                 "country" : country,
               "is_active" : True
        })
        conn.close()
        print(fmtstr("[migrate][success] Success: %s" % url.encode("utf-8"), "green"))
    except AssertionError:
        print(fmtstr("[migrate][error] URL is not valid: %s" % url.encode("utf-8"),"red"))
    except pymongo.errors.DuplicateKeyError:
        print(fmtstr("[migrate][error] Duplicate domain: %s" % domain.encode("utf8"),"red"))

if __name__ == "__main__":
    reader = csv.reader(open(os.path.join(os.getcwd(),"data","blog_list.csv"),"r"))
    result = [migrate(line) for line in reader]
