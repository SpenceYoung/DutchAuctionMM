"""
DAMM
Dutch Auction Money Machine

By Spencer Young
April 21st 2018

Dutch Auction purchase signaler

built using the EOS dutch auction as example, can be adapted to work for any decentralized reverse dutch auction

The concept of the program is to poll the Dutch auction and signal whether it is economically sensible to contribute during the auction period

The program's polling phase must accomplish two goals, poll the market price of asset and poll the current auction price of the asset

The program can then decide to execute corresponding trades with a certainty of increasing the initial amount of prinicipal

Inputs needed would be private keys, eth wallet balance, and intended smart contract

"""

from coinmarketcap import Market
coinmarketcap = Market()
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
timeRemaining = 0
ethContr = 0


def getMarketPrice():
	try:
		return coinmarketcap.ticker("EOS")[0]['price_usd']
	except:
		print("Error getting market price")


def getEOScontractInfo(again = False):
	#if i had a full eth node, i would query it locally with RPC calls rather than 
	try:
		
		driver = webdriver.Firefox()
		driver.get("https://eosscan.io")
		time.sleep(10)
		ethContributed = driver.find_element_by_class_name("main-contributed-eth").text
		ethContr = ethContributed
		usdtPrice = driver.find_element_by_class_name("main-current-price-by-usdt").text
		timeRemaining = driver.find_elements_by_class_name("text-info")[1].text
		return [usdtPrice,timeRemaining]
	except Exception as e:
		print("error getting usdt price... " + str(e))
		if(again == True):
			print("second failure, exitting now")
			driver.quit()
			exit()
		else:
			print("trying again")
			return getEOScontractInfo(again = True)


def getOtherPeriodInfo():
	#if I had a full node, I would query it to get statistics on other periods here
	return 0

def executeDutchAuction(amount = 0):
	#
	#if(amount!=0):
		#send 0xd0a6E6C54DbC68Db5db3A091B171A77407Ff7ccf the amount
	#else:
		#send 0xd0a6E6C54DbC68Db5db3A091B171A77407Ff7ccf the ethbalance/periods remaining
	return 0

def main():
	print("\nWelcome to Dutch Auction money machine")
	print("\nThe current coinmarketcap EOS price is: ")
	marketprice = getMarketPrice()
	print("$" + str(marketprice))
	print("\nThe current EOS contract price is: ")
	infoList = getEOScontractInfo()
	contractPrice = infoList[0]
	print(str(contractPrice))
	timeRemaining = infoList[1]
	timeRemaining = timeRemaining[32:49]
	
	splitStr = timeRemaining.split(" ")
#	print(splitStr)
	splitminStr = splitStr[2].split(":")
#	print(splitminStr)

	timeNow = datetime.datetime.utcnow()
	timeDone = datetime.datetime(year = int(splitStr[1]),
		month = timeNow.month, day = int(splitStr[0]),hour = int(splitminStr[0]),minute = int(splitminStr[1]))
	
	#print(timeNow)
	print("Time remaining in auction period: " + str(timeDone - timeNow))
	
	timeTemp = timeDone-timeNow
	timeLeft = timeTemp #.timedelta #hours * 60 + timeTemp.minutes #time left in minutes
	#print("\nTime left (minutes): " + timeLeft)

	profitMargin = float(marketprice)/(float(contractPrice[1:]))
	profitMargin = str(round(profitMargin*100,3))
	print("\nProfit margin currently is : " + profitMargin + "%")


	#here is where you would compare historical data 
	#
	#call getOtherPeriodInfo()
	
	#after comparing your data, use it to make a decision,
	#or adjust for the risk of the bad GameTheory outcome
	if(profitMargin > 3 and timeRemaining < 5):
		print("Ok, execute a contribution")
		#call executeDutchAuction
		float(input("Enter how much you'd like to contribute, or nothing for balance/periods left: "))
	else:
		print("Looks too risky, maybe next time.")
	exit()
main()
