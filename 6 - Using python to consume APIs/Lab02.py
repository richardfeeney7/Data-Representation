# Import required packages.
import requests # to send http requests
import json     # to handle json

# Open our file from week02
f = open("../2 - Functionality on the webpage/week3.html", "r")
html = f.read()

# Part 1. print out the file
print(html)

# Part 2. Use html2pdf.app with an api key
apiKey = '46ceed910c24ff7cce8240e89ec7b71912f6f40f2ec55fd217ce150ad6d4f1c4'
url = 'https://api.html2pdf.app/v1/generate'

data = {'html': html, 'apiKey': apiKey}

response = requests.post(url, json=data)
print(response.status_code) # should get 200

# Part 3. Write returned data to a pdf file
newfile = open("lab06_02_htmlaspdf.pdf", "wb")
newfile.write(response.content)