from datetime import date, datetime

today = date.today()

print('Welcome to the Age Calculator!')
given_date = date.fromisoformat(
    input('Please provide the date (yyyy-mm-dd) that you wish to calculate the age for: '))

print('Age is:', int((today-given_date).days / 365), 'year(s)')

# NB: this is for format yyyy-mm-dd
# In order to make this work in format dd-mm-yyyy, we have to reformat the string which can be done using .strptime()
# E.g. date = 01-01-1990 would be formatted as:
# formatted_date = datetime.strptime(date, "%d-%m-%Y") -> this would make formatted_date be in the yyyy-mm-dd format
