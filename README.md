# ATM_PIN
Do atm related functions.
import time
name = input('enter a name:')
print('welcome', name, 'to sbi atm')
print('insert a card')
time.sleep(1)
pin = int(input('Please enter your pin:'))
time.sleep(1)
print('its processing......')
time.sleep(1)
print('successfully')
print('Please choose the option')
print('1.Banking\n2.Withdrawal\n3.Pin Change\n4.Balance enquiry')
