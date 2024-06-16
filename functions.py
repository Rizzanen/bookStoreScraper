from bs4 import BeautifulSoup

def getName(listing):
    headers = listing.find_all("h3")
    for header in headers:
        name = header.find("a")
        return name.text
    
def getRating(listing):
    p = listing.find("p", attrs={"class", "star-rating"})
    classNames = p["class"]
    if classNames[1] == "One":
        return 1
    elif classNames[1] == "Two":
        return 2
    elif classNames[1] == "Three":
        return 3
    elif classNames[1] == "Four":
        return 4
    else:
        return 5
   