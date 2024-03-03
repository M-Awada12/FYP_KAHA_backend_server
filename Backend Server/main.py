from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse
import asyncio
import subprocess
from pydantic import BaseModel
import uvicorn
from pymodbus.client import ModbusSerialClient as ModbusClient
import serial

app = FastAPI()

@app.post("/data")
async def process_data():
    client = ModbusClient(method='rtu', port='/dev/ttyUSB0', baudrate=9600, timeout=1)
    if not client.connect():
        print("connection failed")
        return {"message": "No connection established"}
    else:
        print("connection established")

    SOLAR_PANEL_CURRENT_REGISTER = 0x0000
    LOAD_CURRENT_REGISTER = 0x0001
    GRID_CURRENT_REGISTER = 0x0002

    solar_panel_current = client.read_holding_registers(SOLAR_PANEL_CURRENT_REGISTER, 1).registers[0]
    load_current = client.read_holding_registers(LOAD_CURRENT_REGISTER, 1).registers[0]
    grid_current = client.read_holding_registers(GRID_CURRENT_REGISTER, 1).registers[0]

    print(f"Solar Panel Current: {solar_panel_current}")
    print(f"Load Current: {load_current}")
    print(f"Grid Current: {grid_current}")
    data = {
        "Solar Panel Current": solar_panel_current,
        "Load Current": load_current,
        "Grid Current": grid_current
    }

    client.close()
    print('Data Sent Successfully')
    return {"message": data}

@app.post("/MaxCurrent/{value}")
async def modify_max(value: int):
    client = ModbusClient(method='rtu', port='/dev/ttyUSB0', baudrate=9600, timeout=1)
    if not client.connect():
        print("connection failed")
        return {"message": "Max Charging Current modification failed: No connection established"}
    else:
        print("connection established")

    response = client.write_register(210, value=value, slave=1)

    if not response.isError():
        client.close()
        print('Max Charging Current Modified Successfully')
        return {"message": "Max Charging Current Modified Successfully"}
    else:
        client.close()
        print('Max Charging Current Modification failed')
        return {"message": "Max Charging Current Modification failed"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


