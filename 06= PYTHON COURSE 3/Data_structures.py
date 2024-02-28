# # DATA_STRUCTURES =>Waxaa weeye objects, waxaana loo adeegsadaa in lagu kaydiyo, laguna habeeyo data_memoriga. 


#-----------------
#1= LIST DATA_TYPE
#-----------------

#1)Creating a list
my_list = [1,2,3,4,5,6, 'faarax']
print(my_list)
print(' ')

#2)Accessing a list
print(my_list[0]) # The first
print('')
print(my_list[-1]) #The last
print(' ')

#3)Slicing a lists
print(my_list[0:3])
print(' ')

# # #4)Slicing and skipping by 2
# # print(my_list[1::3])
# # print(' ')


# #5)Modifying a list
# #🚀Listsku waa (Mutable) micnaha waxaa laga wadaa waxbaa laga badali karaa. 

# # lists = ['faarax','cabdulaahi','cali']
# # lists[0]='faysal' # Tirada 0 waa meesha uu yaalo shayga aan wax ka badalayo, halka 'faysal' uu yahay kan aan ku badalayo. 
# # print(lists)
# # print(' ')


# # #6)Adding something at the last 
# # lists.append('xasan') #append() waa list method. 
# # print(lists)
# # print(' ')

# #7)Removing something
# # magacyo_arday = ['faarax','yuusuf','sakariye']
# # magacyo_arday.remove('faarax') # Ogoow waxaa lagaa rabaa inaad galisid, remove() methodka shayga la rabo inaad ka saartid. 
# # print(magacyo_arday)
# # print(' ')

# #8)Creating 2D list
# matrix = [
#     [1,2,3], # Qaybtaan isla socota waxaa ay ku jirta index ahaan, 0
#     [4,5,6], # Tana 1
#     [7,8,9] # Tana 2
# ]
# print(matrix) # Printing the all list
# print(' ')

# print(matrix[0]) # Printing the list one
# print(' ')

# print(matrix[0][2]) #Halkaan waxaa laga wadaa listiga koowaad intaad dhexgashid, valuegiisa ku jira index 2 iisoo daabac. Marka saad arki doontidba waxaa lasoo daabacayaa 3 oo oo yaala index 2.
# print(' ')


# #-----------------------
# #2= DICTIONARY DATA_TYPE
# #-----------------------

# #1)Creating a dict
# Wadar = {
#     'Qof':'faarax', # Mid ogoow keygu waa 'Qof', halka 'faarax' uu yahay valuega.
#     'Dadiisa':78,
#     'magaalada':'gaalkacyo',  
# }
# print(Wadar)
# print('')
# #2)Accessing a dictionary
# print(Wadar['Qof']) #Halkaan keyga ama furaha la sheegayaa meeshii la sheegi lahaa indexka. 
# #Kan haduusan keygu jirin error buu keenayaa. Marka si aad errorka uga baxsatid waxaad adeegsataa .get() method. 
# print(' ')

# print(Wadar.get('Qofka'))# haduusan keygu jirin wax error ah masoo daabacmi mayaaan, ee waxaa soo daabacmaya, (None). 

# #Sideedaba waxaad ogaataa in hadaad doonaysid inuusan wax error ah, uusan kuu soo bixin waa markaad wax access garaynaysid waa inaad adeegsataa (get). 
# print(' ')



# #3)Modifying values
# #Tusaale dictionarigaa aan kor kusoo sameeyay magaca qofka waa faarax, marka magacaas baan rabaa inaan ka badalo. 
# Wadar['Qof']=  'Faysal'
# print(Wadar)
# print(' ')

# #4)Removing
# del Wadar['Qof']
# print(Wadar)