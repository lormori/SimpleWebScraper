import sys
import urllib.request
import re

def manipulate_webpage(webpage):
    results = re.findall("\[\w{7}\]\">(\S+)</", webpage) ## this regular expression returns the amount pledged now
    for result in results:
        print(result)
    return results

def open_website(site_name):
    print("Opening", site_name, "...")
    html_page = urllib.request.urlopen(site_name)
    kickstarter_page = html_page.read()

    scraping_data = manipulate_webpage(str(kickstarter_page))

    print(scraping_data)
    file = open("../ScrapingData/BlackPlague.txt", 'w')
    for data in scraping_data:
        file.writelines(data)
    file.close()
    return

def main():
    open_website("https://www.kickstarter.com/projects/coolminiornot/zombicide-black-plague")

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()