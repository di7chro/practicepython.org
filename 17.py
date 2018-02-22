# practicepython.org
# Övning 17
#
# Use the BeautifulSoup and requests Python packages to print out a list of all the 
# article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

def main():
    base_url = 'http://www.nytimes.com'
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text,"html.parser")

    for story_heading in soup.find_all(class_="story-heading"): 
        if story_heading.a: 
            print(story_heading.a.text.replace("\n", " ").strip())
        else: 
            print(story_heading.contents[0].strip())
if __name__ == "__main__": main()