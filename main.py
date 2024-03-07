my_num = int(input('Enter your num: '))

day = my_num//60//60//24
hour = my_num//60//60%24
min = my_num//60%60
sec = my_num%60

word = True

if my_num > 8640000:
  print('Error! Too big a number!')
else:
  if day % 10 == 1 and day != 11:
    word = 'день'
  elif day % 10 in (2,3,4) and day not in (12, 13, 14):
    word = 'дні'
  else:
    word = 'днів'
    result = (f"{day} {word}, {hour:02}:{min:02}:{sec:02}")
    print(result)
