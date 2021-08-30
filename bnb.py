import requests, json

def get_bnb_prices():
    #bnb
    bnb_url="https://api.binance.com/api/v3/ticker/price?symbol=BNBUSDT"
    bnb_reqs = requests.get(bnb_url)
    #bnb_price = ""
#利用json.loads()解碼JSON
    bnb_reqsjson = json.loads(bnb_reqs.text)
    bnb_price = "🚀代幣名稱 : BNB 🚀\n💰價格💰 : $"+ bnb_reqsjson['price'][0:6]
    bnb_coin = bnb_price+"\n\n=============================\n"
    return bnb_coin
def get_baby_prices():
    #babydoge
    baby_url="https://api.pancakeswap.info/api/v2/tokens/0xc748673057861a797275cd8a068abb95a902e8de"
    baby_reqs = requests.get(baby_url)
    baby_name = ""
    baby_price = ""
    #利用json.loads()解碼JSON
    baby_reqsjson = json.loads(baby_reqs.text)
    baby_name = "\n🚀代幣名稱 : " + baby_reqsjson['data']['name']+" 🚀\n"
    baby_price = "\n💰價格 : $"+ baby_reqsjson['data']['price'][0:16]+"💰\n"
    baby_coin = baby_name+baby_price+"\n=============================\n"
    return baby_coin
    
def get_fibo_prices():
    #fibo
    fibo_url="https://api.pancakeswap.info/api/v2/tokens/0x5067c6e9e6c443372f2e62946273abbf3cc2f2b3"
    fibo_reqs = requests.get(fibo_url)
    fibo_name = ""
    fibo_price = ""
    #利用json.loads()解碼JSON
    fibo_reqsjson = json.loads(fibo_reqs.text)
    fibo_name = "\n🚀代幣名稱 : " + fibo_reqsjson['data']['name']+" 🚀\n"
    fibo_price = "\n💰價格 : $"+ fibo_reqsjson['data']['price'][0:8]+"💰\n"
    fibo_coin = fibo_name+fibo_price+"\n=============================\n"
    return fibo_coin
    
def get_gmyx_prices():
    #gmyx
    gmyx_url="https://api.pancakeswap.info/api/v2/tokens/0x1dd813524e0a0f4a36965f24d13bd8a37e51d848"
    gmyx_reqs = requests.get(gmyx_url)
    gmyx_name = ""
    gmyx_price = ""
    #利用json.loads()解碼JSON
    gmyx_reqsjson = json.loads(gmyx_reqs.text)
    gmyx_name = "\n🚀代幣名稱 : " + gmyx_reqsjson['data']['name']+" 🚀\n"
    gmyx_price = "\n💰價格 : $"+ gmyx_reqsjson['data']['price'][0:10]+"💰\n"
    gmyx_coin = gmyx_name+gmyx_price+"\n=============================\n"
    return gmyx_coin