

informacion = {
    "nasa": {
        "url": "https://api.nasa.gov/planetary/apod?api_key=d3f8ZbiJGz1p8AXp3NhZRtlJXq1RRBmiHzST8Dc2",
        "llaves": ('copyright', 'date', 'explanation', 'hdurl', 'media_type', 'service_version', 'title', 'url')
    },
    "covid":{
        "url": "https://covid-19-data.p.rapidapi.com/country",
        "country": "querystring = {'name': 'argentina'}",
        "headers": "{'x-rapidapi-key': '5aafbd6efbmsh384cffe4fd6bdb6p11f423jsn23152897beea','x-rapidapi-host': 'covid-19-data.p.rapidapi.com'}",
        "funcion": "requests.request('GET', url, headers=headers, params=querystring)"
        },
    "finanzas":{
        "url": "https://yahoo-finance-low-latency.p.rapidapi.com/v6/finance/quote",
        "querystring": {"symbols": "AAPL"},
        "headers": "{'x-rapidapi-key': '5aafbd6efbmsh384cffe4fd6bdb6p11f423jsn23152897beea',    'x-rapidapi-host': 'yahoo-finance-low-latency.p.rapidapi.com'}",
        "funcion": "requests.request('GET', url, headers=headers, params=querystring)"
    }
}

llaves_sistemas = (
'system-id', 'system-name', 'active', 'mantainer', 'alfresco-folder', 'nexus-repository', 'redmine-project',
'gitlab-project')
llaves_aplicaciones = (
'active', 'alfresco-folder', 'application-id', 'gitlab-project', 'mantainer', 'nexus-repository', 'redmine-project',
'system-id', 'technology')
llaves_areas = ('area-id', 'acronym', 'description', 'active', 'created_at', 'updated_at')
llaves_instancias = (
'Architecture', 'active', 'age', 'approved', 'comments', 'contribution', 'criticity', 'db', 'db-engine',
'db-engine-version', 'deploy-repo', 'development-instance', 'documentation-repo', 'external-accesibility',
'frontend-language', 'homo-instance', 'id-sgsa', 'information-access', 'instance-id', 'instance-name', 'issue-tracker',
'language', 'maintenance', 'objective', 'os', 'os-version', 'process-assistance', 'redundancy', 'replacement', 'risk',
'server-language', 'software-type', 'source-repo', 'sub-module', 'system-id', 'user-count')