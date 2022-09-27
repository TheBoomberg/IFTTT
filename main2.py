
from ast import Lt
from datetime import datetime, timedelta
from sqlite3 import Timestamp
from xmlrpc.client import DateTime
import pandas as pd
import time
from ifttt_webhook import IftttWebhook

IFTTT_KEY = 'QURN99egyRSfPLEIN4dUq'
ifttt = IftttWebhook(IFTTT_KEY)

DAcsv = pd.read_csv (r'/Users/bjorn/Documents/Python/ifttt/DayAheadSE4.csv')
df = pd.DataFrame(DAcsv)

LT = datetime.now() - timedelta(hours = 1)
LTF = LT.strftime("%Y-%m-%d %H")


CurrentLevel = df.loc[df['Datetime'] == pd.Timestamp("now").strftime("%Y-%m-%d %H"), 'LevelSE4'].iloc[0]
LastLevel = df.loc[df['Datetime'] == LTF, 'LevelSE4'].iloc[0]

print(CurrentLevel)
print(LastLevel)


while True:
    if CurrentLevel == 'Low' and LastLevel == 'High':
        ifttt.trigger('SE4_price_low', value1=5)
    elif CurrentLevel == 'High' and LastLevel == 'Low':
        ifttt.trigger('SE4_price_high', value1=5)
    else:
        time.sleep(10)