#!/usr/bin/env python3

import os
import json

# print all vars as plain text
print("Content-Type: text/html")  # let browser know its plain text
print()
print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")

# print env variables as json
