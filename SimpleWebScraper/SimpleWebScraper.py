import sys
import urllib.request
import re

def manipulate_webpage(webpage):
    results = re.findall("\[\w{7}\]\">(\S+)</", webpage) ## this regular expression returns the amount pledged now
    for result in results:
        print(result)
    return results

def open_website(site_name, filepath):
    print("Opening", site_name, "...")
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
    open_website("https://www.kickstarter.com/projects/coolminiornot/zombicide-black-plague", "../ScrapingData/BlackPlague.txt")

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()