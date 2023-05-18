ticket = input('Enter ticket number: ')
if int(ticket[0] + ticket[1] + ticket[2]) == int(ticket[3] + ticket[4] + ticket[5]):
    print('Your have lucky ticket')
else:
    print('Try again')