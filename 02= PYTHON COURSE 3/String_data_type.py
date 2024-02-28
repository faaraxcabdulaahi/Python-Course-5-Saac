#String => Waa xarafyo isla xiriiro kuwaas oo lagu soo xiro kolmo(Quotes)

"1) String concatenating"
# String concatenating waxaa laga wadaa markaad laba erey isku daraysid. Waayo string sidaan horay ugu soo qeexnay waa 'Text' (Qoraal).

#Hadaan si faahfaahiyo waa laba qoraal oo isku dhajiyay

# '🫡Tusaalaha 1aad'
# magaca_hore = 'Faarax'
# magaca_labaad= 'Cabdulaahi'
# magaca_saddexaad = 'cali'
# print('Magacayga oo dhamaystiran waa ' +  magaca_hore  + magaca_labaad  + magaca_saddexaad)
# print(' ')


'🫡Tusaalaha 2aad'
magaca = input("Magacaagu waa: ")
dada = input("Da'daadu waa: ")
print('Magacaagu waa ' + magaca + ", Sidoo kale da'daadu waa " + dada)
print(' ')


"2= Accessing characters in a string"
# Waxaa laga wadaa xuruuf kamida galitaankooda. 

'Habka koowaad ee loo access garaynkaro string'
name = "Programmer" # Tusaale waxaan rabaa Xarafka 'P' ee qoraalkaas ugu horeeya. Waxaad samaynaysaa 👇:
xaraf = name[0] # Indexing baa loo yaqaan, markaad xaraf rabtid in laguu daabaco
xarafka = name[-1] # Waxaa lasoo daabacayaa xarafka ugu dambeeya ee "r" ah
print(xarafka) # Waxaa lasoo daabacayaa P, sida aad ujeedidba.


'Hab ka labaad ee loo access garayn karo string'
print(name[0]) # habkaan waa loo ogaan karaa, xarafka ugu horeeye

print(name[-1]) 
# xarafkaas xarafka ka horeeya <-2> baad adeegsan

'''
----------------
SHARAXAAD YARA :
----------------
👉 Marka programminka la joogo xarafka ugu horeeya, waxaa weeye <0> zero, xarafka ku xiga waa < 1 >, kan ku xiga waa <2>.

👉 Tusaale hada <"Programmer">, <P> waa <0> (Eber) oo waa xarafka ugu horeeya, <r> waa <1> oo waa xarafka labaad. 

Waxaan rajaynayaa inaad fahantay. 
'''
# Waxaan rajaynayaa in la fahmay

"3= Slicing a string"
# Slicing waxaa laga wadaa in ereyga lasoo daabacoo xaraf laga soo bilaabo ilaa xaraf kale laga gaaro. 
# Tusaale : Magaca faarax, baan waxaa leeyahay waxaad iisoo daabacdaa (xarafka <f> laga bilaabo ilaa <r>)

# Waxaa dhacaya ayaa waxaa uu yahay waxaa lasoo daabacaya xarafka lagu bilaabay ee <f> laakiin lama soo daabacayo xarafka loogu dambaysiiyay ee <r> , waxaa lagu joojinayaa xarfaka <a>. Waxaa outputka soo baxaya ayaa waxaa uu noqon <faa>, sababta xarafka looga reebay python waa in la waydiiyaa. 😶

# Isku soo duubo xaraf laga bilaabo ilaa xarf kale ayaa {slicing} la dhahaa.
magacayga = "Faarax"
print(magacayga[0:4])
print(' ')
'''
👉 Meeshaan kore waxaa ka dhacay, in iri waxaad iisoo daabacdaa laga soo bilaabo xaraka <f> oo 0 (Eber) utaagan ilaa xaraf <a> ee saddexaad ee xarafka <r> ka dambeeyay, xarafkaas oo utaagan <4>.

👉 Waxaa lasoo daaabacay xarafka <f> ilaa <r>, iyadoona python ay dhagaha ka furaysatay inay kusoo darto xarafka <a> ee ka dambeeya <r>
'''

nums = '12345678910'
print(nums[1::2]) # Halkaan waxaa lasoo daaabacayaa iyadoo laba labo laga boodayo.
print(' ')

"4= f-string (formatting string)"
# f-string, waxaa ay qabataa shaqada concatenationka ee pluska (+) iyadoo la adeegsanaya la isku daro, micnaha isku darka laba shay waxayna u qabataa hab yaroo fudud. 
Magaca = input('Magaca: ')
Wadanka = input('Wadanka: ')
print(f'Magacaygu waa {Magaca} waxaana ku dhashay miyga duleedka xarfo {Wadanka}')