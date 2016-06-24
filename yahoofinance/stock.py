from urllib2 import Request, urlopen
from urllib import urlencode
import json

class Stock:     
    
    # make this private 
    def __search(self, symbol, criteria):
        endpoint = 'http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (symbol, criteria)
        request = Request(endpoint)
        response = urlopen(request)
        content = response.read().decode().strip()     
        return content
        
    def get_last_trade(self, symbol):
        return self.__search(symbol, 'l1')
    
    def get_day_high(self, symbol):
        return self.__search(symbol, 'h')
    
    def get_day_low(self, symbol):
        return self.__search(symbol, 'g')
    
    def get_change_in_percent(self, symbol):
        return self.__search(symbol, 'p2')
    
    def get_historical_prices_as_dictionary(self, symbol, start_date, end_date):
        # start_date and end_date are in format 'YYYY-MM-DD'
        params = urlencode({
            's': symbol,
            'a': int(start_date[5:7]) - 1, # MM
            'b': int(start_date[8:10]),    # DD
            'c': int(start_date[0:4]),     # YYYY 
            'd': int(end_date[5:7]) - 1,
            'e': int(end_date[8:10]),
            'f': int(end_date[0:4]),
            'g': 'd',
            'ignore': '.csv'
        })
        endpoint = 'http://real-chart.finance.yahoo.com/table.csv?%s' % params
        print 'historical prices endpoint = %s' % endpoint
        
        request = Request(endpoint)
        response = urlopen(request)
        content = str(response.read().decode('utf-8').strip())
        
        daily_data = content.splitlines()
        
        history_dict = dict()
        keys = daily_data[0].split(',')
        
        for day in daily_data[1:]:
            day_data = day.split(',')
            date = day_data[0]
            history_dict[date] = {
                keys[1]: day_data[1],
                keys[2]: day_data[2],
                keys[3]: day_data[3],
                keys[4]: day_data[4],
                keys[5]: day_data[5],
                keys[6]: day_data[6]
            }
        
#        history_json = json.dumps(history_dict)        
#        return history_json
        return history_dict
    
    def get_historical_prices_as_json(self, symbol, start_date, end_date):
        return json.dumps(self.get_historical_prices_as_dictionary(symbol, start_date, end_date))