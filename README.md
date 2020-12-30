# rpi-send-DHT22
Send measurements made with a DHT 22 humidity and temperature sensor from Raspberry Pi to rpi-measurements-api

# Configuration

Create a `config.json` file with the below contents
```
{
    "device":"<name of your device which is taking the measurements>",
    "rpi-measurements-api":"http://<url to the API>:<port - optional>",
    "DHT_PIN": <GPIO pin number>,
    "frequency" : 1
}
```

GPIO pin number is not the same as physical pin. For example physical pin 3 corresponds to GPIO pin 2. Read more about this in [Rasberry Pi's official documentation](https://www.raspberrypi.org/documentation/usage/gpio/README.md)

With the `frequency` parameter you can define how many times in a minute a reading should be attempted. So if it set to 1 it will attempt 1 reading every minute, if it is set to 3 it will attempt a reading every 20 seconds (so 3 in a minute). After each reading the measurements is attempted to be sent to the API and logged in the console.

Example
```
{
    "device":"raspberrypizero",
    "rpi-measurements-api":"http://raspberrypi:8650",
    "DHT_PIN": 2,
    "frequency" : 3
}
```

# Running the script
```
python3 rpi-send-dht22.py
```

The script will run continuously until it is terminated.