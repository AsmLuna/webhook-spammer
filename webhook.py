#!/usr/bin/env python3

import requests
import time
from discord import Webhook, RequestsWebhookAdapter

url = input("Webhook url: ")
message = input("Message: ")
timeout = float(input("Timeout (in seconds): "))

while True:
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())
    time.sleep(timeout)
    webhook.send(message)
