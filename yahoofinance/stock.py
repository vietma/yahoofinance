from urllib2 import Request, urlopen

class Stock:     
    
    # make this private 
    def __execute(self, symbol, criteria):
        endpoint = 'http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (symbol, criteria)
        request = Request(endpoint)
        response = urlopen(request)
        content = response.read().decode().strip()
        return content
        
    def getLastTrade(self, symbol):
        return self.__execute(symbol, 'l1')
    
    def getDayHigh(self, symbol):
        return self.__execute(symbol, 'h')
    
    def getDayLow(self, symbol):
        return self.__execute(symbol, 'g')
    
    def getChangeInPercent(self, symbol):
        return self.__execute(symbol, 'p2')