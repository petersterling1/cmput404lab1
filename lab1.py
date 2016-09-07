import requests

response = requests.get('https://github.com/petersterling1/cmput404lab1/raw/master/lab1.py')
print response.text
