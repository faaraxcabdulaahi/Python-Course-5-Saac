# Casharkii lasoo qaatay baa inta la isku keenu waxaa laga samaynayaa logic.

# Logicu waxaa weeye isticmaalaha ama userka waxaan waydiinaynaa magaciisa iyo lambarkiisa sirtaa (password) kadibna waxaan usheegaynaa passwordkiisa inta xaraf uu ka koobanyahay.

"1= Creating 2 input variables"
magaca = input('Geli magacaaga: ')
sirta = input('Geli lambarkaaga sirtaa: ')

"2= Printing the 2 variables"
# print(f'Asc, magacaagu waa, ' + magaca + 'sidoo kale lambarkaaga sirta ah inta xaraf ee uu ka koobanyahay waa ' + len(sirta) + 'oo xaraf ah') 
print(' ')
# Hadaad print garaysid error baad la kulmaysaa, marka suaashu waa sidee lagu xalin karaa. 

#Sidaan waan ku xalin karnaa, sidoo kalana f string waan adeegsan karnaa.

"Sidee loo qariyaa passwordka lasoo daabacayo"
#1= Samaynta variable hidden_password la yiraahdo
hidden_password = '*' * len(sirta) 

#2= Samaynta variable labaad oo len_pass la yiraahdo
len_pass = len(sirta)

print(f'Asc, magacaygu waa {magaca} sidoo kale lambarkayga sirta waa \n🔒{hidden_password} \n🔑waxaana uu ka kooban yahay lambarkaaga sirtu {(len_pass)} oo xaraf')