# technical indicator
# ma10 20 50 200
# macd
# rsi

from vnstock import *
import pandas as pd
from datetime import datetime

# date start
START = "2018-10-29"
START_datetime = datetime.strptime(START, '%Y-%m-%d').date()

# date end
TODAY_datetime = datetime.now()
TODAY = TODAY_datetime.strftime('%Y-%m-%d')

# listing companies on HOSE, HNX, UPCOM
list_comp = listing_companies()
ticker_codes = list_comp["ticker"]
# ticker_codes = ['VCB','VNM','HPG','SSI']

industry_data_cache = {}

# Define a function to get the industry for a ticker using company_overview with caching
def get_industry(ticker_code):
    if ticker_code in industry_data_cache:
        return industry_data_cache[ticker_code]

    # Replace this with your actual function call
    industry = company_overview(ticker_code)['industry']
    industry_data_cache[ticker_code] = industry
    return industry


# download data
data_ticker = pd.DataFrame()
for ticker_code in ticker_codes:
    try: 
        df = stock_historical_data(ticker_code, START, TODAY, "1D", 'stock')
        if not df.empty:
            last_1_day = df.tail(1)
            last_5_day = df.tail(5)
            first_day = df.head(1)
            first_day_time = first_day['time'].iloc[0]
            last_1_price = int(last_1_day['close'].iloc[0])
            last_5_vol = int(last_5_day['volume'].sum())
            # check if ticker has volume more than 500k and its price less than 10k, list time = request time of data
            if (last_5_vol > 500000) and (last_1_price > 10000) and (START_datetime.year == first_day_time.year):
                data_ticker = pd.concat([data_ticker, df])
    except Exception as e:
        print(f"Error retrieving data for {ticker_code}: {e}")

data_ticker['industry'] = data_ticker['ticker'].apply(get_industry)
data_ticker = data_ticker.reset_index(drop=True)
data_ticker.to_csv('ticker_data_with_industry.csv', index=False)

