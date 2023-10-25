# Write a Python program that demonstrates exception chaining. Create a custom exception class called CustomError and another called SpecificError. In your program (could contain any logic you want), raise a SpecificError, and then catch it in a try/except block, re-raise it as a CustomError with the original exception as the cause. Display both the custom error message and the original exception message.
class CustomError(Exception):
    pass


class SpecificError(Exception):
    pass


try:
    raise SpecificError("Это специфическая ошибка.")

except SpecificError as specific_error:
    try:
        raise CustomError("Произошла пользовательская ошибка.") from specific_error

    except CustomError as custom_error:
        print("Сообщение пользовательской ошибки:", custom_error)
        print("Сообщение исходного исключения:", custom_error.__cause__)
