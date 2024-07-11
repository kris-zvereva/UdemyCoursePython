def divide(dividend, divisor):
    return dividend / divisor


print("mymodule.py:", __name__)
# __name__ is a global variable which allows to differentiate between the file you run and a file you import

# -- importing from a folder --

import libs.mylib

print("mymodule.py:", __name__)