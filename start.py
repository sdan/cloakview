import slack
from Manager import Manager
import Factory
import time


slack_token = ""
client = slack.WebClient(token=slack_token)

def slacked(msg,channel="status"):
	chnl = {"status": "CR42MCF1S",
			"error": "CRZB83HHB",
			"cancel": "CQT2T629Z",
			"main": "CR4DXKN3X"
			}
	client.chat_postMessage(
	  as_user = False,
	  channel=chnl[channel],
	  text=msg,
	  username = "bird",
	  icon_emoji = ":bird:"
	)

ping = Manager()
while True:
	try:
		ping.connect()
	except:
		slacked(":electric_plug: cloakview/start.py [ERROR] Connection issue with cloakview ","error")
		time.sleep(20)