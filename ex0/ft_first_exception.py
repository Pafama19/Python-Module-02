def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    value1: str = "25"
    print(f"Input data is '{value1}'")
    try:
        temp_int = input_temperature(value1)
        print(f"Temperature is now {temp_int}ºC")
    except ValueError as e:
        print("Caught input_temperature error: ", end="")
        print(f"{e}")
    print()
    value2: str = "abc"
    print(f"input data is '{value2}'")
    try:
        temp_int = input_temperature(value2)
        print(f"Temperature is now {temp_int}ºC")
    except ValueError as e:
        print("Caught input_temperature error: ", end="")
        print(f"{e}")
    print()
    print("All tests completed - program didn't crash!")


def ft_first_exception() -> None:
    print("=== Garden Temperature ===")
    print()
    test_temperature()


if __name__ == "__main__":
    ft_first_exception()
