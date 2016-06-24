from urllib2 import Request, urlopen
import urllib
import json
from collections import OrderedDict
import datetime
from yahoofinance import Stock

class Stocks:
    
    def __init__(self):
        self.criteria_dict = OrderedDict()
        # include symbol in the search criteria
        self.criteria_dict['symbol'] = 's'    
    
    
    def __remove_double_quotes(self, s):
        if s.find('"') != -1:
            return s.replace('"', '')
        return s
    
    
    def __search(self, list_of_symbols, criteria_dictionary):
        # symbols: list of symbols with + sign
        symbols = list_of_symbols.replace(',', '+')
        symbols = symbols.replace(' ', '') 
           
        search_criteria = ''
        for v in criteria_dictionary.itervalues():
            search_criteria += str(v)
        
        search_string = urllib.quote(search_criteria)
        
        endpoint = 'http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (symbols, search_string)
        print 'endpoint = %s' % endpoint 
                
        request = Request(endpoint)
        response = urlopen(request)
        
        content = str(response.read().decode('utf-8').strip())
        
        rows = content.splitlines()
        data_dict = dict()
        
        today = datetime.date.today() # YYYY-MM-DD        
        week_ago = today - datetime.timedelta(days=7) # YYYY-MM-DD
        
        start_date = week_ago.strftime('%Y-%m-%d')
        end_date = today.strftime('%Y-%m-%d')
        
        
        for row in rows:
            row_data = row.split(',')
            idx = 0
            inner_dict = dict()
            symbol = self.__remove_double_quotes(row_data[0])
            for key in criteria_dictionary:                
                if criteria_dictionary.keys().index(key) == 0:
                    inner_dict['historical_prices'] = Stock().get_historical_prices_as_dictionary(symbol, start_date, end_date)
                else:                                        
                    idx += 1
                    inner_dict[key] = self.__remove_double_quotes(row_data[idx])                    
                                      
            data_dict[symbol] = inner_dict
        
        data_json = json.dumps(data_dict)
        return data_json
    
    def get_financial_data(self, list_of_symbols):                 
        return self.__search(list_of_symbols, self.criteria_dict)
    
    def set_last_trade(self):
        self.criteria_dict['last_trade'] = 'l1'
        
    def set_day_low(self):
        self.criteria_dict['day_low'] = 'g'
        
    def set_day_high(self):
        self.criteria_dict['day_high'] = 'h'
        
    def set_change_in_percent(self):
        self.criteria_dict['change_in_percent'] = 'p2'
        
    def set_open(self):
        self.criteria_dict['open'] = 'o'
        
    def set_previous_close(self):
        self.criteria_dict['previous_close'] = 'p'
        
    def set_52_week_low(self):
        self.criteria_dict['52_week_low'] = 'j'
        
    def set_52_week_high(self):
        self.criteria_dict['52_week_high'] = 'k'
        
    def set_last_trade_date(self):
        self.criteria_dict['last_trade_date'] = 'd1'
   
    def set_last_trade_time(self):
        self.criteria_dict['last_trade_time'] = 't1'
    
    def set_50_day_moving_average(self):
        self.criteria_dict['50_day_moving_average'] = 'm3'
        
    def set_200_day_moving_average(self):
        self.criteria_dict['200_day_moving_average'] = 'm4'
        
    def set_dividend_yield(self):
        self.criteria_dict['dividend_yield'] = 'y'
        
    def set_dividend_per_share(self):
        self.criteria_dict['dividend_per_share'] = 'd'
        
    def set_dividend_pay_date(self):
        self.criteria_dict['dividend_pay_date'] = 'r1'
        
    def set_stock_exchange(self):
        self.criteria_dict['stock_exchange'] = 'x'
        
    def set_name(self):
        self.criteria_dict['name'] = 'n'
        
    def set_more_info(self):
        self.criteria_dict['more_info'] = 'i'
        
    def set_market_capitalization(self):
        self.criteria_dict['market_capitalization'] = 'j1'
        
    def set_volume(self):
        self.criteria_dict['volume'] = 'v'
        
    def set_average_daily_volume(self):
        self.criteria_dict['average_daily_volume'] = 'a2'
        
    def set_ticker_trend(self):
        self.criteria_dict['ticker_trend'] = 't7'
        
    def set_earnings_per_share(self):
        self.criteria_dict['earnings_per_share'] = 'e'
        
    def set_eps_estimate_current_year(self):
        self.criteria_dict['eps_estimate_current_year'] = 'e7'
        
    def set_eps_estimate_next_year(self):
        self.criteria_dict['eps_estimate_next_year'] = 'e8'
        
    def set_eps_estimate_next_quarter(self):
        self.criteria_dict['eps_estimate_next_quarter'] = 'e9'
        
    def set_pe_ratio(self):
        self.criteria_dict['pe_ratio'] = 'r'
        
    def set_peg_ratio(self):
        self.criteria_dict['peg_ratio'] = 'r5'
        
    def set_revenue(self):
        self.criteria_dict['revenue'] = 's6'
        
    def set_annualized_gain(self):
        self.criteria_dict['annualized_gain'] = 'g3'