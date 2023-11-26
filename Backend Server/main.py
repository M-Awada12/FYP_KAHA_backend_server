from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse
import asyncio
import subprocess
from pydantic import BaseModel

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
@app.get("/getCurrent")
async def get_events():
    return {"message": "3.27 A"}

@app.post("/data")
async def process_data():
    return {"message": "Data received successfully"}

@app.post("/MaxCurrent")
async def process_data():
    return {"message": "Data received successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 
