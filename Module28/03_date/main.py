from Date_class import Date

date = Date.from_string('10-12-2078')
print(date)

date = Date.from_string('10.12.2077')

print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
