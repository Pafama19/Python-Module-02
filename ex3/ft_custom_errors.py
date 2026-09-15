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


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        if message:
            super().__init__(message)
        else:
            super().__init__("Unknown water error")


def ft_plant_error(plant: str) -> None:
    raise (PlantError(f"The {plant} plant is wilting!"))


def ft_water_error() -> None:
    raise (WaterError("Not enough water in the tank!"))


def ft_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        ft_plant_error("Tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()
    print("Testing WaterError...")
    try:
        ft_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()
    print("Testing catching all gardens errors...")
    try:
        ft_plant_error("Tomato")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        ft_water_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    ft_custom_errors()
