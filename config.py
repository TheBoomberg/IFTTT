from pydantic import BaseSettings
import csv
class Settings(BaseSettings):
    IFTTT_SERVICE_KEY: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()

# class DayAhead:

#     def __init__(self, df):
#         self.df = df

# dayahead = DayAhead()


# class DayAhead:
#    def __init__(self, row, header):
#         self.__dict__ = dict(zip(header, row))

# data = list(csv.reader(open('DayAhead.csv')))
# instances = [DayAhead(i, data[0]) for i in data[1:]]

# print (data)
