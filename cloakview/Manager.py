import os
import sys
import slack
import redis
from rq import Connection, Worker, Queue
import socket

import Factory

class Manager:
    slack_token = ""
    client = slack.WebClient(token=slack_token)
    
    def __init__(self):
        print("Connection initialized")
    
    def slacked(self,msg,channel="status"):
        chnl = {"status": "CR42MCF1S",
                "error": "CRZB83HHB",
                "cancel": "CQT2T629Z",
                "main": "CR4DXKN3X"
                }
        self.client.chat_postMessage(
          as_user = False,
          channel=chnl[channel],
          text=msg,
          username = "bird",
          icon_emoji = ":bird:"
        )

    def hola(self, *args):
        print("test hold")
        for arg in args:
            slacked(arg)


    def connect(self):
        listen = ['cloakview']
        redis_url = os.getenv('REDISTOGO_URL', '')

        conn = redis.from_url(redis_url)

        self.slacked(":gear: Starting [GENZMAFIA CLOAKVIEW] w/auth "+socket.gethostname())
        with Connection(conn):
            worker = Worker(list(map(Queue, listen)))
            worker.work()