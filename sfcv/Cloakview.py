import streamlit as st
import slack
import secrets
import os
from rq import Queue, Connection
from rq.job import Job
from redis import Redis
import time
import stripe



slack_token = ""
client = slack.WebClient(token=slack_token)

def slacked(msg,channel="status"):
	chnl = {"status": "CR42MCF1S",
	        "error": "CRZB83HHB",
	        "cancel": "CQT2T629Z",
	        "main": "CR4DXKN3X",
	        "tweet": "CS1RDGBE3",
	        "users": "CTZGDMRD0"
	        }
	client.chat_postMessage(
	  as_user = False,
	  channel=chnl[channel],
	  text=msg,
	  username = "bird",
	  icon_emoji = ":bird:"
	)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# st.write('<style>.colorgrad { background: rgba(0, 0, 0, 0) repeating-linear-gradient(-45deg, rgb(0, 84, 253) 0%, rgb(255, 25, 247) 7.14%, rgb(255, 46, 93) 14.28%, rgb(255, 170, 7) 21.42%, rgb(255, 170, 7) 28.56%, rgb(255, 46, 93) 35.7%, rgb(255, 25, 247) 42.84%, rgb(0, 84, 253) 50%) repeat scroll 0% 0% / 600vw 600vw padding-box text; background-color: rgba(0, 0, 0, 0); background-position-x: 0%; background-position-y: 0%; background-repeat: repeat; background-attachment: scroll; background-image: repeating-linear-gradient(-45deg, rgb(0, 84, 253) 0%, rgb(255, 25, 247) 7.14%, rgb(255, 46, 93) 14.28%, rgb(255, 170, 7) 21.42%, rgb(255, 170, 7) 28.56%, rgb(255, 46, 93) 35.7%, rgb(255, 25, 247) 42.84%, rgb(0, 84, 253) 50%); background-size: 600vw 600vw; background-origin: padding-box; background-clip: text; -webkit-background-clip: text; -webkit-animation: 90s linear 0s infinite normal forwards running followThrough; -moz-animation: 90s linear 0s infinite normal forwards running followThrough; animation: 90s linear 0s infinite normal forwards running followThrough; -webkit-text-fill-color: transparent; } @keyframes followThrough { 0%{background-position:0% 0%} 50%{background-position:50% 50%} 100%{background-position:0% 0%} } @-webkit-keyframes followThrough { 0%{background-position:0% 0%} 50%{background-position:50% 50%} 100%{background-position:0% 0%} } @-moz-keyframes followThrough { 0%{background-position:0% 0%} 50%{background-position:50% 50%} 100%{background-position:0% 0%} }</style>', unsafe_allow_html=True)
st.write('<link rel="stylesheet" type="text/css" href="https://sdan.cc/assets/css/colorgrad-slow.css">', unsafe_allow_html=True)
st.markdown('# <span class="colorgrad">Cloakview</span>: Mask your photos from AI recognition algorithms', unsafe_allow_html=True)
st.markdown("## Create immersive 3D Photos:", unsafe_allow_html=True)
### END OF REQUIRED

st.markdown("# Make your own:")

uploaded_file = st.file_uploader("Choose a JPG image", type=['jpg', 'jpeg'])

if uploaded_file is not None:
	status_bar = st.progress(0)
	experiment_id = secrets.token_hex(64)
	print("CV EXP ID: "+experiment_id)
	#st.write(experiment_id)
	# experiment_id = str(experiment_id)
	if not os.path.exists("/cdn/laycdn/cloakview/"+experiment_id):
		os.makedirs("/cdn/laycdn/cloakview/"+experiment_id)
		os.makedirs("/cdn/laycdn/cloakview/"+experiment_id+"/image")
	status_bar.progress(20)
	with open("/cdn/laycdn/cloakview/"+experiment_id+"/image/image_01.jpg", "wb") as outfile:
		status_bar.progress(70)
		outfile.write(uploaded_file.getbuffer())
		status_bar.progress(100)
	status_bar.empty()
	email = st.text_input('Enter email')
	slacked("SF CLOAK "+experiment_id+" "+email,"users")
	if st.button('Generate'):
		if email:
			status_bar = st.progress(0)
			slacked("SFLOW CLOAK "+experiment_id+" "+email,"status")
			qParallax = Queue('cloakview', connection=Redis.from_url(''))
			enJob = qParallax.enqueue('Factory.parallax_handler',["/cdn/laycdn/cloakview/"+experiment_id, experiment_id, email, "failed"], result_ttl=8640000, ttl=8640000, job_timeout=12000)
			print(enJob.id)
			status_bar.progress(20) 
			statusProgress = 20
			link1 = "https://cdn.sflow.io/cloakview/{}/image/image_01_cloaked.jpg".format(experiment_id)

			st.markdown('Your photos will be available here after finishing: <br><a href="{}">Cloakview Photo: </a><br>'.format(link1), unsafe_allow_html=True)
			st.info("After noting those links above, you can leave this page now, as in: you can close this page entirely (or wait until they're shown here itself). Those links will point towards your finished photo in a while.")

		else:
			st.warning("Enter your email")

		

			








