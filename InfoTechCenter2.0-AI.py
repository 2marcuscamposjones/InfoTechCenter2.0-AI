import random
from time import sleep


class GasolineBranch:
    # Define lists for gas levels and gas stations
    GAS_LEVELS = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    GAS_STATIONS = ["Shell", "Speedway", "Marathon", "Circle K", "Mobil", "Costco", "Meijer", "7Eleven"]

    @staticmethod
    def gas_level_gauge():
        # Randomly select a gas level
        return random.choice(GasolineBranch.GAS_LEVELS)

    @staticmethod
    def list_of_gas_stations():
        # Randomly select a gas station
        return random.choice(GasolineBranch.GAS_STATIONS)

    @staticmethod
    def gas_level_alert():
        # Get the current gas level
        gas_level = GasolineBranch.gas_level_gauge()

        # Check gas level and provide appropriate message
        if gas_level == "Empty":
            # Warn user and suggest calling AAA
            print("***WARNING - YOU ARE ON EMPTY***")
            sleep(1.25)
            print("Calling Triple AAA")
        elif gas_level == "Low":
            # Inform user about low gas level and nearest gas station
            print("Your gas tank is extremely low, checking Google Maps for the closest gas stations.")
            sleep(1.25)
            print(
                f"The closest gas station is {GasolineBranch.list_of_gas_stations()} which is {round(random.uniform(1, 25), 1)} miles away.")
        elif gas_level == "Quarter Tank":
            # Inform user about quarter tank gas level and nearest gas station
            print("Your gas tank is on a quarter tank, checking Google Maps for the closest gas stations.")
            sleep(1.25)
            print(
                f"The closest gas station is {GasolineBranch.list_of_gas_stations()} which is {round(random.uniform(25.1, 50), 1)} miles away.")
        elif gas_level == "Half Tank":
            # Inform user about half tank gas level
            print("Your gas tank is half full which is plenty to get to your destination.")
        elif gas_level == "Three Quarter Tank":
            # Inform user about three quarter tank gas level
            print("Your gas tank is three quarter full.")
        else:
            # Inform user about full tank gas level
            print("Your gas tank is full.")


if __name__ == "__main__":
    # Print header
    print("******************************************************")
    print("Gasoline Branch\n\n")

    # Call the gas level alert function
    GasolineBranch.gas_level_alert()
