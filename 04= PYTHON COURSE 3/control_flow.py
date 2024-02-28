#📝CONTROL FLOW :
# 👉 Control flow laba ayuu uqaybsamaa
# 1=Conditional statements
# 2= Loops

#-----------------------
#1=Conditional Statement
#-----------------------

#🚀Conditional statements waxaa weeye in go'aamo la samayn karo marka xaalad hebel dhacdo. Tusaale ; Waa adoo yiri haday waxaan dhacaan, waxaan samee oo kale. 


    #a) If statement (Waa hadii baa laga wada)   
    #TRUE IF
x = 10
if x > 7:
    print('x is greater than 7')
    
# Marka halkaan waxaan iri hadii x 7 ka waynaato, waxaad daabacdaa, x waxaa ay ka wayntahay 7. 

#If waxaa ay shaqaysaa hadii xaaladu ay noqoto TRUE. 

# CALAAMADAHA OPERATERSKA IYO MACNAYAASHOODA QAYBKAMIDA
#👉1) > greater than
#👉2) < less than
#👉3) >= greater than or equal to
#👉4) == equal to
#👉5) != Not equal to

        #FALSE IF
y = 9
if y == 10:
    print("y is equal to 9")
    # Halkaan waxba lama soo daabacayo, waa y iyo 9 isma le'eka.
    
    # Midna ogoow shuruuda ku xiran <if> in lasoo daabaco, if waa inay TRUE tahay. 


    #b) The elif statement (Micnaheedu waa hadii kale sidaan)
    
# 👉 elif waxaa laga wadaa mida hore haday false noqoto, if kale adigoo sameeyay camal weeye. 

# elif waxaa loo adeegsadaa hadii <if> ta koowaad ay TRUE noqon waydo. 

y = 34

if y < 7:
    print('y is less than 7')
elif y > 10:
    print('y is greater than 7') # elif waxaa ay ku xirantahay, in if ta koowaad ay false noqoto. 
    
    
    #c)Else (micnaheedu waa wixii kasoo haray)
    
#👉 Else condition dhan ma check garayso, oo micnaheedu waxaa weeye wixii kasoo hara.

y = 34

if y < 7:
    print('y is less than 7')
elif y == 10:
    print('y is equal to 7')
else:
    print('y is greater than 7') # Tan si loo soo daabaco wixii ka horeeya waa inay FALSE noqdaan. 
    
# CONDITIONAL STATEMENT MAXAAN KA FAHANAY :

#👉Shayga 1aad;
#🚀1)if => Inay checking ku samaynayso xaalad(condition)

#🚀2)elif => Inay checking ku samaynayso xaalad(condition)

#🚀3)else => Inay waxba checking garaynayn



#👉Shayga 2aad;
#🚀1)if => Waxaa ay qusaysaa xaalada(condition) ay checking ku samaynayso hadii ay true noqoto. Kadib haday true noqoto hawshaa la fulinayaa.

#🚀2) elif => waxaa ay qusaysaa xaalada ay checkinka ku samaynayso inay TRUE noqoto, Sidoo kalana <if> ta ka horaysa ay false noqoto. 

#🚀3) else => Iyadoo kuli waa inay false noqdaan, marka iyada xaalad(condition) la checking garaynayo ma jirto. 

# THE LECTURE EXAMPLE
number = int(input('Enter the number: '))
if number < 0 :
    print(number, 'is negative')
elif number == 0 :
    print('This number is zero')
else:
    print(number, 'is positive')