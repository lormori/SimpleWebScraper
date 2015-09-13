import sys
import SimpleWebScraper
import ScraperTimer
import time

def main():
    ## create timer arguments as a tuple
    args = ("https://www.kickstarter.com/projects/coolminiornot/zombicide-black-plague", "../ScrapingData/BlackPlague.txt")
    #args = ("https://www.kickstarter.com/projects/loneshark/the-apocrypha-adventure-card-game", "../ScrapingData/BlackPlague.txt") # TODO: need to work out what  to do with ended projects
    scraper_timer = ScraperTimer.ScraperTimer(5, SimpleWebScraper.open_website, *args)
    scraper_timer.start()

    try:  
        time.sleep(10) # your long-running job goes here...
    finally:
        scraper_timer.stop()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()