#1=TYPE CONVERSION
'''
👉 Type conversion waxaa laga wadaa markaad data type aad ubadalaysid data type kale. Tusaale ; <Integer> baad waxaad ubadalaysaa <float>.
'''
num1 = input('Number 1: ')
num2 = input('Number 1: ')
print( 'Jawaabtu waa: ', num1 + num2 )# Halkaan waxaa la sameeyay string concatenating, oo micnaha laba string baa la isku daba qabtay.

# Micanaha waxaa uu ka dhigayaa laba xaraf oo la isku darayo.

print(' lamabaro sidii xuruufihii la isugu darayo')
print(' ')
 


"XALINTA CILADA LAMBARADA OO SIDA XURUUFTA LA ISKU DARAYO"
# Si ciladaas loo xaliyo waa in shayga horey <Constructor keyword laga soo geliyaa>, halkaan 
number1 = int(input('Number 1: '))
number2 = int(input('Number 1: '))
print('Jawaabtu waa :', number1 + number2)  # Hada maadaama labadaan integer loo badalay, labada tiro caadi buu isugu darayaa. 
print(' ')

'👇 Fiirinta labadaas typekooda'
print(type(number1),type(number2))
print(' ') # Printigaan waxaa u adeegsanayaa si codedka space ugu sameeyo. 

"""
🚀 Mid waa inaad ogataa, taasoo ah in wax kasta aanan <Type Conversion> aanan laga dhigi karin, Tusaale {string integer uma badali kartid}, hadaad falkaas isku daydidna (error) baad la kulmaysaa.  

"""


#2=KNOWING TYPE OF THE FUNCTION
'''waxaa jira built in(micnaha function python ku dhex dhisan weeye), functionkaas waxaa la yiraahdaa <Type() function. >'''
# print(type(num1),type(num2))

age = 34
Type = type(str(age))
print(Type)