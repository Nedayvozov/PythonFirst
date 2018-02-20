def get_age(year_of_birth):
    return 2018 - year_of_birth


user_year_of_birth = int(input('What year was you born?'))

print(f"You are {get_age(user_year_of_birth)} years old.")

# test