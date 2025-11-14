def D5538Y_celsius_to_fahrenheit(celsius):

    return (celsius * 9/5) + 32

def D5538Y_validate_city_name(city):

    if not city or not isinstance(city, str):
        return False
    return city.replace(" ", "").isalpha()

def D5538Y_calculate_feels_like(temp, humidity):

    # Egyszerű számítás (nem pontos meteorológiai formula)
    if temp > 20:
        return temp + (humidity / 100) * 2
    else:
        return temp - (humidity / 100)