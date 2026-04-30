from datetime import datetime, timezone
from fastapi import FastAPI

app = FastAPI()

@app.get("/date")
def get_date():
    now = datetime.now(timezone.utc)
    return {
        "iso_utc": now.isoformat(),
        
        "unix": now.timestamp()
    }
    
"""
vbox:

	Your code is a FastAPI application definition, not a standalone long-running server. Running it with python3 	your_file.py only loads the module and exits, so nothing stays alive in the background.
	To keep it running until you stop it, start it with an ASGI server such as uvicorn.

		python3 -m pip install fastapi uvicorn

	    nohup python3 -m uvicorn my_first_api:app --host 0.0.0.0 --port 8000 > fastapi.log 2>&1 &

WSL:
	curl http://192.168.0.153:8000/date
"""
