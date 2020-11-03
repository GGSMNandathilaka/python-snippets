def execute_dictionary():
    customer = {
        "name": "Shehan Nandathilaka",
        "age": 30,
        "is_verified": True
    }

    print(customer["name"])
    print(customer.get("birth_date", "March 7 1991"))
    print(customer)


def telephone_number_in_words():
    digits = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight"
    }
    phone_no = input("Enter phone no : ")

    phone_str = ""
    for n in phone_no:
        phone_str += " " + digits.get(int(n), "!")
    print(phone_str)


if __name__ == '__main__':
    telephone_number_in_words()
