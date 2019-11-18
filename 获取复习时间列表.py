from datetime import datetime
from datetime import timedelta
import pyperclip

today = datetime.today()

oneday = timedelta(days = 1)
oneweek = timedelta(weeks = 1)
onemonth = timedelta(days = 31)
oneyear = timedelta(days = 365)

today_1day = today-oneday
today_2day = today-2*oneday
today_3day = today-3*oneday

today_1week = today-oneweek
today_1month = today-onemonth
today_3month = today-3*onemonth

today_1year = today-oneyear

today_str = today.date().strftime('%Y%m%d')
today1day_str = today_1day.date().strftime('%Y%m%d')
today2day_str = today_2day.date().strftime('%Y%m%d')
today3day_str = today_3day.date().strftime('%Y%m%d')
today1week_str = today_1week.date().strftime('%Y%m%d')
today1month_str = today_1month.date().strftime('%Y%m%d')
today3month_str = today_3month.date().strftime('%Y%m%d')
today1year_str = today_1year.date().strftime('%Y%m%d')

searchcmd_str = today_str + ' || ' + today1day_str + ' || ' + today2day_str + ' || ' + today3day_str + ' || ' + today1week_str + ' || ' + today1month_str + ' || ' + today3month_str + ' || ' + today1year_str

pyperclip.copy(searchcmd_str)