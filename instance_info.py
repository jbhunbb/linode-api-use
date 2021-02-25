import requests, json

def call_api(value):

    keypath = '/home/bhji/github/ctf_git/api_key/linode.key'
    keyopen = open(keypath, 'r')
    key = keyopen.read()
    keyopen.close()

    api_host = 'https://api.linode.com/v4/' + value

    header = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + key,
    }
    params = {
            'page_size' : 500
    }
    
    result = requests.get(api_host, params=params , headers=header).json()
    return result

result = call_api('linode/instances')
for i in range(len(result['data'])):
    print(f" {result['data'][i]['id']}) {result['data'][i]['label']} {result['data'][i]['ipv4']}")

