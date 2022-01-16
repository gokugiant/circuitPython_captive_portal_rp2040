# circuitPython_captive_portal_rp2040

1. To run the code you have to create a secret.py file in the following format in the toot directory. 


```
\# This file is where you keep secret settings, passwords, and tokens!

\# If you put them in the code you risk committing that info or sharing it

secrets = {
    'ssid' : 'quantum',
    'password' : 'quantum',
    'timezone' : "America/New_York", # http://worldtimeapi.org/timezones
    'github_token' : 'fawfj23rakjnfawiefa',
    'hackaday_token' : 'h4xx0rs3kret',
    }
```

2. You have to install the [`adafruit_esp32spi`](https://circuitpython.readthedocs.io/projects/neopixel/en/latest/) libary to for the nessesary libary support. 
