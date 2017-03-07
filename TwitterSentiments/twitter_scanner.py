from TwitterSearch import *

def getTweets(hashtag):

	try:
	    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
	    tso.set_keywords(['#'+hashtag]) # let's define all words we would like to have a look for
	    tso.set_language('en') # we want to see English tweets only
	    tso.set_include_entities(False) # and don't give us all those entity information

	    # it's about time to create a TwitterSearch object with our secret tokens
	    ts = TwitterSearch(
	        consumer_key = 'JJf1zaFm62QWDI9Kh55v8MMV7',
	        consumer_secret = '376WqS1KISggbRuiKHTPIZknFImiqjCNmJi8W2Myj7OfSpLS0B',
	        access_token = '2172451140-4D6obJISbYBvQM0mxa9kaEYY1xMh3flIJVQ3Jmn',
	        access_token_secret = 'FbJKBWwO48z5KWBztipDrvlc4l3glXTZKKd5l8hSn6D5M'
	     )

	     # this is where the fun actually starts :)
	    with open('test_tweets.txt','w') as file:

		    for tweet in ts.search_tweets_iterable(tso):
		    	twt = tweet['text'].replace('\n','')+'\n'
		        file.write(twt.encode('cp850', errors='replace'))

	    return True 

	except TwitterSearchException as e: # take care of all those ugly errors if there are some
	    print(e)

# getTweets('againstjntuhevaluation')