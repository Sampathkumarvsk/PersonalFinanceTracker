from datetime import datetime

CATEGORIES = {"I":"Income","E":"Expense"}

def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime("%d-%m-%Y")
    try:
        valid_date = datetime.strptime(date_str,"%d-%m-%Y")
        return valid_date
    except ValueError:
        print("Invalid Date format, Re-Enter ")
        return get_date()

def get_amount():
    try:
        amount = float(input("Enter the value"))
        if amount <= 0:
            raise ValueError("Not the valid number")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()


def get_category():
    categorys = input("Enter the Category ('I' for income or 'E' for Expense)").upper()
    if categorys in CATEGORIES:
        return CATEGORIES[categorys]
    
    print("Invalid Category. Please Enter I or E")
    return get_category()


def get_description():
    description = input("Enter the description")
    return description

