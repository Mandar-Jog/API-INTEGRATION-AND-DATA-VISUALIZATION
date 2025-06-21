import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Replace with your OpenWeatherMap API key
API_KEY = "1794f4940d5c9d45e91c00429ceb344e"  # Replace with your actual API key

def get_coordinates(city):
    """Fetch latitude and longitude for a city using the Geocoding API."""
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    response = requests.get(geo_url)
    print(f"Geocoding Status: {response.status_code}")
    print(f"Geocoding Response: {response.text}")
    data = response.json()
    if data:
        return data[0]["lat"], data[0]["lon"]
    else:
        raise ValueError(f"City '{city}' not found.")

def get_weather_data(lat, lon, use_one_call=False):
    """Fetch weather data using Current Weather Data API or One Call API 3.0."""
    if use_one_call:
        weather_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=current,minutely,daily,alerts&units=metric&appid={API_KEY}"
    else:
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"
    response = requests.get(weather_url)
    print(f"Weather Status: {response.status_code}")
    print(f"Weather Response: {response.text}")
    data = response.json()
    if response.status_code == 200:
        if use_one_call and "hourly" in data:
            return data["hourly"]
        else:
            return [{"dt": data["dt"], "temp": data["main"]["temp"], "humidity": data["main"]["humidity"]}]
    else:
        raise ValueError(f"Error fetching weather data: {data.get('message', 'Unknown issue')}")

def process_data(weather_data):
    """Process weather data into a pandas DataFrame."""
    times = [datetime.fromtimestamp(item["dt"]) for item in weather_data]
    temps = [item["temp"] for item in weather_data]
    humidity = [item["humidity"] for item in weather_data]
    df = pd.DataFrame({"Time": times, "Temperature (°C)": temps, "Humidity (%)": humidity})
    print("DataFrame Contents:")
    print(df)
    return df

def plot_bar(df, city):
    """Plot temperature and humidity as a bar chart using Matplotlib."""
    plt.figure(figsize=(8, 6))
    bar_width = 0.35
    index = range(len(df))
    plt.bar([i - bar_width/2 for i in index], df["Temperature (°C)"], bar_width, label="Temperature (°C)", color="orange")
    plt.bar([i + bar_width/2 for i in index], df["Humidity (%)"], bar_width, label="Humidity (%)", color="blue")
    plt.title(f"Weather in {city}")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.xticks(index, df["Time"].dt.strftime("%Y-%m-%d %H:%M"), rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("weather_bar.png")
    plt.show()

def plot_heatmap(df, city):
    """Plot a correlation heatmap using Seaborn."""
    plt.figure(figsize=(8, 6))
    corr = df[["Temperature (°C)", "Humidity (%)"]].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
    plt.title(f"Correlation Heatmap for Weather in {city}")
    plt.savefig("weather_heatmap.png")
    plt.show()

def main():
    try:
        city = input("Enter city name (e.g., Tokyo): ")
        lat, lon = get_coordinates(city)
        # Set use_one_call=True if you have access to One Call API 3.0, else False
        weather_data = get_weather_data(lat, lon, use_one_call=False)
        df = process_data(weather_data)
        if not df.empty:
            plot_bar(df, city)
            plot_heatmap(df, city)
            print("Visualizations saved as 'weather_bar.png' and 'weather_heatmap.png'.")
        else:
            print("Error: No data to plot.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()