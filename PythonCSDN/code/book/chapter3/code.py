#list and tuple
order_ending = ('st','nd','rd') + ('th',) * 17 + ('st','nd','rd') + ('th',) * 7 + ('st',)
print(order_ending)
day = input('Input a date(1-31): ')
print(day + order_ending[int(day) -1])