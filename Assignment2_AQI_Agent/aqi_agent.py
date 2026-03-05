import csv

def calculate_aqi(pm25):
    if pm25 <= 50:
        return "Good"
    elif pm25 <= 100:
        return "Moderate"
    elif pm25 <= 150:
        return "Unhealthy for Sensitive Groups"
    elif pm25 <= 200:
        return "Unhealthy"
    elif pm25 <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"

def reflex_agent(file):
    with open(file, 'r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            pm25 = float(row['pm25'])
            pm10 = float(row['pm10'])

            aqi = calculate_aqi(pm25)

            print("PM2.5:", pm25)
            print("PM10:", pm10)
            print("AQI Level:", aqi)
            print("-------------------")

if __name__ == "__main__":
    reflex_agent("pollution_data.csv")