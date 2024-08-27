import requests
from bs4 import BeautifulSoup
import json

def ibonAPI(city):
    try:
        url = 'https://www.ibon.com.tw/retail_inquiry_ajax.aspx'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': '_ga=GA1.3.927991393.1585149670;_gid=GA1.3.688677455.1585149670',
        }
        formData = {
            'strTargetField': 'COUNTY',
            'strKeyWords': city,
        }
        response = requests.post(url, data=formData, headers=headers)
        return response
    except Exception as e:
        print(e)
        return e

def parseStoreInfo(ibonInfo):
    try:
        soup = BeautifulSoup(ibonInfo.text, 'html.parser')
        store = []
        for row in soup.select('table tr'): # CSS Selector
            columns = row.find_all('td')
            if len(columns) == 3:
                store.append({
                    'code': columns[0].get_text().strip(),
                    'storeName': columns[1].get_text().strip(),
                    'address': columns[2].get_text().strip(),
                })
        return store
    except Exception as e:
        print(e)
        return e

def getStoreInfo(city):
    try:
        ibonInfo = ibonAPI(city)
        storeInfo = parseStoreInfo(ibonInfo)
        return storeInfo
    except Exception as e:
        print(e)
        return e

store_info = getStoreInfo('台北市')
print(json.dumps(store_info, ensure_ascii=False, indent=2))
