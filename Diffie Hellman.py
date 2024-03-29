def diffie():
    p = int(input("Powernum: "))
    q = int(input("Modnum: "))

    Person1 = int(input("Person1: "))
    Person2 = int(input("Person2: "))

    Person1_value = p**Person1 % q
    Person2_value = p**Person2 % q

    PERSON_1KEY = Person2_value**Person1 % q
    PERSON_2KEY = Person1_value**Person2 % q

    print(PERSON_1KEY)
    print(PERSON_2KEY)



