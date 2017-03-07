import sys
import csv

from string import punctuation
from twitter_scanner import getTweets


files=['positive.txt','negative.txt','test_tweets.txt']

hashtag = sys.argv[1]

if(getTweets(hashtag)):

	tweets = open(files[2]).read()
	tweets_list = tweets.split('\n')

	pos_sent = open(files[0]).read()
	positive_words=pos_sent.split('\n')
	positive_counts=[]

	neg_sent = open(files[1]).read()
	negative_words=neg_sent.split('\n')
	negative_counts=[]


	for tweet in tweets_list:
	    positive_counter=0
	    negative_counter=0
	    
	    tweet_processed=tweet.lower()
	    
	    
	    for p in list(punctuation):
	        tweet_processed=tweet_processed.replace(p,'')

	    words=tweet_processed.split(' ')
	    word_count=len(words)
	    for word in words:
	        if word in positive_words:
	            positive_counter=positive_counter+1
	        elif word in negative_words:
	            negative_counter=negative_counter+1


	    pos = positive_counter/word_count
	    neg = negative_counter/word_count

	    positive_counts.append(round(pos + 0.005, 2))
	    negative_counts.append(round(neg + 0.005, 2))

	print ('\ntweets processed: '+str(len(positive_counts)))

	output=zip(tweets_list,positive_counts,negative_counts)

	writer = csv.writer(open('tweet_sentiment.csv', 'wb'))
	writer.writerows(output)