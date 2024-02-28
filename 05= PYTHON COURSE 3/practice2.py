print('welcome to distance converter program')
while True:
   choice =input('(MI) for miles, (KM) for kilometers & (q) for Quit: ').lower()
   if choice == 'q': # Halkaan waxaan niri hadii ay choice lamid noqoto 'q' jooji. 
       break  # Jooji (breaktaan) baan ka wadaa
   elif choice == 'mi':
       km = int(input('Enter the kilometers: '))
       mi = km / 1.609
       print(f'{km} kilometers is {mi} miles')
   elif choice == 'km':
       mi = int(input('Enter the miles: '))
       km = mi * 1.609
       print(f'{mi} miles is {km} kilometers')