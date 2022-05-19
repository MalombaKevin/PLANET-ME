import urllib.request, json
from webbrowser import get
from . import models
from .models import Quotes

base_url= 'http://quotes.stormconsultancy.co.uk/random.json'
def get_quotes():

    with urllib.request.urlopen(base_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quotes_results = None

        if get_quotes_response:          
    
            author = get_quotes_response.get('author')
            quote = get_quotes_response.get('quote')
            permalink = get_quotes_response.get('permalink')

            if quote:
              quotes_results = models.Quotes(author, quote, permalink)    
    
    return quotes_results
        


    



      



    
