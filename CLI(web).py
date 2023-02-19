import requests
import json
print("Welcome to URL Shortener.\n")
try:
    r = requests.get('http://ak10.pythonanywhere.com/-json') #resolve issue of key conflict
    #using '-' ensures that a key-value pair containing '-json' as key is never generated, since '-' is not in symbols.
    maps = json.loads(r.text)
    long_url = input("Enter URL to shorten: ")

    #print(maps)

    def shorten(long_url, max_index): #this essentially makes a key represented by len(symbols) base number system.
        #It is done like that because a higher base would be able to store more information in same number of characters than base 10.
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
            base_url = "http://ak10.pythonanywhere.com"
            short_url = base_url+'/'+out
            add_on = {short_url: long_url}
            return add_on
        else:
            return None #implying map already exists.
        
    short_url_addon = shorten(long_url, len(maps))

    #print(short_url_addon)

    if(short_url_addon is not None):
        payload = json.dumps(short_url_addon)
        headers = {"Content-Type": "application/json"} #for MIME type
        r = requests.post("http://ak10.pythonanywhere.com/-update", data=payload, headers=headers)
        #print(r.text)
        length_shortened=len(long_url)-len(r.text)
        #print(length_shortened)
        if length_shortened>0:
            print("\nYour URL has been shortened by "+str(length_shortened)+" characters!")
            print("Here's your shortened URL, "+r.text)
        else:
            print("\nYour URL was already too small and couldn't be shortened more.")
            print("Here's your shortened URL, "+r.text)

    else:
        #print('{\''+list(maps.keys())[list(maps.values()).index(long_url)][7:]+'\': \''+long_url+'\'}')
        short_url = list(maps.keys())[list(maps.values()).index(long_url)][7:] #returns the key from given value as long_url.
        length_shortened=len(long_url)-len(short_url)
        if length_shortened>0:
            print("\nYour URL has been shortened by "+str(length_shortened)+" characters!")
            print("Here's your shortened URL, "+short_url)
        else:
            print("\nYour URL was already too small and couldn't be shortened more.")
            print("Here's your shortened URL, "+short_url)

    ask = input("\nPress enter to exit.")
except:
    print("Connection failed.")
