#create an empty dictionary
country_db = {
    "SOUTH_AFRICA":"JOHANNESBURG"
}# countries are the keys and capitals are the value
while True :
    print("1 - insert")
    print("2 - display all countries")
    print("3 - display all capitals")
    print("4 - get capital") 
    print("5 - deleting")

    choice = int(input("Enter your choice 1-5: "))

    if choice == 1:
        country = input("What country do you you want to use: ").upper()#this will be used as key
        capital = input("What is the capital of this country: ").upper()#This will be used as value
        country_db[country] = capital
        print(country_db)

    elif choice == 2:
        print(country_db.keys())

    elif choice == 3:
        print(country_db.values())

    elif choice == 4:
        country = input("What country do you want to use: ").upper()
        capital = country_db.get(country)
        print(capital)

    elif choice == 5:
        country = input("What country would you like to delete frome the data base: ").upper()
        del country_db[country]
        print(country_db)

    else:
        print("This option is not available")
        break
