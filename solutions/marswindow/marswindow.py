startm = 4
year = int(input())

difyear = year-2018
difmonth = difyear*12 - startm
print(difmonth)
difmonth %= 26


if year == 2018:
    print('yes')
elif difmonth <= 11:
    print('yes')
else:
    print('no')
