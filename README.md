# Twitter-data-mining
Short scripts to efficiently scrap tweets off Twitter using Tweepy. This repository includes code for automated data collection of tweets, logging of data collection, and automated updates on data collection via text messages

# Intelligent Account Weaving
Collect data from Twitter's Search API using multiple accounts

Each account has a maximum of 180 queries per 15 minutes, where each query can have 100 tweets (18,000 tweets per 15 minutes per account)

With account weaving you can start pulling tweets from a different account the moment you run out of queries with a different account

Around 7-8 accounts are needed to achieve 100% uptime on tweet collection

# Regional Automated Tweet Collection
Using the free Search API (version 1.1) and Tweepy to automatically gather tweets using account weaving and cycle through different regions

# File Breakdrown
* tweepy_utils.py
  
  * Functions to account weave Twitter API accounts and extract relevant data from tweets
  * Function to read regional coordinates data for regional tweet collection
  
* tweetId_functions.py

  * Numerous functions to manipulate tweet ID's and create synthetic tweet ID's based on time
  
    * This can be abused to constrain tweet collection time intervals down to millisecond ranges
    * Paper in the works which abuses this to create an efficient sampling algorithm based on tweet density

* locations.txt

  * Coordinates and radius for the circle used in the Search API to specify a region
  
  * Format:
    * Region Name
    * Coordinates (NO SPACES BETWEEN COMMAS!)
    * Blank line
    
* daily_twitter_script.py

  * An example of how to collect tweets daily from a set of regions 
  
  * This example can be extended to cover many different use cases, but message me if you need help

* text_cell.py

  * Script using [Twilio](https://www.twilio.com/docs/libraries/python) to text you updates about the data collection script
  
  * Useful to catch odd bugs in Twitter API which might result in the script failing or getting stuck (rare)
