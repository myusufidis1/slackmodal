#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, os

from flask import Flask, request, Response
from slack import WebClient

app = Flask(__name__, template_folder='')

# Set the token from the secret environment variables.
client = WebClient(token=os.environ.get('TOKEN'))

@app.route('/', methods=['GET'])
def main():
  return Response("To get started, remix this project and check out the README file!")

# Step 4: The path that allows for your server to receive information from the modal sent in Slack
@app.route('/interactive', methods=['POST'])
def interactive():
    payload = json.loads(request.form["payload"])
    # Extra Credit: Uncomment out this section
    # thank_you_channel = "your_channel_id"
    # user_text = payload["view"]["state"]["values"]["my_block"]["my_action"]["value"]
    # client.chat_postMessage(channel=thank_you_channel, text=user_text)
    return Response()
  
# Step 5: Payload is sent to this endpoint, we extract the `trigger_id` and call views.open
@app.route('/slashcommand', methods=['GET', 'POST'])
def slashcommand():
    with open("modal.txt") as modalfile:
        client.views_open(trigger_id=request.form["trigger_id"], view=json.load(modalfile))
    return Response()

if __name__ == '__main__':
    app.run()