import requests
VIRT_PATH = 'app/virt/'
def scan_url(resource):
    apikey = None
    with open(VIRT_PATH+'apikey','r') as f:
        apikey = f.read()
        apikey = apikey.split('\n')[0]
    url = 'https://www.virustotal.com/vtapi/v2/url/report'
    params = {'apikey': apikey, 'resource':resource,'scan':1}
    response = requests.get(url, params=params)
    api_result = response.json()
    print(api_result)
    scan_result = dict() 
    scan_result.update({'scan_date':api_result['scan_date']})
    scan_result.update({'positives':api_result['positives']})
    scan_result.update({'total':api_result['total']})

    malsite_detect = dict()
    for scan in api_result['scans'].keys():
        if api_result['scans'][scan]['detected']:
            malsite_detect.update({scan:api_result['scans'][scan]})
    scan_result.update({'deteted_machine':malsite_detect})
    return scan_result 
