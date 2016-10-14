from twython import Twython, TwythonError
import sys

import import_twitter_keys as keys

t = Twython(app_key = keys.TWITTER_APP_KEY,
            app_secret = keys.TWITTER_APP_KEY_SECRET,
            oauth_token = keys.TWITTER_ACCESS_TOKEN,
            oauth_token_secret = keys.TWITTER_ACCESS_TOKEN_SECRET)

##### from http://stackoverflow.com/a/21644346/5127934 #####

tweets                          =   []
MAX_ATTEMPTS                    =   10
COUNT_OF_TWEETS_TO_BE_FETCHED   =   500 

for i in range(0,MAX_ATTEMPTS):

    if(COUNT_OF_TWEETS_TO_BE_FETCHED < len(tweets)):
        break # we got 500 tweets... !!

    #----------------------------------------------------------------#
    # STEP 1: Query Twitter
    # STEP 2: Save the returned tweets
    # STEP 3: Get the next max_id
    #----------------------------------------------------------------#

    # STEP 1: Query Twitter
    if(0 == i):
        # Query twitter for data. 
        results    = t.search(q="foobar",count='100')
    else:
        # After the first call we should have max_id from result of previous call. Pass it in query.
        results    = t.search(q="foobar",include_entities='true',max_id=next_max_id)

    # STEP 2: Save the returned tweets
    for result in results['statuses']:
        tweet_text = result['text']
        tweets.append(tweet_text)


    # STEP 3: Get the next max_id
    try:
        # Parse the data returned to get max_id to be passed in consequent call.
        next_results_url_params    = results['search_metadata']['next_results']
        next_max_id        = next_results_url_params.split('max_id=')[1].split('&')[0]
    except:
        # No more next pages
        break

############################################################

print(str(tweets).encode(sys.stdout.encoding, errors='replace'))