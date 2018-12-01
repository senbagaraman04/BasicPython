#10.2 Write a program to read through the mbox-short.txt and figure out the distribution
#by hour of the day for each of the messages. You can pull the hour out from the 'From '
#line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.



name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
line2 = list()

for line in handle:
    if line.startswith("From "):
		line = line.split()
		line2.append(line[5])
#Prints the list of mails
line2.sort() #List are sorted
#print(line2)

#line2 = string.split(':')[0]
#print("splitting.....")
line3 = list()

for i in line2:
    line3.append(i.split(':')[0])

dic = dict()

for i in line3:
    dic[i] = dic.get(i,0)+1

for x,y in dic.items():
    print(x,y)
#Now to split it based on hours.


