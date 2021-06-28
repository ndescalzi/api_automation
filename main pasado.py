import unittest
import funciones



"""
#Api Nasa
#API KEY -> Required
#https://api.nasa.gov/planetary/apod?api_key=d3f8ZbiJGz1p8AXp3NhZRtlJXq1RRBmiHzST8Dc2

##### Covid
#############

url = "https://covid-19-data.p.rapidapi.com/country/all"

#Required
headers = {
    'x-rapidapi-key': "5aafbd6efbmsh384cffe4fd6bdb6p11f423jsn23152897beea",
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

#############

url = "https://covid-19-data.p.rapidapi.com/country"

querystring = {"name":"argentina"}
#Required
headers = {
'x-rapidapi-key': "5aafbd6efbmsh384cffe4fd6bdb6p11f423jsn23152897beea",
'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


##### Google translate
#############

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

payload = "q=Hello%2C%20world!&target=es&source=en"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-key': "5aafbd6efbmsh384cffe4fd6bdb6p11f423jsn23152897beea",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
#############

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/languages"

headers = {
    'accept-encoding': "application/gzip",
    'x-rapidapi-key': "5aafbd6efbmsh384cffe4fd6bdb6p11f423jsn23152897beea",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)


#Yahoo finanza
##############
#Hacer la comparacion con la actualizacion web

url = "https://yahoo-finance-low-latency.p.rapidapi.com/v11/finance/quoteSummary/AAPL"

querystring = {"modules":"defaultKeyStatistics,assetProfile"}

headers = {
    'x-rapidapi-key': "5aafbd6efbmsh384cffe4fd6bdb6p11f423jsn23152897beea",
    'x-rapidapi-host': "yahoo-finance-low-latency.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

################


url = "https://yahoo-finance-low-latency.p.rapidapi.com/v6/finance/quote"

#Los simbolos a buscar
querystring = {"symbols":"AAPL,BTC-USD,EURUSD=X"}

headers = {
    'x-rapidapi-key': "5aafbd6efbmsh384cffe4fd6bdb6p11f423jsn23152897beea",
    'x-rapidapi-host': "yahoo-finance-low-latency.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
"""