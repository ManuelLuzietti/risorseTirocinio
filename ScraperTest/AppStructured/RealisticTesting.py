from Crawler import Crawler
from KeywordsGenerator import generate
crawler = Crawler(False,debug=True)
fbList = [
    "league of legends",
    "lol",
    "leagueoflegends",
    "leagueoflegend"
]
generate(fbList)

def test1():
   
    crawler.manualCookieJarSetter("https://www.nulled.to")
    crawler.setScraperConfig(["https://www.nulled.to"],regex=True)
    crawler.initializeDrivers()
    crawler.addBlockedPath("nulled.to/user/")
    
    crawler.enableQueryTruncation()
    crawler.setGetTimeout(15)
    #crawler.setTimeoutForRequests(2)
    crawler.start()

def test2():
    crawler.initializeDrivers()
    crawler.manualCookieJarSetter()
    
testDic = {
    "1" : test1,
    "2" : test2
}

if __name__ == "__main__":
    num = input("insert n. test: ")
    testDic[num]()
    