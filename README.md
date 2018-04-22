DAMM
Dutch Auction Money Machine

By Spencer Young
April 21st 2018

Reverse Dutch Auction purchase signaler

http://www.yourdictionary.com/reverse-dutch-auction




Abstract:

Built using the EOS dutch auction as example, can be adapted to work for any decentralized dutch auction

The concept of the program is to poll the Dutch auction and signal whether it is economically sensible to contribute during the auction period

The program's polling phase must accomplish two goals, poll the market price of asset and poll the current auction price of the asset

More analytics can be included, such as previous auction prices and  if running on a full node

The program can then decide to execute corresponding trades with a certainty of increasing the initial amount of prinicipal




Inputs needed would be private keys, eth wallet balance, and intended smart contract in a fully implemented version



program virtual environment can be initialized using: source contractPoller/bin/activate

required libraries are in requirements.txt
