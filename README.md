# D5538Y Időjárás Alkalmazás

## Hallgató: [A Hallgató Neve]

## Feladat leírása:
Ez egy egyszerű időjárás alkalmazás, amely lehetővé teszi a felhasználók számára, hogy különböző városok időjárási adatait lekérjék. Az alkalmazás grafikus felülettel rendelkezik.

## Modulok és függvények:

### D5538Y_weather.py (tanult modul)
- `get_weather_data(city)` - Időjárás adatok lekérése
- `format_weather_response(data)` - Adatok formázása
- `display_weather_info(city, data)` - Információk megjelenítése

### D5538Y_gui.py (bemutatandó modul)
- `D5538YWeatherApp` osztály - Fő alkalmazás osztály
- `setup_ui()` - Felület létrehozása
- `get_weather()` - Eseménykezelő időjárás lekéréshez
- `clear_results()` - Eredmények törlése

### D5538Y_utils.py (saját modul)
- `D5538Y_celsius_to_fahrenheit(celsius)` - Hőmérséklet átváltás
- `D5538Y_validate_city_name(city)` - Városnév validálás
- `D5538Y_calculate_feels_like(temp, humidity)` - Érzett hőmérséklet számítás

## Osztályok:
- `D5538YWeatherApp` - A fő alkalmazás osztálya, kezeli a grafikus felületet és eseménykezelést

## Telepítés és futtatás:
1. Python 3.x szükséges
2. Futtasd a `main.py` fájlt
3. Add meg a városnevet és kattints a "Get Weather" gombra

## Követelmények:
- tkinter (alapértelmezetten telepítve Pythonnal)