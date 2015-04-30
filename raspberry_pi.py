import json
import time
import raspy.sensors as sensors
import raspy.output as output
import subprocess

class Car(object):
    def __init__(self, port):
        self.motor = output.Motor(port)

    def drive(self, wait):
        self.motor.on()
        time.sleep(wait)
        self.motor.off()

def getUser(prev):
    with open('commands.json') as json_data:
        d = json.loads(json_data.read())
        json_data.close()
    data = d['command']
    text = d['text']
    if d['run'] and not prev:
        prev = True
        d['run'] = False
        test = open('commands.json', 'w')
        test.write(json.dumps(d))
        test.close()
    elif not d['run']:
        prev = False
    return (prev, data, text)

led = output.LED(16)
car = Car(18)
light = sensors.Light(12)
on = False

try:
    prev = False
    while True:
        commands = getUser(prev)
        if not commands[0]:
            user = ""
        else:
            user = commands[1]
            led.off()
        if user == "drive":
            car.drive(1.2)
        elif user == "morse":
            led.transToMorse(commands[2])
        elif user == "sense":
            if light.isLight():
                led.off()
            else:
                led.on()
        elif user == "shutdown":
            subprocess.call("sudo halt", shell=True)
        else:
            if on:
                led.off()
                on = False
            else:
                led.on()
                on = True
        time.sleep(0.2)
except KeyboardInterrupt:
    pass
