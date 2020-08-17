import os
import slack
import sys
import requests
sys.path.append('../')

slack_token = ""
client = slack.WebClient(token=slack_token)


def hola(*args):
    print("test rogue")
    for arg in args:
        slacked(arg)

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



def cloakview_handler(payload):
    #["/cdn/laycdn/videos/"+experiment_i, experiment_id, email, payment]

    pathway = payload[0]
    experiment_id = payload[1]
    email = payload[2]
    mode = payload[3]
    print("in CLOAK handler"+pathway+" "+email)
    cmd = "python /fawkes/protection.py --mode {} --gpu 0  --directory /cdn/laycdn/cloakview/{}/image".format(mode,experiment_id)
    os.system(cmd)
    return experiment_id



# def cloakview_twitter_handler(payload):






