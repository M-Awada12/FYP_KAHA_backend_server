from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse
import asyncio
import subprocess
from pydantic import BaseModel
import uvicorn
#import serial

app = FastAPI()

'''

global_count = 0 
last_sent_count = None 

async def generate_event():
    global global_count, last_sent_count
    while True:
        if last_sent_count != global_count:
            event_data = f"{global_count}\n\n"
            yield event_data
            last_sent_count = global_count
        await asyncio.sleep(1)

@app.get("/getCurrent")
async def get_events():
    events = generate_event()
    return StreamingResponse(events, media_type="text/event-stream")

@app.get("/increment")
async def get_events():
     global global_count
     global_count = global_count + 1
     return global_count

@app.post("/execute_command")
async def execute_command():
    # Execute your Python command here
    result = subprocess.run(["your_python_command_here"], capture_output=True)
    return {"output": result.stdout.decode(), "error": result.stderr.decode()}

'''
#ser =serial.Serial('dev/ttyUSB0', 2400)

@app.get("/getCurrent")
async def get_events():
    # ser.write('QDI'.encode())
    # response = ser.readline().decode
    # charg_curr = int(response[6:8])
    # return {'message': charg_curr}
    print('Get Charging Current Sent Successfully')
    return {"message": "3.27 A"}

@app.post("/data")
async def process_data():
    print('Data Received Successfully')
    return {"message": "Data Received Successfully"}

@app.post("/MaxCurrent")
async def process_data():
    # command to modify the max charging current
    print('Max Charging Current Modified Successfully')
    return {"message": "Max Charging Current Modified Successfully"}

#ser.close

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 
