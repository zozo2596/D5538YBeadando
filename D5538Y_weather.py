import random


def get_weather_data(city):

    try:
        mock_data = {
            "Budapest": {"temperature": 22, "condition": "Sunny", "humidity": 65},
            "London": {"temperature": 15, "condition": "Cloudy", "humidity": 80},
            "New York": {"temperature": 18, "condition": "Rainy", "humidity": 75},
            "Berlin": {"temperature": 16, "condition": "Partly Cloudy", "humidity": 70},
            "Paris": {"temperature": 17, "condition": "Rainy", "humidity": 78},
            "Tokyo": {"temperature": 20, "condition": "Sunny", "humidity": 60},
            "Sydney": {"temperature": 25, "condition": "Clear", "humidity": 55},
            "Rome": {"temperature": 19, "condition": "Sunny", "humidity": 68},
            "Madrid": {"temperature": 24, "condition": "Hot", "humidity": 45},
            "Prague": {"temperature": 14, "condition": "Cloudy", "humidity": 72}
        }

        return mock_data.get(city, {"temperature": "N/A", "condition": "Unknown", "humidity": "N/A"})
    except Exception as e:
        return {"temperature": "Error", "condition": "Error", "humidity": "Error"}


def format_weather_response(data):

    return f"Temperature: {data['temperature']}°C\nCondition: {data['condition']}\nHumidity: {data['humidity']}%"


def display_weather_info(city, data):

    print(f"Weather in {city}:")
    print(format_weather_response(data))


def D5538Y_get_random_city():

    cities = ["Budapest", "London", "New York", "Berlin", "Paris",
              "Tokyo", "Sydney", "Rome", "Madrid", "Prague"]
    return random.choice(cities)



if __name__ == "__main__":
    random_city = D5538Y_get_random_city()
    print(f"Random város: {random_city}")
    data = get_weather_data(random_city)
    display_weather_info(random_city, data)