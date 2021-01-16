import requests

url = 'https://www.zillow.com/san-jose-ca/fsbo/'

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6',
    'cache-control': 'max-age=0',
    'cookie': 'JSESSIONID=25C41912C005B6BC2A3BFA7C2F077DFE; zguid=23|%24df581793-da10-4f72-aa33-164376eed35d; zgsession=1|b7a926a8-653a-439e-b514-de7ad22bf21f; _ga=GA1.2.875758300.1610836707; _gid=GA1.2.937883808.1610836707; zjs_user_id=null; zjs_anonymous_id=%22df581793-da10-4f72-aa33-164376eed35d%22; _gcl_au=1.1.1282373530.1610836729; KruxPixel=true; DoubleClickSession=true; _fbp=fb.1.1610836730256.1855954493; _derived_epik=dj0yJnU9QnplSWpKSlJ0cG1MZnF5djFrUTR0S3RfZENjNUphdjMmbj0zSDFjaVBuMHpnX1FuWUVsRDdkUDVnJm09MSZ0PUFBQUFBR0FEYXZvJnJtPTEmcnQ9QUFBQUFHQURhdm8; _pin_unauth=dWlkPU5HTmlOR1ZsWTJJdE1qWTBaQzAwWmpZNUxXRTNOR010WXpabE1EVTRZelpqWkRrMQ; KruxAddition=true; _pxvid=aa42e7b9-584b-11eb-884a-0242ac12000d; _px3=1bc52ba2ca3d70da5d8662913af8ffde100bc8b8738b3157c4ed3c1c954f0e36:z6sdGMYwtnhryLFsFw/N2WlXkY0LyaFTcFgPyf8lTFKX14ydzU6E+N5jdKaWoKMR8pqytXfraFBIy+c8O4iOgA==:1000:4DwJdPObzuceo733GpZkEYiFtro/+nDQkfEOCiqpgz7JQybUCqz3i4u4FE2OrX87WXWK70mRAgHmka76lBJ6VFf+Oozis3A/lp2F5unzSDD1h5DFKH+XMzLurouJYifzF/qgJ5PCHYyr4B10AkXYnPQs8ziU62Js5XxvzJM2ays=; _uetsid=9a3ab280584b11eb928f5b12d8cafb7d; _uetvid=9a3b4ed0584b11ebb69d475576214d34; __gads=ID=0d4f1266b4e0b7df:T=1610836760:S=ALNI_MYFuyvyqpvstqFOR7gfbO_bzoScYA; _gat=1; AWSALB=M6gAPkpZaWWU8rtO0ReFt6ToUmHCiZItQwo8SQuk8V8a1YYxXiUP0rTpgllr+R5MqUCyIozVBK8C7MYX9ZvikvLR8gRHKRx9S0rNeAXNA0YSusBBL2EHtO2+Cs8u; AWSALBCORS=M6gAPkpZaWWU8rtO0ReFt6ToUmHCiZItQwo8SQuk8V8a1YYxXiUP0rTpgllr+R5MqUCyIozVBK8C7MYX9ZvikvLR8gRHKRx9S0rNeAXNA0YSusBBL2EHtO2+Cs8u; search=6|1613428812312%7Crect%3D37.471773406402754%252C-121.5347786508789%252C37.14572594567122%252C-122.2152443491211%26rid%3D33839%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D1%26lt%3Dfsbo%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%09%0933839%09%09%09%09%09%09',
    'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.'
    }

params ={
    'searchQueryState': '{"pagination":{},"mapBounds":{"west":-122.2152443491211,"east":-121.5347786508789,"south":37.14572594567122,"north":37.471773406402754},"regionSelection":[{"regionId":33839,"regionType":6}],"isMapVisible":true,"category":"cat2","filterState":{"sort":{"value":"globalrelevanceex"},"fsba":{"value":false},"nc":{"value":false},"fore":{"value":false},"cmsn":{"value":false},"auc":{"value":false},"pmf":{"value":false},"pf":{"value":false},"ah":{"value":true}},"isListVisible":true,"mapZoom":11}'
    }

response = requests.get(url, headers=headers, params=params)
print(response)

class ZillowScraper():

    