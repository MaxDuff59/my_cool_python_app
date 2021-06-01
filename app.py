import os
import re
import streamlit as st
import logging
import requests
from pytrends.request import TrendReq
from datetime import datetime


pytrends = TrendReq(hl='en-US', tz=360)
a = pytrends.get_historical_interest(['football','formula 1'], year_start=2018, month_start=1, day_start=1, hour_start=0, year_end=2018, month_end=2, day_end=1, hour_end=0, cat=0, geo='', gprop='', sleep=0)

somme_foot = 0
somme_f1 = 0

for i in range(len(a)):
	somme_foot += a['football'][i]
	somme_f1 += a['formula 1'][i]

st.text(somme_foot)
st.text(somme_f1)

st.line_chart(a[['football','formula 1']])
	
code = """<!-- Global site tag (gtag.js) - Google Analytics -->
<script async
src="https://www.googletagmanager.com/gtag/js?id=G-9GS61NDRDZ"></script>
<script>
	window.dataLayer = window.dataLayer || [];
	function gtag(){dataLayer.push(arguments);}
	gtag('js', new Date());
	gtag('config','G-9GS61NDRDZ');
</script>"""

a=os.path.dirname(st.__file__) + '/static/index.html'
with open(a,'r') as f:
	data=f.read()
	if len(re.findall('G-',data)) == 0:
		with open(a,'w') as f:
			newdata=re.sub('<head>','<head>' + code, data)
			f.write(newdata)
st.title("Hi everybody")
title = st.text_input('Movie title','Life of Brian')
st.write('The current movie title is',title)
st.write(a)

if st.button('Google requests'):
	req = requests.get("https://www.google.com/")
	st.write('Google test : ',req)
else:
	st.write('No requests')

st.markdown(req.cookies._cookies)

req2 = requests.get('https://analytics.google.com/analytics/web/?utm_source=marketingplatform.google.com&utm_medium=et&utm_campaign=marketingplatform.google.com%2Fabout%2Fanalytics%2F#/p272833877/reports/defaulthome')
st.write('Google Analytics requests : ',req2.content)

st.text(req2.status_code)
st.markdown(req2.text)
st.text('a : ',a)

logging.warning('Watch out !')
logging.info('I told you so')
