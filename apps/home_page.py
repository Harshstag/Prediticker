import streamlit as st
from .fetch_news import retrieve_business_news
import requests
import pandas as pd
from datetime import date
import yfinance as yf
from yahoo_fin import stock_info as si
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go
from .fetch_news import retrieve_news
from PIL import Image

import streamlit.components.v1 as components

def app():	
	title = Image.open('Images/title.png')
	st.image(title, caption=' ')


	##kpit1, kpit2 = st.beta_columns([1,6])
	##with kpit1:

		##image = Image.open('logo.png')
		##st.image(image, caption=' ', width=110)

	##with kpit2:
		##st.write("<h style=' font-size:60px;'>**PrediTicker**</h>", unsafe_allow_html=True)
		##st.write("<h style=' color: #0078ff; font-size:15px;'>**The Modern Stock Screener that helps you pick better stock**</h>", unsafe_allow_html=True)



	##st.write("<h style=' color: #0078ff; font-size:60px;'>PrediTickerr</h>", unsafe_allow_html=True)
	st.markdown("<hr/>", unsafe_allow_html=True)
	

	stock = yf.Ticker("^IXIC")
	#st.write(stock.info)
	def load_data(component):
		component_data=si.get_quote_data(component)
		return component_data

	NASDAQ_data = load_data("^IXIC")
	NIFTY50_data = load_data("^NSEI")
	BSESENSEX_data = load_data("^BSESN")
	
	


	
	

	#st.write(NASDAQ_data)

	def write_data(component):


		 

		

		shortname = (str(component['shortName']))
		marketstate = component['marketState']
		regularmarketprice = str(round(component['regularMarketPrice'],2))
		Changepercent = str(round(component['regularMarketChangePercent'],2))
		regularMarketChange = str(round(component['regularMarketChange'],2))

		low = Image.open('Images/low.png')
		##st.image(low, caption=' ',width = 100)

		help = Image.open('Images/help.png')
		


		if component['regularMarketChange'] > 0:




			

			st.markdown(f"<h style='text-align: center; font-size:20px; color: green; '>**{shortname}**</h>", unsafe_allow_html=True)
			st.markdown(f"<h style='text-align: center; font-size:40px; color: green; '>**{regularmarketprice}**</h>", unsafe_allow_html=True)
			st.markdown(f"<h style='text-align: center; font-size:20px; color: green; '>**{marketstate} : {regularMarketChange} / {Changepercent}%** </h>", unsafe_allow_html=True)	
			
				
		else:
			st.markdown(f"<h style='text-align: center; font-size:20px; color: red; '>**{shortname}**</h>", unsafe_allow_html=True)
			st.markdown(f"<h style='text-align: center; font-size:40px; color: red; '>**{regularmarketprice}**</h>", unsafe_allow_html=True)
			st.markdown(f"<h style='text-align: center; font-size:20px; color: red; '>**{marketstate} : {regularMarketChange} / {Changepercent}%**  </h>", unsafe_allow_html=True)  
			

	
	
	
	
	
	
	col1, col2, col3 = st.beta_columns(3)


	with col1: 
		write_data(NASDAQ_data)
	with col2:
		write_data(NIFTY50_data)
	with col3:
		write_data(BSESENSEX_data)

	

	st.markdown("<hr/>", unsafe_allow_html=True)




	image2 = Image.open('Images/homebg.png')
	st.image(image2, caption=' ')



	gainer_col, loser_col, active_col = st.beta_columns([1,1,1])
	st.markdown("<hr/>", unsafe_allow_html=True)
	
	gainers=si.get_day_gainers().head(10)
	with gainer_col:
		st.write("<h style=' color: green; font-size:40px;'>**Top Gainers**</h>", unsafe_allow_html=True)
		st.dataframe(gainers)


	losers=si.get_day_losers().head(10)
	with loser_col:
		st.write("<h style=' color: red; font-size:40px;'>**Top Losers**</h>", unsafe_allow_html=True)
		st.dataframe(losers)

	active=si.get_day_most_active().head(10)
	with active_col:
		st.write("<h style=' color: #ffd800; font-size:40px;'>**Top Active**</h>", unsafe_allow_html=True)
		st.dataframe(active)

	



	help = Image.open('Images/help.png')
	st.image(help, caption=' ')

	help2 = Image.open('Images/help2.png')
	st.image(help2, caption=' ')


	st.markdown("&nbsp ")
	st.write("<h style=' color: #0078ff; font-size:50px;'>Trending News</h>", unsafe_allow_html=True)
	st.markdown("<hr/>", unsafe_allow_html=True)
	retrieve_business_news()
	st.markdown("<hr/>", unsafe_allow_html=True)