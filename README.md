# ☀️ Interactive Weather Application ☔

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Vue.js](https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white)](https://vuejs.org/)
[![Weather API](https://img.shields.io/badge/Weather_API-00BFFF?style=for-the-badge&logo=weather&logoColor=white)](https://www.weatherapi.com/)

> **Meteora** is an immersive weather application that brings weather data to life with stunning animations and intuitive design. Experience weather forecasts with dynamic backgrounds and visual effects that change based on current conditions.

## ✨ Features

- 🔍 **Location Search**: Find weather information for any city worldwide
- 🌦️ **Current Weather**: Display current temperature, condition, and key weather metrics
- 📅 **3-Day Forecast**: See upcoming weather conditions for planning ahead
- 🎨 **Dynamic Themes**: Background and animations change based on current weather
- ⏰ **Real-time Clock**: Displays current time
- 📱 **Responsive Design**: Works seamlessly on both mobile and desktop devices
- ✨ **Weather Animations**: Unique visual effects for different weather conditions:
  - Sunny, cloudy, rainy, snowy, and stormy animations
  - Day/night visual changes

## 📱 Responsive Design

Meteora adapts beautifully to any device:

- Desktop: Full-featured experience with detailed animations
- Tablet: Optimized layout with preserved animations
- Mobile: Streamlined interface focused on essential weather data

![Responsive Design](https://github.com/Divyajeet7978/Weather-App/blob/main/images/ss.png)

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Node.js (optional for development)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/meteora-weather.git
   cd meteora-weather
   ```

2. **Install backend dependencies**
   ```bash
   pip install fastapi uvicorn httpx pydantic jinja2
   ```

3. **Install frontend dependencies (optional for development)**
   ```bash
   npm install particles.js three
   ```

4. **Start the server**
   ```bash
   uvicorn app:app --reload
   ```

5. **Access the application**
   
   Open your browser and navigate to: [http://localhost:8000](http://localhost:8000)

## 🔧 Technical Architecture

### Backend

Built with FastAPI, the backend provides:
- RESTful API endpoints
- Asynchronous weather data retrieval
- Error handling and data validation
- Proxy service to WeatherAPI.com

```python
# Core API endpoint for weather data
@app.post("/api/weather")
async def get_weather(location: LocationRequest):
    # Access weather data for the requested location
    # Process and return formatted weather information
```

### Frontend

The Vue.js frontend delivers:
- Reactive UI with the Composition API
- Dynamic CSS animations and transitions
- Weather-based background and animation changes
- Mobile-responsive design using modern CSS techniques

```javascript
// Weather animation creation
const createWeatherAnimation = (condition) => {
    // Generate weather-specific animations
    // Apply dynamic visual effects based on conditions
}
```

## 🎨 Weather Themes

Meteora features unique themes for different weather conditions:

| Weather | Theme | Animation |
|---------|-------|-----------|
| 🌞 Sunny | Warm gradient | Animated sun with rays |
| ☁️ Cloudy | Cool blue gradient | Floating clouds |
| 🌧️ Rainy | Deep blue gradient | Falling raindrops |
| ❄️ Snowy | Light blue gradient | Falling snowflakes |
| ⚡ Stormy | Dark gradient | Lightning flashes |
| 🌙 Clear Night | Dark purple gradient | Twinkling stars |

## 🔄 API Reference

### Get Weather Data

```http
POST /api/weather
Content-Type: application/json

{
  "query": "London"
}
```

**Response:**
```json
{
  "location": {
    "name": "London",
    "region": "City of London, Greater London",
    "country": "United Kingdom"
  },
  "current": {
    "temp_c": 18.0,
    "condition": {
      "text": "Partly cloudy",
      "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png"
    },
    "humidity": 72,
    "wind_kph": 14.4
  },
  "forecast": [...]
}
```

### Get Current Time

```http
GET /api/time
```

**Response:**
```json
{
  "time": "2025-04-27T15:30:45.123456"
}
```

## 🛠️ Customization

### Adding New Weather Animations

Extend the `createWeatherAnimation` function in the frontend code:

```javascript
// Add a new weather animation
if (condition.includes('Tornado')) {
    // Create tornado animation elements
    const tornado = document.createElement('div');
    tornado.className = 'tornado';
    // Add styling and animation properties
    weatherAnimation.value.appendChild(tornado);
}
```

### Modifying Weather Themes

Update the CSS variables in the `:root` section:

```css
:root {
    /* Add or modify weather gradients */
    --tornado: linear-gradient(135deg, #392e4a, #5e5086);
}
```

## 📦 Deployment

### Docker

```bash
# Build the Docker image
docker build -t meteora-weather-app .

# Run the container
docker run -p 8000:8000 meteora-weather-app
```

### Cloud Platforms

Deploy to popular cloud platforms:

- **Heroku**: Use the included Procfile
- **Vercel**: Set up serverless functions for the API
- **AWS**: Deploy with Elastic Beanstalk or Lambda functions

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

