
import streamlit as st
import requests

def app():
	st.write("<h style=' color: #0078ff; font-size:50px;'>Stock tweets</h>", unsafe_allow_html=True)

	symbol = st.text_input("Symbol")
	if symbol=="":
		r = requests.get("https://api.stocktwits.com/api/2/streams/trending.json")
	else:
		r = requests.get(f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json")

	data = r.json()

	try:
		for message in data['messages']:
			st.image(message['user']['avatar_url'])
			st.write(message['user']['username'])
			st.write(message['created_at'])
			st.write(message['body'])
	except:
		st.error("Invalid Ticker")
		
		




	