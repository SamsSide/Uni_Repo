k = int(input("Date after: "))
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
years = k // 360
days = k % 360
months = days // 30
days = days - (months * 30)
year = year + years
day = day + days
if day > 30:
    newMonths = day // 30
    day = day - (newMonths * 30)
    months = months + newMonths
month = month + months
if month > 12:
    year = year + (month // 12)
    month = months % 12
print(day,month,year)
