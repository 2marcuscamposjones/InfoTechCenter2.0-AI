import random
from time import sleep

class GasolineBranch:
    GAS_LEVELS = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    GAS_STATIONS = ["Shell", "Speedway", "Marathon", "Circle K", "Mobil", "Costco", "Meijer", "7Eleven"]

    @staticmethod
    def gas_level_gauge():
        return random.choice(GasolineBranch.GAS_LEVELS)

    @staticmethod
    def list_of_gas_stations():
        return random.choice(GasolineBranch.GAS_STATIONS)

    @staticmethod
    def gas_level_alert():
        gas_level = GasolineBranch.gas_level_gauge()
        if gas_level == "Empty":
            print("***WARNING - YOU ARE ON EMPTY***")
            sleep(1.25)
            print("Calling Triple AAA")
        elif gas_level == "Low":
            print("Your gas tank is extremely low, checking Google Maps for the closest gas stations.")
            sleep(1.25)
            print(f"The closest gas station is {GasolineBranch.list_of_gas_stations()} which is {round(random.uniform(1, 25), 1)} miles away.")
        elif gas_level == "Quarter Tank":
            print("Your gas tank is on a quarter tank, checking Google Maps for the closest gas stations.")
            sleep(1.25)
            print(f"The closest gas station is {GasolineBranch.list_of_gas_stations()} which is {round(random.uniform(25.1, 50), 1)} miles away.")
        elif gas_level == "Half Tank":
            print("Your gas tank is half full which is plenty to get to your destination.")
        elif gas_level == "Three Quarter Tank":
            print("Your gas tank is three quarter full.")
        else:
            print("Your gas tank is full.")

if __name__ == "__main__":
    print("******************************************************")
    print("Gasoline Branch\n\n")
    GasolineBranch.gas_level_alert()
