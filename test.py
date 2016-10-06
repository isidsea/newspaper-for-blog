from lib.factory.parser import ParserFactory
from lib.factory.saver  import SaverFactory
import newspaper

if __name__ == "__main__":
    paper   = newspaper.build("http://cnn.com")
    article = paper.articles[0]

    parser  = ParserFactory.get_parser(ParserFactory.ARTICLE)
    article = parser.parse(article)

    saver = SaverFactory.get_saver(SaverFactory.ARTICLE)
    saver.save(article)