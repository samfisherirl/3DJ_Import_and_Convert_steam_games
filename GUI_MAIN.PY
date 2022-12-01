import eel
import time
import os
import random
import import_gspread_table as GS

eel.init(f'{os.path.dirname(os.path.realpath(__file__))}/web') 
array = [1,2,3,4,5,6,7,8,9,10]

val = random.randint(0,9)
val1 = random.randint(0,9)
port = int('80{}{}'.format(val, val1))
@eel.expose
def hello():
    val2 = GS.search()
    eel.returner(val2)
      # in python it will call this function
      #  and push val2 over as val      
      # // instantiate python function with onfocus timing

    return val2

my_options = {
    'mode': "chrome", # or "chrome-app",
    'host': 'localhost',
    'port': port,
    'chromeFlags': ["--start-fullscreen", "--browser-startup-dialog"]
}
eel.start('hello.html', options=my_options, suppress_error=True, size=(1150, 1000))
