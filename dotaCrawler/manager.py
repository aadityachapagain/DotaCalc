from os import system, getcwd, listdir
from dotaCrawler.settings import FEED_URI
from server import runServer

filename = FEED_URI


def main():
    if filename in listdir(getcwd()):
        print("file is in the path you are ready to go !")
        runServer()
        return
    else:
        print("file is not in the path run the spider first")
        print('This will take few time')
        system("scrapy crawl dota_scrape --nolog")
        runServer()


if __name__ == '__main__':
    main()
    print(" Closing Server ...... !")