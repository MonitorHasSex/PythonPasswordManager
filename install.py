import os
import requests

r =requests.get('https://pastebin.com/raw/6rpaMNEM')
file = open('PPM.py', 'w')
file.write(r)
file.close()