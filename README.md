**API INTEGRATION AND DATA VISUALIZATION**

COMPANY: CODTECH IT SOLUTIONS

NAME: MANDAR JOG

INTERN ID: CT04DF1656

DOMAIN: Python Programming

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

**TASK SUMMARY**: This Python script retrieves and visualizes weather data for a user-specified city using the OpenWeatherMap API. It begins by prompting the user to input a city name, then uses the API’s Geocoding endpoint to fetch the city’s latitude and longitude. With these coordinates, it queries either the Current Weather Data API or the One Call API 3.0 (depending on the `use_one_call` flag) to obtain weather metrics like temperature and humidity in metric units. The script processes the retrieved data into a pandas DataFrame, organizing it by timestamp, temperature, and humidity.

The script then generates two visualizations. First, it creates a bar chart using Matplotlib, displaying temperature and humidity side-by-side for each timestamp, with the x-axis showing formatted dates and times. The chart includes a legend, grid, and labels, and is saved as `weather_bar.png`. Second, it produces a correlation heatmap using Seaborn to show the relationship between temperature and humidity, saved as `weather_heatmap.png`. Both plots are displayed and tailored to the specified city.

Error handling is implemented to manage issues like invalid city names or API failures, printing descriptive error messages. The script requires an OpenWeatherMap API key and dependencies like `requests`, `pandas`, `matplotlib`, and `seaborn`. It’s designed for simplicity, assuming a single data point unless the One Call API is used, and provides a clear, visual representation of weather data for analysis.
