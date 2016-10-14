from twython import Twython, TwythonError
import sys

import import_twitter_keys as keys

t = Twython(app_key = keys.TWITTER_APP_KEY,
            app_secret = keys.TWITTER_APP_KEY_SECRET,
            oauth_token = keys.TWITTER_ACCESS_TOKEN,
            oauth_token_secret = keys.TWITTER_ACCESS_TOKEN_SECRET)


for count, tweet in enumerate(tweets):
    print('\n' + str(count+1))
    print(str(tweet['text']).encode(sys.stdout.encoding, errors='replace'))

def get_tweets(hashtag, num_of_tweets=1000, max_attempts=10):
    tweets_list = []
    for(i in range(0, max_attempts)):
        if(num_of_tweets < len(tweets_list)):
            return tweets_list
        if(i == 0):
            results = t.search(q='#pineapple', count=100)
        else:
            results = t.search(q='#pineapple', include_entities='true', max_id = next_max_id)
        for result in results['statuses']:
            tweet_text = result['text']
            tweets.append(tweet_text)
        try:
            next_results_url_params    = results['search_metadata']['next_results']
            next_max_id        = next_results_url_params.split('max_id=')[1].split('&')[0]
        except:
            return tweets_list


def main():
    num_of_tweets = 1000
    max_attempts = 10
    
    tweets_list = get_tweets("#pineapple", num_of_tweets=num_of_tweets)
