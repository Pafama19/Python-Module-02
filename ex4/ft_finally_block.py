class GardenError (Exception):
    def __init__(self, message: str) -> None:
        if message:
            self.message = message
        else:
            self.message = "Unknown garden error"


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        if message:
            super().__init__(message)
        else:
            super().__init__("Unknown plant error")


def water_plant(plant: str) -> None:
    if plant == plant.capitalize():
        print(f"Watering {plant}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant}'")


def test_watering_system() -> None:
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        return
    finally:
        print("Closing watering system")
    print()
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
        print()
        print("Cleanup always happens, even with errors!")
    print("Esta línea no debería verse")


def main() -> None:
    print("=== Garden Watering System ===")
    print()
    test_watering_system()


if __name__ == "__main__":
    main()
