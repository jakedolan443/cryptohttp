import cryptowatch as cw
import threading
import time
import json


class Server:
    def __init__(self, refresh_rate):
        self.refresh_rate = refresh_rate
        with open("coins.json", "r") as f:
            data = f.read()
        self.__coins = list(json.loads(data).keys())
        self.__coin_names = json.loads(data)
        self.__cache = []
        
        threading.Thread(target=self.fetch_new_data).start()
        
    def query_coin_name(self, code):
        try:
            return self.__coin_names[code]
        except KeyError:
            return False
        
    def read_coins_file(self):
        with open("config/coins.conf", "r") as f:
            data = f.read()
        ls = []
        data = data.split("\n")
        for line in data:
            if line in self.__coins:
                ls.append(line)
        return ls
        
    def fetch_new_data(self):
        coins = self.read_coins_file()
        ls = []
        for coin in coins:
            req = cw.markets.get("KRAKEN:{}USD".format(coin))
            candles = cw.markets.get("KRAKEN:{}USD".format(coin), ohlc=True, periods=["1d"])
            data = req._http_response._content.decode()
            older_data = json.loads(candles._http_response._content.decode())['result']
            d = {}
            d['img'] = "/icons/{}.png".format(coin.lower())
            d['price'] = "{:.2f}".format(round(float(data.split('"last":')[1].split(",")[0]), 2))
            real_change = round(float(data.split('"change":')[1].split(",")[0].split(":")[1])*100, 2)
            if real_change > 0:
                d['change_colour'] = "green"
                d['change_symbol'] = "▲"
                d['change'] = "+{:.2f}%".format(real_change)
            else:
                d['change_colour'] = "red"
                d['change_symbol'] = "▼"
                d['change'] = "{:.2f}%".format(real_change)
            d['code'] = coin
            d['name'] = self.__coin_names[coin]
            d['past'] = []
            for entry in older_data:
                for dump in older_data[entry]:
                    d['past'].append([dump[0]*1000, dump[1]])
                    d['past'].append([dump[0]*1000, dump[4]])
                
            ls.append(d)
        self.__cache = ls.copy()
        time.sleep(self.refresh_rate)
        self.fetch_new_data()
        
    def get_coin_data(self, coin):
        coin_data = self.__cache[next((index for (index, d) in enumerate(self.__cache) if d["code"] == coin), None)]
        return coin_data
        
    def get_graph_data(self, coin):
        coin_data = self.__cache[next((index for (index, d) in enumerate(self.__cache) if d["code"] == coin), None)]
        print(coin_data['past'])
        return coin_data['past']
    

        
    def get_data(self):
        return self.__cache
