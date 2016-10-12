print_values = True

try:
  import twitter_keys as keys
except:
  raise ValueError("Error importing twitterkeys.py. Does the file exist?")

values_present = True
try:
  TWITTER_APP_KEY = str(keys.TWITTER_APP_KEY)
  TWITTER_APP_KEY_SECRET = str(keys.TWITTER_APP_KEY_SECRET)
  TWITTER_ACCESS_TOKEN = str(keys.TWITTER_ACCESS_TOKEN)
  TWITTER_ACCESS_TOKEN_SECRET = str(keys.TWITTER_ACCESS_TOKEN_SECRET)
except:
  values_present = False

if(not TWITTER_APP_KEY
   or not TWITTER_APP_KEY_SECRET
   or not TWITTER_ACCESS_TOKEN
   or not TWITTER_ACCESS_TOKEN_SECRET):
  values_present = False

if(not values_present):
  raise ValueError("Your twitterkeys.py file must contain values for "\
                   "TWITTER_APP_KEY, "\
                   "TWITTER_APP_KEY_SECRET, "\
                   "TWITTER_ACCESS_TOKEN and "\
                   "TWITTER_ACCESS_TOKEN_SECRET.")

if(print_values):
  print(("TWITTER_APP_KEY = {0}\n"\
        "TWITTER_APP_KEY_SECRET = {1}\n"\
        "TWITTER_ACCESS_TOKEN = {2}\n"\
        "TWITTER_ACCESS_TOKEN_SECRET = {3}").format(TWITTER_APP_KEY,
        TWITTER_APP_KEY_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET))