#!/usr/bin/python
# -*- coding: utf-8 -*-



import requests

# cookies = {
#     'f5avrbbbbbbbbbbbbbbbb': 'LDIPDOECIPIPGANKNJPFFIBMFIGMENEBHHFLMLBJAFMBCALOOGOGMIIGEGAEPIPBDPMDODHJPAMNCAGHDPNAMDMODJJNNHLBKAHAGLEPKEEMGFMOIEDLAGOONJMMHOPG',
#     'BIGipServerpool_prod_selfservice_8031': '1023919882.24351.0000',
# }

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Sec-Fetch-User': '?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

# response = requests.get('https://selfservice.pasadena.edu/prod/pw_psearch_sched.p_search', headers=headers, cookies=cookies)
response = requests.get('https://selfservice.pasadena.edu/prod/pw_psearch_sched.p_search', headers=headers)


print(response.text)




