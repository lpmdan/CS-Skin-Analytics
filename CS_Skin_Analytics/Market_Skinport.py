import json
import requests
import pandas as pd

class Skinport():
    def __init__(self):
        self.file_path = 'Output/skinport_data.json'
        self.url = "https://api.skinport.com"
        self.params = {
            "app_id": 730,
            "currency": "USD",
        }
        
    def initializeMarketData(self):
        response = requests.get(self.url+'/v1/items' , params=self.params)
        if response.status_code == 200:
            payload = response.json()
            self.skins = pd.DataFrame(payload)
        else:
            print(f"Request failed with status code {response.status_code}")
        
    def getPrice(self, itemname):
        # Look for a row with the item name, and if it exists, return the price. Otherwise, return None.
        row = self.skins.loc[self.skins['market_hash_name'] == itemname]
        if row.empty:
            return None
        else:
            return row.iloc[0]['min_price']
    
    def getUnlockTime(self, itemname):
        return None
        
    def writeToFile(self):
        self.skins.to_json(self.file_path, orient='records')
    
    def readFromFile(self):
        self.skins = pd.read_json(self.file_path, orient='records')