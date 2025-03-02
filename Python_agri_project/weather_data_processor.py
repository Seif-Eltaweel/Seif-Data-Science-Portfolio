import pandas as pd
import logging

class WeatherDataProcessor:
    def __init__(self, config_params):
        self.config_params = config_params
        self.weather_df = None
        logging.info("WeatherDataProcessor")

    def process(self):
        # Example: Load weather data from CSV
        self.weather_df = pd.read_csv(self.config_params["weather_csv_path"])
        logging.info("Weather data processed")
    