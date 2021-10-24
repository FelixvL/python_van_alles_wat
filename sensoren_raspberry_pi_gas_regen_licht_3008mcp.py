import busio
import digitalio
import board
import time
from datetime import datetime
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import json

def append_to_json(meting):
    # data laden
    with open('test.json') as file:
        data = json.load(file)

    print(type(data))
    #meting = {"Hello":"World"}
    data.append(meting)

    # data schrijven
    with open('test.json', 'w') as file:
        json.dump(data, file, indent=4, sort_keys=True)

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

cs = digitalio.DigitalInOut(board.D24)

mcp = MCP.MCP3008(spi, cs)

locatie = "Eindhoven"

regen = AnalogIn(mcp, MCP.P0)
gas = AnalogIn(mcp, MCP.P1)
licht = AnalogIn(mcp, MCP.P2)

count = 0
while True:
    demeting = dict()
    print(regen.value)
    print(gas.value)
    print(licht.value)
    print("\n") 
    now = datetime.now()
    now = now.strftime("%d/%m/%Y %H:%M")
    print("\n")
    time.sleep(2)
    count = count + 1    
    demeting["regen"] = regen.value
    demeting["gas"] = gas.value
    demeting["licht"] = licht.value 
    demeting["locatie"] = locatie
    demeting["tijdstip"] = now
    demeting["id"] = int(time.time())
    append_to_json(demeting)
    if count == 5:
        break

print("klaar")
