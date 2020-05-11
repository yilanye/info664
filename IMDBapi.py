import requests, json
import csv
import re

url = "https://movie-database-imdb-alternative.p.rapidapi.com/"
flims = []
# querystring = {"i":"tt7286456","type":"movie","y":"2019"}
list_2020 = ['tt7286456', 'tt7131622', 'tt7549996', 'tt7653254', 'tt1979376', 'tt8579674', 'tt3281548', 'tt6751668', 'tt9351980', 'tt10397932', 'tt1950186', 'tt6394270','tt2066051', 'tt7129636', 'tt8163822','tt2584384']
list_2019 = ['tt1727824', 'tt6966692', 'tt5083738', 'tt7125860', 'tt4633694', 'tt6155172', 'tt1825683', 'tt7775622', 'tt6939026', 'tt6266538', 'tt1517451', 'tt8075496', 'tt6043142','tt7349662','tt1213641']
list_2018 = ['tt4555426', 'tt5027774', 'tt5580036', 'tt2380307', 'tt1856101', 'tt5776858', 'tt5580390', 'tt6333060', 'tt5095260', 'tt5013056', 'tt5639354', 'tt8107568', 'tt6186970', 'tt5726616','tt5052448']
list_2017 = ['tt4034228', 'tt4975722', 'tt3783958', 'tt2671706', 'tt2948356', 'tt3183660', 'tt5275892', 'tt6073176', 'tt2119532', 'tt5186714', 'tt1386697', 'tt5613056', 'tt3470600', 'tt2543164', 'tt3040964', 'tt4034228']
list_2016 = ['tt1663202', 'tt3682448', 'tt3170832', 'tt0810819', 'tt2096673', 'tt1392190', 'tt2870648', 'tt5144072', 'tt3808342', 'tt3460252', 'tt2379713', 'tt1895587', 'tt3829254', 'tt4817576', 'tt0470752', 'tt1596363']
list_2015 = ['tt2980516', 'tt2582802', 'tt3316960', 'tt1065073', 'tt2245084', 'tt2562232', 'tt2278388', 'tt4044364', 'tt3449252', 'tt2718492', 'tt1020072', 'tt0426459', 'tt3071532', 'tt2179136', 'tt0816692', 'tt2084970']
list_2014 = ['tt0790636', 'tt2334873', 'tt2024544', 'tt2294629', 'tt1454468', 'tt1343092', 'tt2396566', 'tt2924484', 'tt2358891', 'tt3043542', 'tt2511594', 'tt1798709']
list_2013 = ['tt0443272', 'tt1853728', 'tt1045658', 'tt1707386', 'tt1217209', 'tt0454876', 'tt1781769', 'tt2125608', 'tt2123210', 'tt1024648', 'tt1602620', 'tt1074638', 'tt2388725', 'tt2088735', 'tt1790885']
list_2012 = ['tt1655442', 'tt1532503', 'tt1007029', 'tt1454029', 'tt1192628', 'tt0970179', 'tt1860355', 'tt2140371', 'tt1568346', 'tt1832382', 'tt1204342', 'tt1778342', 'tt2201259', 'tt1033575', 'tt1605783']
list_2011 = ['tt1504320', 'tt0964517', 'tt0947798', 'tt0964517', 'tt0435761', 'tt1014759', 'tt1375666', 'tt1645089', 'tt1754549', 'tt1285016', 'tt1340107', 'tt0780653', 'tt1669698', 'tt1631323']


list = list_2011 +list_2012 + list_2013 + list_2014 + list_2015 + list_2016 + list_2017 + list_2018 + list_2019 + list_2020

for movie in list:
    querystring ={"i":movie,"type":"movie"}

    headers = {
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
    'x-rapidapi-key': "059129dd04msh013d08bbe2f0b90p1c275djsn22182c2a9fc1"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    results = json.loads(response.text)
    flims.append (results)

with open('Academy_Awards.json','w') as outfile:
    json.dump(flims, outfile, indent = 2)
