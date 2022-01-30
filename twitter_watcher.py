from twitter_api import search as twitter_search
import pandas as pd
from NLP import NLP
from difflib import SequenceMatcher
import time

# csv columns: event_id, event_type, event_location, event_status, recent_tweets, relevent_hashtags, is_active

class Twitter_Watcher:
    def __init__(self, csv_path, sleep_time=60, default_hashtag="#TwitterDisasterWatcher"):
        self.csv_path = csv_path
        self.df = pd.read_csv(csv_path)
        self.sleep_time = sleep_time
        self.default_hashtag = default_hashtag
        self.nlp = NLP(
            "./models/tf_bert/model_weights_9.h5",
            "./models/spacy_ner_cpu/model-best"
        )
    
    def run(self, bert_thres=0.5):
        rows = self.df[self.df["is_active"] == "yes"]

        for row in rows:
            row_dict = row.to_dict()
            hashtag_list = row["relevent_hashtags"].split("|")

            query = " OR ".join(hashtag_list)
            query = f"({query})"

            tweets = twitter_search(query)

            temp_list = [tweet.text for tweet in tweets if tweet.lang == "en"]
            bert_results = self.nlp.process_bert(temp_list)

            relevent_tweets = []
            for i, item in enumerate(bert_results):
                prob = item[0][0]
                if prob > bert_thres:
                    relevent_tweets.append(tweets[i])
                
            tweet_ids = []
            tweet_texts = [tweet.text for tweet in relevent_tweets]

            spacy_results = self.nlp.process_spacy(tweet_texts)
            for i, item in spacy_results:
                for word in item.ents:
                    if word.label_ == "STATUS":
                        row_dict["event_status"] += f"|{word.text}"
                        tweet_ids.append(relevent_tweets[i].id)

            row_dict["recent_tweets"] = "|".join(tweet_ids)

            self.df.loc[row.name] = row_dict

            

    def run_default_search(self):
        active_events = self.df[self.df["is_active"] == "yes"]

        tweets = twitter_search(self.default_hashtag)
        temp_list = [tweet.text for tweet in tweets if tweet.lang == "en"]

        bert_results = self.nlp.process_bert(temp_list)

        relevent_tweets = []
        for i, item in enumerate(bert_results):
            prob = item[0][0]
            if prob > 0.5:
                relevent_tweets.append(tweets[i])

        

    def refrest_database(self):
        self.df=pd.read_csv(self.csv_path) 

def get_hashtags(tweet):
    return [hashtag.tag for hashtag in tweet["entities"]["hashtags"]]

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

if __name__ == "__main__":
    print(twitter_search("#covid19"))
