import requests, json, datetime, Adafruit_DHT, time

# Read configuration from config.json
with open('config.json', 'r') as f:
    config = json.load(f)

# Configuration to read sensor 
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = config["DHT_PIN"]

while True:
    # Get a reading
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        measurements = { 
                        "device": config["device"],
                        "dateTime": datetime.datetime.now().isoformat(),
                        "temperature": temperature,
                        "humidity": humidity
                    }
    else:
        print("["+datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S")+"] Failed to retrieve data from sensor")

    try:
        # Send measurement to API
        resp = requests.post(config["rpi-measurements-api"]+'/TempAndHum', json=measurements)
        if resp.status_code != 200:
            print("["+datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S")+"] Temperature ={0:0.1f}*C, Humidity={1:0.1f}% - ERROR sending data to API".format(temperature, humidity))
        else: 
            print("["+datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S")+"] Temperature ={0:0.1f}*C, Humidity={1:0.1f}% - Successfully sent to API".format(temperature, humidity))

    except requests.exceptions.RequestException as e:
        print("["+datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S")+"] Temperature ={0:0.1f}*C, Humidity={1:0.1f}% - ERROR connecting to API".format(temperature, humidity))

    time.sleep(60/config["frequency"])




