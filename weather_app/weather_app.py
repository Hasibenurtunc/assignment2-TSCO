class City:

    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature


    def __str__(self):
        return f"City: {self.name}, Temperature: {self.temperature}"


class WeatherForecast:

    def __init__(self):
        self.cities = [
            City("Aydın", 15),
            City("Ankara", 3),
            City("Adana", 18)
        ]


    def add_city(self, name, temperature):
        for i in self.cities:
            if i.name.lower() == name.lower():
                print(f"{name} city has been entered before.")
                return

        new_city = City(name, temperature)
        self.cities.append(new_city)
        print(f"{new_city} city added to the list.")


    def query_city(self, name):
        for city in self.cities:
            if city.name == name:
                return city

        return f"{name} city not found on the list."


    def update_temperature(self, name, new_temperature):
        for city in self.cities:
            if city.name.lower() == name.lower():
                city.temperature = new_temperature
                return f"temperature for {name} updated to {new_temperature}."

        return f"no cities found to update."


    def advice(self, name):
        for city in self.cities:
            if city.name.lower() == name.lower():
                if city.temperature < 0:
                    return("it's cold, wear tight clothes.")
                elif city.temperature <= 15:
                    return("it's chilly, don't forget to take a coat.")
                else:
                    return("the weather is nice, dress comfortably.")

        return f"{name} city not found for advice."


    def list_cities(self):
        if not self.cities:
            return "No cities in the list."
        return "\n".join(str(city) for city in self.cities)


forecast = WeatherForecast()
print("Welcome to our weather app, select the action you want to take and enjoy.")

while True:
    print("Choose an option:\n"
          "1. Add city\n"
          "2. Query city\n"
          "3. Update temperature\n"
          "4. Get advice\n"
          "5. List all cities\n"
          "6. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        name = input("Enter city name: ")
        temp = int(input("Enter temperature: "))
        forecast.add_city(name, temp)
    elif choice == "2":
        name = input("Enter city name to query: ")
        print(forecast.query_city(name))
    elif choice == "3":
        name = input("Enter city name to update: ")
        temp = int(input("Enter new temperature: "))
        print(forecast.update_temperature(name, temp))
    elif choice == "4":
        name = input("Enter city name to get advice: ")
        print(forecast.advice(name))
    elif choice == "5":
        print("Cities in the list:")
        print(forecast.list_cities())
    elif choice == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Try again.")





