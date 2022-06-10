# create func that return age after providing year of birth
from datetime import date


def age_of_person(year_of_birth):
    return date.today().year - year_of_birth


age_of_person(1700)
age_of_person(2020)
age_of_person(1988)
'''
from datetime import date
def age_of_person():
    year_of_birth = int(input('What is the year of your birthday? '))
    current_year = date.today().year
    person_date = current_year - year_of_birth
    return person_date  
age_of_person()
'''
