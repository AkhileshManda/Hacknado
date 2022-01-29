import tweepy
from tweepy import Client
import pandas as pd


#Installation / Access to Twitter account
consumer_key = 'JPPxbx7JO5kjtSvf42nTrIpQd' #api key
consumer_secret = 'gUlhcQ5GZfw2AJx3mNfESatyT5z8vF1ufm6RUC4McR2Zk5GqJJ' #api key secret
bearer_token = "AAAAAAAAAAAAAAAAAAAAADzJTgEAAAAA5KGUizcxvi0CzaKGivZbuz4HsWY%3DCvXWJPmZz6C1txZlCEyOqe7PZX5o7FUBeuNCS5fNW9NXdmGic2"
access_token = '773944734070996992-iFUMZYrV1WO9oNuKpyO9ItirotdKoIg'
access_token_secret = '7m6rXWgqexVRVJwYdp78ix3IomrxmHPP5NLMUGYHwr1Gb'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit = True)

client = Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret, wait_on_rate_limit=True)

def profile_image(filename):
    api.update_profile_image(filename)

def update_profile_info(name, url, location, description):
    api.update_profile(name, url, location, description)

def post_tweet(text):
    api.update_status(text)

def upload_media(text, filename):
    media = api.media_upload(filename)
    api.update_status(text, media_ids = [media.media_id_string])

def favorite(tweet_id):
    api.create_favorite(str(tweet_id))

def retweet(tweet_id):
    api.retweet(str(tweet_id))

def unfavorite(tweet_id):
    api.destroy_favorite(str(tweet_id))

def unretweet(tweet_id):
    api.unretweet(str(tweet_id))

def reply(tweet_id, message):
    tweet = api.get_status(str(tweet_id))
    username = tweet.user.screen_name
    reply = api.update_status(f'@{username} ' + message, str(tweet_id))

#Scrape uesr timeline
    
def user_timeline(username):
    keyword_tweets = []
    for tweet in tweepy.Cursor(api.user_timeline, screen_name = username,
                               tweet_mode = 'extended').items(150):
        keyword_tweets.append(tweet.full_text)
    return keyword_tweets
            
    '''
        if tweet.full_text.startswith('@'):
            replies.append(tweet.full_text)
        elif tweet.full_text.startswith('RT @'):
            rts.append(tweet.full_text)
        else:
            ot.append(tweet.full_text)
    print(len(ot))
    print(len(replies))
    print(len(rts))
    return ot, replies, rts
    '''
#keyword_tweets = user_timeline('elonmusk')
def search_tweets(keyword):
    for tweet in tweepy.Cursor(api.search, q = keyword,
                               tweet_mode = 'extended').items(10):
        if tweet.full_text.startswith('RT @'):
            text = tweet.retweeted_status.full_text
            print(len(text))
            print(text)
        else:
            print(len(tweet.full_text))
            print(tweet.full_text)

def scrape_user_followers(username, max_length=None):
    followers_scraped = []
    for i, _id in enumerate(tweepy.Cursor(api.get_followers,
                                          screen_name = username).items()):
        followers_scraped.append(_id.id)

        if max_length is not None:
            if len(followers_scraped) >= max_length:
                break

    return followers_scraped


def scrape_user_friends(username):
    friends_scraped = []
    for i, _id in enumerate(tweepy.Cursor(api.get_friend_ids,
                                          screen_name = username).items()):
        friends_scraped.append(_id)
    return friends_scraped

def follow(screen_name):
    api.create_friendship(screen_name)

def unfollow(screen_name):
    api.destroy_friendship(screen_name)

'''
friends = scrape_user_friends('k_ristovski')
for i in range(len(friends)):
    screen_name = api.get_user(friends[i]).screen_name
    print(i, screen_name)
'''
def user_data(screen_name): #Screen_name and Twitter-profile ID
    user = client.get_user(id=screen_name)
    return user

def get_users_v2(usernames):

    if len(usernames) > 100:
        raise Exception("length of given list > 100")

    usernames = list(map(str, usernames))

    data = client.get_users(ids=','.join(usernames), user_fields="description", user_auth=True) 
    return data.data

def send_message(screen_name, text):
    profile_id = api.get_user(screen_name).id
    api.send_direct_message(str(profile_id), text = text)

def extract_messages(count):
    messages = []
    all_data = api.list_direct_messages(count = count)
    for i in range(len(all_data)):
        text = all_data[i]._json['message_create']['message_data']['text']
        messages.append(text)
    return messages        



def extract_trends(woeid, threshold):
    all_trends = api.trends_place(id = woeid)
    dataframe = pd.DataFrame(columns = ['Trend', 'Volume'], index = None)
    for i in range(len(all_trends[0]['trends'])):
        trend = all_trends[0]['trends'][i]['name']
        volume = all_trends[0]['trends'][i]['tweet_volume']
        try:
            if volume > threshold:
                new_row = {'Trend' : trend, 'Volume' : volume}
                dataframe = dataframe.append(new_row, ignore_index = True)
            else:
                pass
        except:
            pass
    dataframe = dataframe.set_index('Trend')
    dataframe = dataframe.sort_values(by = 'Volume', ascending = False)
    return dataframe