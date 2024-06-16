import requests
from bs4 import BeautifulSoup
import bookClass as Book
import functions


def scraper():
    pageToScrape = requests.get("https://books.toscrape.com/catalogue/category/books/horror_31/index.html")
    soup = BeautifulSoup(pageToScrape.text, "html.parser")
    listings = soup.findAll("li", attrs={"class", "col-xs-6 col-sm-4 col-md-3 col-lg-3"})
    

    #     listings = container.findAll("listing-search")
    #     print(listings)
    for listing in listings:
        price = listing.find("p", class_="price_color")
        name = functions.getName(listing)
        starRating = functions.getRating(listing)
        
        print(f"Name: {name} \nPrice: {price.text[2:]}€ \nStar rating: {starRating}\n")
        
scraper()