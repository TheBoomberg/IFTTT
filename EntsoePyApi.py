# Program should be run once 00:00:01 re-occuring every day

import pandas as pd
from entsoe import EntsoePandasClient
import numpy as np
import schedule
import time

#def create_df_se4():
client = EntsoePandasClient(api_key='80208ebc-a0e8-43ac-bc69-77749824d3d8')
today = pd.Timestamp("today").strftime("%Y%m%d") # Fetch todays date
#tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y%m%d") # Fetch tomorrows date

# Input parameters for entsoe API request
start = pd.Timestamp(today+' '+'00:00:00', tz ='Europe/Stockholm')
end = pd.Timestamp(today+' '+'23:00:00', tz ='Europe/Stockholm')
country_code_1 = 'SE_1'  # Swedish elomrade SE1
country_code_2 = 'SE_2'  # Swedish elomrade SE2
country_code_3 = 'SE_3'  # Swedish elomrade SE3
country_code_4 = 'SE_4'  # Swedish elomrade SE4

DA_pricesSE4 = client.query_day_ahead_prices(country_code_4, start=start,end=end) #query day-ahead market prices (€/MWh) from entsoe pandaclient
indexsize = DA_pricesSE4.size # counting the number of hours in the response
dailysum = DA_pricesSE4.sum() # the sum of all hourly prices for the response
average = dailysum/indexsize # average price over all hours in the response

df = pd.Series.to_frame(DA_pricesSE4).reset_index()
df.columns = ['Datetime', 'PriceSE4']

#df['Datetime'].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S"))

# Create level column and write low if price is below daily average, high if above
df['LevelSE4'] = np.where(df['PriceSE4'] < average, 'Low', 'High')
# Format date time to enable comparison on hurly base
df['Datetime'] = df['Datetime'].dt.strftime("%Y-%m-%d %H")

df.to_csv('DayAheadSE4.csv') #save to csv

# schedule.every(1).day.at("00:00").do(create_df_se4)
# while 1:
#         schedule.run_pending()
#         time.sleep(1)

