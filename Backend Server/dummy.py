from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse
import asyncio
import subprocess
from pydantic import BaseModel
import uvicorn
from pymodbus.client import ModbusSerialClient as ModbusClient
import serial

app = FastAPI()

@app.get("/data")
async def process_data():

    data = {
        "Solar Panel Current": '7.2 A',
        "Load Current": '3.5 A',
        "Grid Current": '2.6 A'
    }

    #return {"message": "No connection established"}
    return {"message": data}

@app.post("/MaxCurrent/{value}")
async def modify_max(value: int):
    
    #return {"message": "Max Charging Current modification failed: No connection established"}
    return {"message": "Max Charging Current Modified Successfully"}
    #return {"message": "Max Charging Current Modification failed"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


