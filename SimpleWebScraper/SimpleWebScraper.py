import sys
import urllib.request
import re
import ScraperTimer
import time

def manipulate_webpage(webpage):
    results = re.findall("\[\w{7}\]\">(\S+)</", webpage) ## this regular expression returns the amount pledged now
    for result in results:
        print(result)
    return results

def open_website(*args):
    site_name = args[0] # zero index is the website
    filepath = args[1] # index one is the file path to save the file to

    print("Opening", site_name,"...")

    html_page = urllib.request.urlopen(site_name)
    kickstarter_page = html_page.read()
    scraping_data = manipulate_webpage(str(kickstarter_page))

    print(scraping_data)
    file = open(filepath, 'r')
    lines = file.readlines();
    
    file = open(filepath, 'w')

    for data in scraping_data:
        lines.append(data + '\n')

    for line in lines:
        file.writelines(line)

    file.close()
    return

def main():
    ## create timer arguments as a tuple
    args = ("https://www.kickstarter.com/projects/coolminiornot/zombicide-black-plague", "../ScrapingData/BlackPlague.txt")
    scraper_timer = ScraperTimer.ScraperTimer(10, open_website, *args)
    scraper_timer.start()

    try:  
        time.sleep(20) # your long-running job goes here...
    finally:
        scraper_timer.stop()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()