import tweepy_utils as twptils
import tweetId_functions as twtid
import os
import numpy as np
import pandas as pd
import tweepy as tw
from text_cell import text_my_cell,int_comma
from datetime import datetime, timedelta

# Script to extract tweets on 1 day for a set of regions
# This can be extended to more than 1 day. Message me on github if you are interested in that feature.

# path to locations.txt file
inputs = r'C:\Users\brian\Documents\Python Scripts\locations.txt' 
output_folder = r'E:\\my_tweets'
locations = twptils.extract_locations_from_txt(inputs)

accounts = twptils.accounts

total_tweet_count = 0

# Set delay in days (days = 6 means collect all the tweets from the date 6 days ago)
date = (datetime.now().date()-timedelta(days = 6)).strftime("%Y-%m-%d")

until_date = twtid.untilDateStr_from_datetimeStr(date) # we first generate the until dates we want w/ random sampling
since_id = twtid.sinceId_from_untilDate(until_date)
s = datetime.now()
pull_count = []
time_start = []
time_end = []

# Set specific keyword here. Default = filter retweets out
keyword = "-filter:retweets"
# keyword = ""

os.mkdir(output_folder+'//'+date)

logs = []
query_count=0 # used to keep track of total queries so swapping regions is efficient
region_counter = 1
for region,circles in locations.values:
    circle = circles[0]
    data = pd.DataFrame([])
    i = 0
    max_id = twtid.sinceId_from_untilDate((datetime.strptime(date,'%Y-%m-%d') + timedelta(days=2)).date().strftime("%Y-%m-%d")) # last ID from the first run of this program
    while max_id >= since_id:  #initial max = next days ID, then go until the last tweet pulled has a smaller tweet ID than the smallest ID possible
        twitter = twptils.init((query_count // 180) % len(accounts)) # use our accounts intelligently (only kind of), dont wait
        try:
            tweets = tw.Cursor(twitter.search, q=keyword,lang='en',tweet_mode='extended', count = 100, max_id=max_id-1,
                     result_type ='recent',until=until_date, geocode=circle).pages(1)
            temp_df = twptils.extract_tweets(list(next(tweets)), region)
            temp_df['query'] = i
        except StopIteration:
            print("No more tweets after ",temp_df.iloc[-1].tweet_date)
            break
        except: 
            pass
        if len(temp_df)<=1:
            data = data.append(temp_df)
            break
        pull_count.append(len(temp_df))
        time_start.append(temp_df.tweet_date.iloc[0])
        time_end.append(temp_df.tweet_date.iloc[-1])
        print(f"{i} | {len(temp_df)} | {str(temp_df.iloc[-1].tweet_date)} | Region: {region}: {region_counter}/{len(locations)}")
        
        max_id = temp_df.iloc[-1].tweet_id
        data = data.append(temp_df)
        i+=1
        query_count+=1
        
        
    # Filter out tweets 
    correct = data.loc[data['tweet_date'] >= datetime.strptime(date+' 00:00:00','%Y-%m-%d %H:%M:%S')]
    correct = correct.drop_duplicates('tweet_id')
    correct.to_csv(output_folder+'//'+date+'//all_'+region+'_'+date+'.csv.gz',index=False)
    
    print(f"Completion Time: {datetime.now()-s} | Queries Used: {i} | Number of tweets collected: {len(data)} | Region: {region}")
    print(f"Pulls per Query: {np.mean(pull_count)}")
    
    # log data
    total_tweet_count += len(data)
    logs.append([region,len(data)])
    region_counter += 1
    pull_count = []
    velocity = []
    time_start = []
    time_end = []
    
    del correct # free some space
    
runtime = datetime.now()-s
print(f'Total queries used: {query_count}')
print(f'Total tweets collected: {total_tweet_count}')
text_my_cell(f'Twitter collection finished collecting tweets from {date} with a total of {int_comma(total_tweet_count)} tweets collected\ntotal run time: {runtime}',0)
with open(output_folder+'//'+date+'//log.txt','w+') as f:
    f.write(f'total tweet count: {total_tweet_count}\ntotal run time: {runtime}\n\n')
    f.write('Region: number_of_tweets\n')
    for i in range(0,len(logs)):
        f.write(f'{logs[i][0]}: {logs[i][1]}\n')
        
