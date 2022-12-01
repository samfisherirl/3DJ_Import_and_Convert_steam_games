import eel

# Set web files folder
eel.init('web')

 
eel.start('hello.html', options=options)
#eel.start('hello.html', mode='custom', cmdline_args=['node_modules/electron/dist/electron.exe', '.'])
