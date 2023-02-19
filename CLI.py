import requests
import json
r = requests.get('http://127.0.0.1:5000/json') #resolve issue of key conflict

maps = json.loads(r.text)
long_url = input("Enter URL to shorten: ")

#print(maps)

def shorten(long_url, max_index):
    if long_url not in maps.values():
        symbols = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        base = len(symbols)
        num = max_index+1
        out = ''
        while(num!=0):
            out=str(symbols[num%base])+out
            #print(num%16)
            num=num//base
            #print(num)
        base_url = "http://127.0.0.1:5000"
        short_url = base_url+'/'+out
        add_on = {short_url: long_url}
        return add_on
    else:
        return None #implying map already exists.
    
short_url_addon = shorten(long_url, len(maps))

#print(short_url_addon)

if(short_url_addon is not None):
    payload = json.dumps(short_url_addon)
    headers = {"Content-Type": "application/json"}
    r = requests.post("http://127.0.0.1:5000/update", data=payload, headers=headers)
    print(r.text)
    #print(payload)
else:
    print('{\''+list(maps.keys())[list(maps.values()).index(long_url)]+'\': \''+long_url+'\'}')
