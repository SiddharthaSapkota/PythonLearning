age = input("what is your current age in year?: ")

age_in_int = int(age)

month_in_year = 12 
weeks_in_year = 52
days_in_year = 365

year_remaining = 90-age_in_int
month_remaining = year_remaining *month_in_year
week_remaining = year_remaining*weeks_in_year
days_remaining = year_remaining*days_in_year

print(f"You have {days_remaining} days, {week_remaining} weeks, and {month_remaining} months left ")
