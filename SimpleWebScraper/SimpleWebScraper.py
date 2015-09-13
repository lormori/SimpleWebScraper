import urllib2
import re
import ScraperTimer
import JsonDataWrapper

def scrape_webpage(webpage):
    results = re.findall("\[\w{7}\]\">(\S+)</", webpage) # this regular expression returns the amount pledged now, it is specific to the web page
    for result in results:
        print(result)
    return results

def open_website(*args):
    site_name = args[0] # zero index is the website
    filepath = args[1] # index one is the file path to save the file to

    print("Opening", site_name,"...")

    html_page = urllib2.urlopen(site_name)
    kickstarter_page = html_page.read()
    print kickstarter_page
    scraping_data = scrape_webpage(str(kickstarter_page))
    print scraping_data
    jsonWrapper = JsonDataWrapper.JsonDataWrapper(filepath)
    jsonWrapper.LoadJsonData()

    for data in scraping_data:
        jsonWrapper.AddNewScrapeEntry(data)

    jsonWrapper.WriteJsonData()

    return