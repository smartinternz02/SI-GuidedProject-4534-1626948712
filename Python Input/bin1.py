import wiotp.sdk.device
import time
import json
import random
myConfig = { 
    "identity": {
        "orgId": "v34dpq",
        "typeId": "18BLC1057",
        "deviceId":"123456"
    },
    "auth": {
        "token": "123456789"
    }
}



client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()
s=0

while True:
    name="Bin 1"
    wt=int(input())
    la= 13.004999071524786
    lon= 80.24882690953538
    s=s+wt
    myData={'name':name,'weight':wt,'total':s,'lat':la,'lon':lon}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    time.sleep(5)
client.disconnect()
