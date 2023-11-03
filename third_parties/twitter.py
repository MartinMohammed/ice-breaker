import os
from datetime import datetime, timezone
import logging
import tweepy

# Retrieve environment variables or set fallback values
bearer_token = os.environ.get(
    "TWITTER_BEARER_TOKEN", "YOUR_FALLBACK_TWITTER_BEARER_TOKEN"
)
consumer_key = os.environ.get("TWITTER_API_KEY", "YOUR_FALLBACK_TWITTER_API_KEY")
consumer_secret = os.environ.get(
    "TWITTER_API_SECRET", "YOUR_FALLBACK_TWITTER_API_SECRET"
)
access_token = os.environ.get(
    "TWITTER_ACCESS_TOKEN", "YOUR_FALLBACK_TWITTER_ACCESS_TOKEN"
)
access_token_secret = os.environ.get(
    "TWITTER_ACCESS_SECRET", "YOUR_FALLBACK_TWITTER_ACCESS_SECRET"
)


# Setting up logging
logger = logging.getLogger("twitter")

# # Authenticating with Twitter API using environment variables
# auth = tweepy.OAuthHandler(
#     os.environ.get("TWITTER_API_KEY"), os.environ.get("TWITTER_API_SECRET")
# )
# auth.set_access_token(
#     os.environ.get("TWITTER_ACCESS_TOKEN"), os.environ.get("TWITTER_ACCESS_SECRET")
# )

# # This code by default tries to use the v1 version of the api.
# api = tweepy.API(auth)

# Use tweepy.client instead that uses api version 2.
twitter_client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)


def scrape_user_tweets(username, num_tweets=20):
    """
    Scrapes a Twitter user's original tweets (i.e., not retweets or replies) and returns them as a list of dictionaries.

    Parameters:
    - username (str): The Twitter username of the user whose tweets are to be scraped.
    - num_tweets (int): The number of tweets to scrape. Default is 20.

    Returns:
    - list: A list of dictionaries containing details of original tweets, each with fields:
            "time_posted" (relative to now),
            "text" (tweet text), and
            "url" (URL to the tweet).
    """

    # # Fetching tweets from the user's timeline
    # tweets = api.user_timeline(screen_name=username, count=num_tweets)

    # tweet_list = []

    # # Loop through the fetched tweets
    # for tweet in tweets:
    #     # Filtering out retweets and replies
    #     if "RT @" not in tweet.text and not tweet.text.startswith("@"):
    #         tweet_dict = {}
    #         # Calculating the time difference from the current time
    #         tweet_dict["time_posted"] = str(
    #             datetime.now(timezone.utc) - tweet.created_at
    #         )
    #         tweet_dict["text"] = tweet.text
    #         # Constructing the URL for each tweet
    #         tweet_dict[
    #             "url"
    #         ] = f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"
    #         tweet_list.append(tweet_dict)

    # Returns user object and we extract the id.
    user_id = twitter_client.get_user(username=username).data.id
    tweets = twitter_client.get_users_tweets(
        id=user_id, max_results=num_tweets, exclude=["retweets", "replies"]
    )
    tweet_list = []
    for tweet in tweets.data:
        tweet_dict = {}
        tweet_dict["text"] = tweet["text"]
        tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet.id}"
        tweet_list.append(tweet_dict)
    return tweet_list


if __name__ == "__main__":
    # No '@' symbol.
    print(scrape_user_tweets(username="hwchase17"))
