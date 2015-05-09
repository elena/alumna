import oauth2 as oauth
from django.conf import settings

def oauth_req(url, key, secret, http_method="GET", post_body=None, http_headers=None):
    consumer = oauth.Consumer(key=settings.SOCIAL_AUTH_TWITTER_KEY, secret=settings.SOCIAL_AUTH_TWITTER_SECRET)
    token = oauth.Token(key=key, secret=secret)
    client = oauth.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers)
    return content

    print oauth_req( 'https://api.twitter.com/1.1/users/lookup.json?screen_name=elequ', '', '')


import oauth2 as oauth
from django.conf import settings

# Create your consumer with the proper key/secret.
consumer = oauth.Consumer(key=settings.SOCIAL_AUTH_TWITTER_KEY, secret=settings.SOCIAL_AUTH_TWITTER_SECRET)


# Request token URL for Twitter.
request_token_url = "http://twitter.com/oauth/request_token"

# Create our client.
client = oauth.Client(consumer)

# The OAuth Client request works just like httplib2 for the most part.
resp, content = client.request(request_token_url, "GET")
print resp
print content
