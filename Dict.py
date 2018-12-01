#Dictionaries :

#Dictinaries will have data which is packed and of key value pair 

purse = dict()  #assign purse variable as of dict. type

purse['Money'] = 100

purse['Scent'] = 23

purse ['chokey'] = 11
#print the dict
print(purse)

#print a particular value
print(purse['chokey'])


#TO find a key whether present in python 


print('chokey' in purse)

#will return true or false 


#Explains the Get Method in python Deict 


longName = dict()

nj = ['india','srilanka','bangladesh','india','srilanka','china','srilanka']

for names in nj:
	longName[names] = longName.get(names,0) + 1  #This code which check wther the "names" is present in the dict. if so will return the value or else will take the default value given in the second argument 
print (longName)