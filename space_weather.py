import requests
import pandas as pd
import matplotlib.pyplot as plt

# NOAA Space Weather Data API (Real-Time)
NOAA_URL = "https://services.swpc.noaa.gov/json/solar_cycle_prediction.json"

def fetch_solar_data():
    """Fetches real-time solar activity data from NOAA."""
    response = requests.get(NOAA_URL)
    
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        print("Failed to fetch data")
        return None

def plot_solar_activity(df):
    """Plots the solar cycle prediction."""
    plt.figure(figsize=(10, 5))
    plt.plot(df["time-tag"], df["predicted_ssn"], label="Predicted Sunspot Number", color="red")
    plt.xlabel("Year")
    plt.ylabel("Sunspot Number")
    plt.title("Solar Cycle Prediction")
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

def main():
    df = fetch_solar_data()
    
    if df is not None:
        print(df.head())
        plot_solar_activity(df)

if __name__ == "__main__":
    main()
