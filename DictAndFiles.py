#Counting 

lis = list()

dic = dict()

inp = input("Enter a line:")

lis = inp.split()

for i in lis:
	dic[i] = dic.get(i,0)+1

	
print (dic)


#Input and Output

#   Enter a line:we are going to a movie oginght. the movie will be soo goof. are we ready to go?                         
#    {'the': 1, 'goof.': 1, 'we': 2, 'to': 2, 'ready': 1, 'a': 1, 'going': 1, 'go?': 1, 'soo': 1, 'are': 2, 'be': 1, 'oging
#    ht.': 1, 'will': 1, 'movie': 2} 