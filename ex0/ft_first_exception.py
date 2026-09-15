def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("input data is '25'")
    try:
        temp_int = input_temperature("25")
        print(f"Temperature is now {temp_int}ºC")
    except ValueError as e:
        print("Caught input_temperature error: ")
        print(f"{e}")
    print()
    print("input data is 'abc'")
    try:
        temp_int = input_temperature("abc")
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
