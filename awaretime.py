import datetime
import pytz

'''
https://stackoverflow.com/questions/13866926/is-there-a-list-of-pytz-timezones

To get all possible timezones:

for tz in pytz.all_timezones:
    print tz
'''

fmt = '%d-%m %H:%M'
UTC = datetime.datetime.now(tz=pytz.UTC)

CET = UTC.astimezone(pytz.timezone('CET'))
PDT = UTC.astimezone(pytz.timezone('US/Pacific'))
CDT = UTC.astimezone(pytz.timezone('US/Central'))
WAUS = UTC.astimezone(pytz.timezone('Australia/Perth'))
NSWAUS = UTC.astimezone(pytz.timezone('Australia/Sydney'))
QAUS = UTC.astimezone(pytz.timezone('Australia/Brisbane'))
SAUS = UTC.astimezone(pytz.timezone('Australia/Adelaide'))
VAUS = UTC.astimezone(pytz.timezone('Australia/Melbourne'))


print('Brisbane ' + QAUS.strftime(fmt))
print('Perth' + WAUS.strftime(fmt))
print('Berlin ' + CET.strftime(fmt))
print('UTC ' + UTC.strftime(fmt))
print('Dallas ' + CDT.strftime(fmt))
print('Portland ' + PDT.strftime(fmt))
