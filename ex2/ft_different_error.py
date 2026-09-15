def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int('abc')
    elif operation_number == 1:
        _ = 5 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        print("Hola" + 10)


def test_error_types() -> None:
    i: int = 0
    while i <= 4:
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed seccessfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError:{e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        i += 1
    print()
    print("All error types tested successfully!")


def ft_differents_errors() -> None:
    print("=== Garden Error Types Demo ===")
    test_error_types()


if __name__ == "__main__":
    ft_differents_errors()
