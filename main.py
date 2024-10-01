print('Welcome to the tip calculator!')
total = float(input('What is your total bill? $ '))
percent = int(input('How much tip would you like to give? 10, 12, or 15? '))
people_amount = int(input('How many people to split the bill? '))

percent_per_person = ((total / people_amount) * percent) / 100
total_to_pay_per_person = round(total / people_amount + percent_per_person, 2)

print(f'Each person should pay: {total_to_pay_per_person}')

