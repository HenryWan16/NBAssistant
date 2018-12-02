from crawler import WebCrawler


if __name__ == '__main__':
    web_crawler = WebCrawler()
    web_crawler.craw()
    web_crawler.driver.close()
    web_crawler.driver.quit()