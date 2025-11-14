import tkinter as tk
from tkinter import messagebox
from D5538Y_weather import get_weather_data, format_weather_response, D5538Y_get_random_city


class D5538YWeatherApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("D5538Y Weather App")
        self.root.geometry("450x350")
        self.setup_ui()

    def setup_ui(self):


        title_label = tk.Label(self.root, text="D5538Y Weather Application", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)


        city_frame = tk.Frame(self.root)
        city_frame.pack(pady=10)

        tk.Label(city_frame, text="Enter city:").pack(side=tk.LEFT)
        self.city_entry = tk.Entry(city_frame, width=20)
        self.city_entry.pack(side=tk.LEFT, padx=5)
        self.city_entry.bind("<Return>", lambda event: self.get_weather())

        # Gombok frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)

        # Get Weather gomb
        self.get_weather_btn = tk.Button(button_frame, text="Get Weather", command=self.get_weather)
        self.get_weather_btn.pack(side=tk.LEFT, padx=5)

        # Random City gomb
        self.random_btn = tk.Button(button_frame, text="Random City", command=self.get_random_weather)
        self.random_btn.pack(side=tk.LEFT, padx=5)

        # Eredmény megjelenítése
        result_frame = tk.Frame(self.root)
        result_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        tk.Label(result_frame, text="Weather Results:", font=("Arial", 10, "bold")).pack(anchor=tk.W)
        self.result_text = tk.Text(result_frame, height=10, width=50)
        self.result_text.pack(fill=tk.BOTH, expand=True, pady=5)

        # Clear gomb
        clear_btn = tk.Button(self.root, text="Clear Results", command=self.clear_results)
        clear_btn.pack(pady=5)

    def get_weather(self):
        city = self.city_entry.get().strip()

        if not city:
            messagebox.showwarning("Warning", "Please enter a city name!")
            return

        self._display_weather_data(city)

    def get_random_weather(self):
        random_city = D5538Y_get_random_city()
        self.city_entry.delete(0, tk.END)
        self.city_entry.insert(0, random_city)
        self._display_weather_data(random_city)

    def _display_weather_data(self, city):
        try:
            weather_data = get_weather_data(city)
            result = f"Weather in {city}:\n{format_weather_response(weather_data)}"
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result)

            self._apply_text_colors(weather_data['condition'])

        except Exception as e:
            messagebox.showerror("Error", f"Failed to get weather data: {str(e)}")

    def _apply_text_colors(self, condition):
        """Színes formázás az időjárási állapot alapján"""
        self.result_text.tag_configure("sunny", foreground="orange", font=("Arial", 10, "bold"))
        self.result_text.tag_configure("rainy", foreground="blue", font=("Arial", 10, "bold"))
        self.result_text.tag_configure("cloudy", foreground="gray", font=("Arial", 10, "bold"))
        self.result_text.tag_configure("hot", foreground="red", font=("Arial", 10, "bold"))
        self.result_text.tag_configure("clear", foreground="green", font=("Arial", 10, "bold"))

        condition_lower = condition.lower()
        if "sunny" in condition_lower:
            self.result_text.tag_add("sunny", "1.0", "end")
        elif "rain" in condition_lower:
            self.result_text.tag_add("rainy", "1.0", "end")
        elif "cloud" in condition_lower:
            self.result_text.tag_add("cloudy", "1.0", "end")
        elif "hot" in condition_lower:
            self.result_text.tag_add("hot", "1.0", "end")
        elif "clear" in condition_lower:
            self.result_text.tag_add("clear", "1.0", "end")

    def clear_results(self):
        """Eseménykezelő: eredmények törlése"""
        self.result_text.delete(1.0, tk.END)
        self.city_entry.delete(0, tk.END)

    def run(self):
        """Elindítja az alkalmazást"""
        self.root.mainloop()


if __name__ == "__main__":
    app = D5538YWeatherApp()
    app.run()