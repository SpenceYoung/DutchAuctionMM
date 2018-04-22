#DAMM
##Dutch Auction Money Machine

##By Spencer Young
###April 21st 2018
####Decentralized Markets Hackathon

#####A Reverse Dutch Auction purchase signaler

http://www.yourdictionary.com/reverse-dutch-auction


##Summary

Built using the EOS dutch auction as example, can be adapted to work for any decentralized dutch auction with very little implementation/ability.

The design of the program is to poll the Dutch auction and the current market price while considering other historical data to signal whether it is economically sensible to contribute during the curent auction period.

The program's polling phase must accomplish two goals, poll the market price of asset and poll the current auction price of the asset. This is done with web scraping. Currently this is down with the coinmarketcap API and selenium but ideally would be done with several market APIs and querying a local Ethereum public node.

More analytics can be included, such as previous auction prices considerations when redesigned with an availalble ETH node.

The program can then decide to execute corresponding trades with a certainty of increasing the initial amount of prinicipal.

Inputs needed would be private keys, eth wallet balance, maximum risk, and intended smart contract in a fully implemented version



##Setting up

Required libraries are in requirements.txt.

After downloading required libs, you can receive basic signals and tweak the details to implement any trading strategy based on the signals.
