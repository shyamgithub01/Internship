try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Zero se divide nahi kar sakte!")
except ValueError:
    print("Error: Sirf numbers hi enter karo!")
finally:
    print("Thanks for using our calculator!")


# HTTPException

from fastapi import HTTPException

raise HTTPException(status_code=404, detail="Item not found")
