import time
import lcddriver
import time
import datetime
import subprocess
import datetime
import pytz
import i2c_lib

'''
https://stackoverflow.com/questions/13866926/is-there-a-list-of-pytz-timezones
To get all possible timezones:
for tz in pytz.all_timezones:
    print tz

Brisbane = ['Don', 'James', 'Mike', 'Shaffi']
Dallas = ['Jeremy']
Perth = ['Pete']
Portland = ['Zach']

'''

display_2 = lcddriver.lcd(0x22)
display_3 = lcddriver.lcd(0x23)
display_4 = lcddriver.lcd(0x24)
display_5 = lcddriver.lcd(0x25)
display_6 = lcddriver.lcd(0x26)
display_7 = lcddriver.lcd(0x27)

fmt = '%d-%m %H:%M:%S'


try:

 
    while True:   
       
        UTC = datetime.datetime.now(tz=pytz.UTC)
        CET = UTC.astimezone(pytz.timezone('CET'))
        PDT = UTC.astimezone(pytz.timezone('US/Pacific'))
        CDT = UTC.astimezone(pytz.timezone('US/Central'))
        QAUS = UTC.astimezone(pytz.timezone('Australia/Brisbane'))
        WAUS = UTC.astimezone(pytz.timezone('Australia/Perth'))
        NSWAUS = UTC.astimezone(pytz.timezone('Australia/Sydney'))
        SAUS = UTC.astimezone(pytz.timezone('Australia/Adelaide'))
        VAUS = UTC.astimezone(pytz.timezone('Australia/Melbourne'))
        
        utc = UTC.strftime(fmt)
        berlin = CET.strftime(fmt)
        portland = PDT.strftime(fmt)
        dallas = CDT.strftime(fmt)
        brisbane = QAUS.strftime(fmt)
        perth = WAUS.strftime(fmt)
        sydney = NSWAUS.strftime(fmt)
        adelaid = SAUS.strftime(fmt)
        melbourne = VAUS.strftime(fmt)
        
        print('start of loop')

        # first display city name and time
        display_2.lcd_display_string("Portland", 1) # Write line of text to first line of display
        display_2.lcd_display_string(portland, 2) # Write just the time to the display

        display_3.lcd_display_string("Dallas", 1)
        display_3.lcd_display_string(dallas, 2)
        
        display_4.lcd_display_string("UTC", 1)
        display_4.lcd_display_string(utc, 2)
        
        display_5.lcd_display_string("Berlin", 1)
        display_5.lcd_display_string(cet, 2)
        
        display_5.lcd_display_string("Perth", 1)
        display_5.lcd_display_string(perth, 2)
        
        display_7.lcd_display_string("Brisbane", 1)
        display_7.lcd_display_string(brisbane, 2)

        time.sleep(1)

        # then display team-mate name and time
        display_2.lcd_display_string("Zach", 1) # Write line of text to first line of display
        display_2.lcd_display_string(brisbane, 2) # Write just the time to the display

        display_3.lcd_display_string("Jermey", 1)
        display_3.lcd_display_string(dallas, 2)
        
        display_4.lcd_display_string("UTC", 1)
        display_4.lcd_display_string(utc, 2)
        
        display_5.lcd_display_string("Dustin", 1)
        display_5.lcd_display_string(cet, 2)
        
        display_5.lcd_display_string("Pete", 1)
        display_5.lcd_display_string(perth, 2)
        
        display_7.lcd_display_string("Don, Shaffi, James, Mike", 1)
        display_7.lcd_display_string(brisbane, 2)

        time.sleep(1)

        print('end of loop')
        

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
