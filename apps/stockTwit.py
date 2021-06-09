
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
	i = 0;
	col = [];
	try:
		for message in data['messages']:
			col[i], col[i+1] = st.beta_columns[(1,3)]
			with col[i]:
				st.image(message['user']['avatar_url'])
			with col[i+1]:
				st.write(message['user']['username'])
			st.write(message['created_at'])
			st.write(message['body'])
			i = i +1
			st.markdown("&nbsp")
	except:
		st.error("Invalid Ticker")
		
		




	