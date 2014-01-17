import tweepy

def buscarTweets(tema):
    CONSUMER_KEY = 'UYdOZdbPnBraThMG4cXW6A'
    CONSUMER_SECRET = 'WlvJCerj3KI323zEX8XQhcg0IzF0j5DWORzZmUeMPM'
    ACCESS_KEY = '221535588-Jagmw9aLUWveCkjHhG5IhW9izVQMclfEfsF0ZcZO'
    ACCESS_SECRET = 'V6zktyKmd1KUUw1NHj0tofoLtzqrUMT6JC9gxRk7qXzZr'


    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    i=0
    j=0
    tweets = []
    for status in tweepy.Cursor(api.search,  include_entities=True, q=tema).items(800): 
        for url in status.entities['urls']:
             tweets.append(status.text)
             tweets.append(url['expanded_url'])
             print url['expanded_url']
             i+=1
        if (i>6):
            break

    return tweets
