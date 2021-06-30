import streamlit as st
import tweepy
import config


def app():
	auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
	auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)


	for username in config.TWITTER_USERNAMES:

		user = api.get_user(username)
		tweets= api.user_timeline(username)
		st.header(username)
		st.image(user.profile_image_url)
		for tweet in tweets:
			if '$' in tweet.text:
				words = tweet.text.split(' ')
				for word in words:
					if word.startswith('$') and word[1:].isalpha():
						symbol = word[1:]
						st.write(symbol)
						st.write(tweet.text)
						st.image(f"https://finviz.com/chart.ashx?t={symbol}")