import json
import requests

class Afvalwijzer:
    
    postcode = ''
    huisnr = ''
    bagid = None
    afvalinfo = None
    ophaaldata = None
    
    def __init__(self, postcode, huisnr):
        self.postcode = postcode
        self.huisnr = huisnr
        self.bagid = None
        self.afvalinfo = None
        self.ophaaldata = None

    def resolve(self):
        try:
            url = 'https://inzamelwijzer.prezero.nl/adressen/'+ self.postcode + ':' + str(self.huisnr)
            response = requests.get(url)
            data = response.json()
            self.bagid = response.json()[0]['bagid']
        except Exception as e:
            print('Helaas... {}'.format(e))
            self.bagid = None
    
    def retrieve_data(self):
        if not self.bagid:
            self.resolve()
        try:
            url = 'https://inzamelwijzer.prezero.nl/rest/adressen/' + self.bagid + '/afvalstromen'
            response = requests.get(url)
            self.afvalinfo = json.loads(response.text)
        except Exception as e:
            print('Helaas... {}'.format(e))
            self.afvalinfo = []

    def get_ophaaldata(self):
        self.ophaaldata = None
        if not self.afvalinfo:
            self.retrieve_data()
        self.ophaaldata = []
        for afl in afval.afvalinfo:
            if afl['ophaaldatum']:
                el = {'product':afl['title'].replace(' Arnhem', ''), 'datum': afl['ophaaldatum']}
                self.ophaaldata.append(el)        
    
    def __get_datum__(self, product):
        if not self.ophaaldata:
            self.get_ophaaldata()
        if self.ophaaldata:
            for d in self.ophaaldata:
                if d['product'] == product:
                    return d['datum']
        return None
            
    def get_volgende_groen(self):
        return self.__get_datum__('Groente-, fruit en tinafval')
    
    def get_volgende_plastic(self):
        return self.__get_datum__('Plastic, blik & drinkpakken')
            
    def get_volgende_papier(self):
        return self.__get_datum__('Papier en karton')
