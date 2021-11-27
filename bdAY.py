birth_year = input('What is your birth year : ')
print(birth_year)

birth_age = input('What is your current age : ')
print(birth_age)

if float(birth_year) + float(birth_age) == 2021:
    print('Then Your Birthday Is gone')
elif float(birth_year) + float(birth_age) == 2020:
    print('In this year you will have your birthday')
else:
    print("Check your values!!!!")
