import requests
from bs4 import BeautifulSoup
import bookClass as Book
import functions

def scraper():
    responseStatus = 200
    webpageNumber = 1
    books = []
    print("scraping book store...")
    while responseStatus == 200:
        try:
            pageToScrape = requests.get(f"https://books.toscrape.com/catalogue/page-{webpageNumber}.html")
            responseStatus = pageToScrape.status_code
            
            soup = BeautifulSoup(pageToScrape.text, "html.parser")
            listings = soup.findAll("li", attrs={"class", "col-xs-6 col-sm-4 col-md-3 col-lg-3"})
    
            for listing in listings:
                price = listing.find("p", class_="price_color")
                name = functions.getName(listing)
                starRating = functions.getRating(listing)
                bookDictionary= {"Title" : name, "Price" : price.text[2:], "rating": starRating}
                books.append(bookDictionary)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return
        webpageNumber = webpageNumber +1
    print(books)
scraper()