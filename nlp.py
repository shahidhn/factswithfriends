import conda
#from conda import beautifulsoup4
import bs4
#import google
#from conda import google
#from google import search
from googlesearch.googlesearch import GoogleSearch


test1 = "Dude, Obama was born in Kenya"
test2 = "Africa is a country, right?"
test3 = "Hillary Clinton is involved in a sex ring in a pizza store"
test4 = "Tide pods are safe for human consumption"

trueone = "the kochs contribute 500,000 to ryan"



response = GoogleSearch().search(trueone + "fact", num_results = 3)
for result in response.results:
    print("Title: " + result.title)
    print(result.url)
    if "snopes.com" in result.url:
    	print("verifiable!")
    	if "claim false" in result.getMarkup():
    		print("Claim False!")
    	if "claim true" in result.getMarkup():
    		print("Claim True!")	
    #print("Content: " + result.getText())