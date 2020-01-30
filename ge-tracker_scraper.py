import requests
import urllib.request
import time
from bs4 import BeautifulSoup

#New line on top of document
print()

#All dictionaries of items and their URL's.
from items import *
from sets import *

#Check individual items
def displayItems(urlDict):

	print("Checking items...")

	for title, url in urlDict.items():
		response = requests.get(url)
		
		#Make sure URL response is OK
		if response.status_code != requests.codes.ok:
			raise ValueError('Response code not 200, instead ' + str(response))

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
			raise ValueError('Response code not 200, instead ' + str(response))

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
	print()


# Pause for x amount of seconds to avoid timeout
def timeout(time):
	print("\n\tProgram idle for " + str(time) + " seconds to avoid timeout", flush=True)
	time.sleep(time)



#Running code
while True:

	print("What would you like to look up?")
	userinput = input()
	print()

	if "arma" in userinput:
		displaySets(armadylPageSet)
	elif "sara" in userinput:
		displaySets(saradominPageSet)
	elif "bandos" in userinput:
		displaySets(bandosPageSet)
	elif "ancient" in userinput:
		displaySets(ancientPageSet)
	elif "zam" in userinput:
		displaySets(zamorakPageSet)
	elif "guthix" in userinput:
		displaySets(guthixPageSet)
	elif "item" in userinput:
		displayItems(items)
	elif "all" in userinput:
		displayItems(items)
		timeout(10)
		displaySets(armadylPageSet)
		timeout(10)
		displaySets(saradominPageSet)
		timeout(10)
		displaySets(bandosPageSet)
		timeout(10)
		displaySets(ancientPageSet)
		timeout(10)
		displaySets(zamorakPageSet)
		timeout(10)
		displaySets(guthixPageSet)
	elif "exit" in userinput:
		exit()

