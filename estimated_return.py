import time
def selection():
#main selection.
    text = (
        '1 - Estimated Return of S&P500 ETFs\n'
        '2 - Estimated Return of Turkish ISB ETFs: '
    )
    while True:
        choice_str = input(text)
        try:
            choice_int = int(choice_str)
            if choice_int in (1,2):
                return choice_int
            else:
                print('Please Select 1 or 2, other options are not available.')
        except ValueError:
            print('Invalid value, please input a number(1 or 2).')

user_option = selection()

def calculation(initial, monthlyIncrease, duration, rate):
    rateMultiplier = 1 + rate/12/100
    for i in range(duration*12):
        initial = initial * rateMultiplier
        initial = initial + monthlyIncrease
    return initial

if user_option == 1:
    print('Processing Estimated Return...')
    time.sleep(0.5)
    initial = int(input('Initial Money Before Investment Period: '))
    monthlyIncrease = int(input('How Much Money Will You Add Each Month?: '))
    duration = int(input('How Many Years Are You Going to Invest?: '))
    calculation(initial, monthlyIncrease, duration, 8.6)
    print(f'You will earn {calculation(initial, monthlyIncrease, duration, 8.6):.2f} USD in {duration:.1f} years.({duration*12:.0f} months)')
    pass
elif user_option == 2:
    print('Processing...')
    time.sleep(0.5)
    initial = int(input('Initial Money Before Investment Period: '))
    monthlyIncrease = int(input('How Much Money Will You Add Each Month?: '))
    duration = int(input('How Many Years Are You Going to Invest?: '))
    rate = int(input('What is the Estimated Increment Rate of ETF per Year: '))
    calculation(initial, monthlyIncrease, duration, rate)
    print(f'You will earn {calculation(initial, monthlyIncrease, duration, rate):.2f} TL in {duration:.1f} years.({duration*12:.0f} months)')
    pass    
