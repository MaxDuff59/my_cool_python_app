import os
import re
import streamlit as st
import logging

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

logging.warning('Watch out !')
logging.info('I told you so')
