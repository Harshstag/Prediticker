
import tweepy
import config
import streamlit as st
import requests

def app():
	st.write("<h style=' color: #0078ff; font-size:50px;'>Stock tweets</h>", unsafe_allow_html=True)

	option = st.selectbox(" ",('Trending tweets', 'user tweets'))

	if option == 'Trending tweets':

		symbol = st.text_input("Symbol")
		if symbol=="":
			r = requests.get("https://api.stocktwits.com/api/2/streams/trending.json")
		else:
			r = requests.get(f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json")

		data = r.json()

		try:
			for message in data['messages']:
				st.image(message['user']['avatar_url'])
				st.markdown("#"+message['user']['username'])
				st.write(message['created_at'])
				st.write(message['body'])
				st.markdown("&nbsp")
		except:
			st.error("No tweets available!")

	if option == 'user tweets':
		auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
		auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)
		api = tweepy.API(auth)

		inputUsername = st.text_input("insert username")

		if inputUsername == "":
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

		else:
			user = api.get_user(inputUsername)
			tweets= api.user_timeline(inputUsername)
			st.header(inputUsername)
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



		
		
		




	