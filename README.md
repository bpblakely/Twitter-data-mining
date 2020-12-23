# Twitter-data-mining
Short scripts to efficiently scrap tweets off Twitter using Tweepy

# Main Feature: Intelligent Account Weaving
Collect data from Twitter's Search API using multiple accounts

Each account has a maximum of 180 queries per 15 minutes, where each query can have 100 tweets (18,000 tweets per 15 minutes per account)

With account weaving you can start pulling tweets from a different account the moment you run out of queries with a different account

Around 7-8 accounts are needed to achieve 100% uptime on tweet collection

# Regional Automated Tweet Collection
Using the free Search API (version 1.1) and Tweepy, automatically gather tweets using account weaving and cycle through different regions

