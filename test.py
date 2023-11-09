from lib import *

# path
ticker_data = pd.read_csv('ticker_data_with_industry.csv', parse_dates=['time'], date_parser=lambda x: pd.to_datetime(x, format='%Y-%m-%d'))


# get all ticker name
def ticker_name(data_ticker):
    return data_ticker['ticker'].unique().tolist()



# get data of a specific ticker
def take_data_ticker(data_ticker, name_ticker):
    data_source = []
    for ticker in name_ticker:
        filtered_data = data_ticker[data_ticker['ticker'] == ticker]
        data_source.append(filtered_data)
    return data_source


# data
code_ticker_taken = ['SSI']
# code_ticker_taken = ticker_data['ticker'].unique()
data_full = take_data_ticker(ticker_data, code_ticker_taken)

# momentum indicators
for data in data_full:
    momentum_adx = talib.ADX(data['high'],data['low'],data['close'])
    momentum_adxr = talib.ADXR(data['high'],data['low'],data['close'])
    momentum_apo = talib.APO(data['close'])
    momentum_aroonUP, momentum_arronDOWN = talib.AROON(data['high'],data['close'])
    momentum_arronosc = talib.AROONOSC(data['high'],data['close'])
    momentum_bop = talib.BOP(data['open'],data['high'],data['low'])
    print(momentum_aroonUP.shape)
    talib.ACOS()
    talib.ACOS()