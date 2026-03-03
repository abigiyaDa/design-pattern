# Step 1: Define the Observer Interface
class Observer:
    def update(self, temperature):
        pass

# Step 2: Define the Subject
class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = None

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def _notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature):
        self._temperature = temperature
        self._notify_observers()

# Step 3: Create Concrete Observers

class PhoneDisplay(Observer):
    def update(self, temperature):
        print(f"Phone display updated: {temperature}°C")

class WindowDisplay(Observer):
    def update(self, temperature):
        print(f"Window display updated: {temperature}°C")

# Step 4: Use the WeatherStation and Observers
if __name__ == "__main__":
    weather_station = WeatherStation()

    phone_display = PhoneDisplay()
    window_display = WindowDisplay()

    weather_station.register_observer(phone_display)
    weather_station.register_observer(window_display)

    weather_station.set_temperature(25)
    weather_station.set_temperature(30)

    weather_station.remove_observer(phone_display)
    weather_station.set_temperature(28)