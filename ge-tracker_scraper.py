import requests
import urllib.request
import time
from bs4 import BeautifulSoup

#New line on top of document
print()

#All dictionaries of items and their URL's.
items = {
	"Warrior Ring": "https://www.ge-tracker.com/item/warrior-ring",
	"Mystic Mud Staff": "https://www.ge-tracker.com/item/mystic-mud-staff",
	"Death Rune": "https://www.ge-tracker.com/item/death-rune",
}

ancientPageSet = {
	"Ancient Page 1": "https://www.ge-tracker.com/item/ancient-page-1",
	"Ancient Page 2": "https://www.ge-tracker.com/item/ancient-page-2",
	"Ancient Page 3": "https://www.ge-tracker.com/item/ancient-page-3",
	"Ancient Page 4": "https://www.ge-tracker.com/item/ancient-page-4",
	"Set": "https://www.ge-tracker.com/item/book-of-darkness-page-set",
}


#Check individual items
def displayItems(urlDict):

	print("Checking items...")

	for title, url in urlDict.items():
		response = requests.get(url)
		
		#Make sure URL response is OK
		if response.status_code != requests.codes.ok:
			raise ValueError('Response code not 200, instead ' + response)

		else:
			#Get HTML contents of site
			soup = BeautifulSoup(response.text, "html.parser")

			#Set variables
			currentPrice = ''.join(soup.find(id="item_stat_overall").text.split())
			offerPrice = ''.join(soup.find(id="item_stat_offer_price").text.split())
			sellPrice = ''.join(soup.find(id="item_stat_sell_price").text.split())
			profit = ' '.join(soup.find(id="item_stat_approx_profit").text.split())

			#Print details
			print(title + ": ")
			print("\tCurrent price: " + currentPrice)
			print("\tOffer price: " + offerPrice)
			print("\tSell price: " + sellPrice)
			print("\tApproximate profit: " + profit)
	
	print("----------------------")



#Check sets
def displaySets(setDict):

	#Define variable for both individual and set price
	individualPrice = 0
	setPrice = 0

	print("Checking sets...")
	print("Individual items cost: ")

	for title, url in setDict.items():
		response = requests.get(url)
		
		#Make sure URL response is OK
		if response.status_code != requests.codes.ok:
			raise ValueError('Response code not 200, instead ' + response)

		else:
			#Get HTML contents of site
			soup = BeautifulSoup(response.text, "html.parser")

			#Set and format variables based on if item is set or individual
			if title != "Set":
				offerPrice = ''.join(soup.find(id="item_stat_offer_price").text.split())
				individualPrice += int(offerPrice.replace(",", ""))

				#Print details of individual items
				print("\t" + title + ": " + offerPrice)
			
			else:
				sellPrice = ''.join(soup.find(id="item_stat_sell_price").text.split())
				setPrice += int(sellPrice.replace(",", ""))

	#Print summary
	profit = setPrice - individualPrice
	print("\nTotal price for individual items: " + str(individualPrice))
	print("Total price for set: " + str(setPrice))
	print("Profit per set: " + str(profit) + " (" + str(round(100*profit/individualPrice, 2)) + "%)")
	print("----------------------")


#Running code
displayItems(items)
displaySets(ancientPageSet)