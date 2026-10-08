def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    if temp_int < 0:
        raise Exception(f"{temp_int}ºC is too cold for plants (min 0ºc)")
    elif temp_int > 40:
        raise Exception(f"{temp_int}ºC is too hot for plants (max 40ºC)")
    return temp_int


def test_temperature() -> None:
    print("=== Graden Temperature Checker ===")
    print()
    value1: str = "25"
    print(f"Input data is '{value1}'")
    try:
        temp = input_temperature(value1)
        print(f"Temperature is now {temp}ºC")
    except ValueError as e:
        print("Caught input_temperature error: ")
        print(f"{e}")
    print()
    value2: str = "abc"
    print(f"Input data is '{value2}'")
    try:
        temp = input_temperature(value2)
        print(f"Temperature is now {temp}ºC")
    except ValueError as e:
        print("Caught input_temperature error: ", end="")
        print(f"{e}")
    print()
    value3: str = "100"
    print(f"Input data is '{value3}'")
    try:
        temp = input_temperature(value3)
        print(f"Temperature is now {temp}ºC")
    except Exception as e:
        print("Caught input_temperature error: ", end="")
        print(f"{e}")
    print()
    value4: str = "-50"
    print(f"Input data is '{value4}'")
    try:
        temp = input_temperature(value4)
        print(f"Temperature is now {temp}ºC")
    except Exception as e:
        print("Caught input_temperature error: ", end="")
        print(f"{e}")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
