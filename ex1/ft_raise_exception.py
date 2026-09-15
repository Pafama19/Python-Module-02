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
    print("Input data is '25'")
    try:
        temp = input_temperature("25")
        print(f"Temperature is now {temp}ºC")
    except ValueError as e:
        print("Caught input_temperature error: ")
        print(f"{e}")
    print()
    print("Input data is 'abc'")
    try:
        temp = input_temperature("abc")
        print(f"Temperature is now {temp}ºC")
    except ValueError as e:
        print("Caught input_temperature error: ", end="")
        print(f"{e}")
    print()
    print("Input data is '100'")
    try:
        temp = input_temperature("100")
        print(f"Temperature is now {temp}ºC")
    except Exception as e:
        print("Caught input_temperature error: ", end="")
        print(f"{e}")
        print()
    print("Input data is '-50'")
    try:
        temp = input_temperature("-50")
        print(f"Temperature is now {temp}ºC")
    except Exception as e:
        print("Caught input_temperature error: ", end="")
        print(f"{e}")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
