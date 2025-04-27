from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import httpx
from pydantic import BaseModel
import datetime
import os

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (if you have any)
app.mount("/static", StaticFiles(directory="static"), name="static")

API_KEY = "62eb481e9e884e48bb6122848252704"
BASE_URL = "http://api.weatherapi.com/v1"

class LocationRequest(BaseModel):
    query: str

@app.get("/")
async def serve_frontend():
    # Serve the index.html file
    return FileResponse('index.html')

@app.post("/api/weather")
async def get_weather(location: LocationRequest):
    try:
        async with httpx.AsyncClient() as client:
            # Get current weather
            current_url = f"{BASE_URL}/current.json?key={API_KEY}&q={location.query}&aqi=no"
            current_response = await client.get(current_url)
            current_response.raise_for_status()
            current_data = current_response.json()
            
            # Get forecast
            forecast_url = f"{BASE_URL}/forecast.json?key={API_KEY}&q={location.query}&days=3&aqi=no&alerts=no"
            forecast_response = await client.get(forecast_url)
            forecast_response.raise_for_status()
            forecast_data = forecast_response.json()
            
            # Process data
            processed_data = {
                "location": current_data["location"],
                "current": current_data["current"],
                "forecast": forecast_data["forecast"]["forecastday"]
            }
            
            return processed_data
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail="Weather API error")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/time")
async def get_current_time():
    return {"time": datetime.datetime.now().isoformat()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)