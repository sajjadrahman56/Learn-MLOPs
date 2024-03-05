# Exception detaiels

**Importing sys module**: The `sys` module provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter.

```python
import sys
```

**Function `error_message_detail(error, error_detail:sys)`**: This function takes two arguments, an error message and error details. It extracts the traceback information from the error details, which includes the filename where the error occurred, the line number, and the error message. It then formats this information into a string and returns it.

```python
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))
    
    return error_message
```

**Class `CustomException(Exception)`**: This is a custom exception class that inherits from the built-in Python `Exception` class.
When an instance of this class is created, it takes an error message and error details as arguments.
The `__init__` method calls the `error_message_detail` function to get a detailed error message, which is then stored as an instance variable. The `__str__` method returns this detailed error message when the exception is printed.

```python
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
```
