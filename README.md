# freefolio

Simple python script to track your cryptocurrency funds. Based on a configuration file (by default in `$ HOME/.config/freefolio/config`) and the CoinGecko API, it calculates the total investment value.

Given a threshold and a `principal` coin (by default respectively 80% and bitcoin), the script warns if the value in `curr` (fiat chosen by the user, by default EUR) of the main coin is below the threshold.


