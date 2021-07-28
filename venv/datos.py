"""
Información relevante para el llamado de las API, y la comparacion de la estructura de la misma.
"""

informacion = {
    "nasa": {
        "url": "https://api.nasa.gov/planetary/apod?api_key=d3f8ZbiJGz1p8AXp3NhZRtlJXq1RRBmiHzST8Dc2",
        "params": {},
        "headers": {},
        "llaves": ('copyright', 'date', 'explanation', 'hdurl', 'media_type', 'service_version', 'title', 'url')
    },
    "covid":{
        "url": "https://covid-19-data.p.rapidapi.com/country",
        "params": {'name': 'argentina'},
        "headers": {'x-rapidapi-key': '5aafbd6efbmsh384cffe4fd6bdb6p11f423jsn23152897beea','x-rapidapi-host': 'covid-19-data.p.rapidapi.com'},
        "funcion": "requests.get(url, headers=headers, params=params)",
        "llaves": ('country', 'code', 'confirmed', 'recovered', 'critical', 'deaths', 'latitude', 'longitude', 'lastChange', 'lastUpdate')
        },
    "finanzas":{
        "url": "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-quotes",
        "params": {"region":"US","symbols":"AMZN"},
        "headers": {
            'x-rapidapi-key': "5aafbd6efbmsh384cffe4fd6bdb6p11f423jsn23152897beea",
            'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"},
        "funcion": "requests.get(url, headers=headers, params=params)",
        "llaves": ('quoteResponse')
    },
}