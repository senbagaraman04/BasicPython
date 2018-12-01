#Write code using find() and string slicing (see section 6.10) to extract 
#the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
text = "X-DSPAM-Confidence:    0.8475";
slic = text.find(":");
ans = text[slic+1:]
ans = ans.strip();
ans = float(ans)
print (ans)
#####################################################
#7.1 Write a program that prompts for a file name, then opens that file and reads through the file, 
#and print the contents of the file in upper case. Use the file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt

# Use words.txt as the file name
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.strip()
    print(line.upper())
	
######################################################################
#7.2 Write a program that prompts for a file name, 
#then opens that file and reads through the file, looking for lines of the form:
##X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below. 
#Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 
#when you are testing below enter mbox-short.txt as the file name.



# Use the file name mbox-short.txt as the file name
# Use the file name mbox-short.txt as the file name
average = 0
count = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    lh = line 
    pos = lh.find(":")
    number = float(lh[19:])
    average = average + number
    count = count + 1

print("Average spam confidence:",average/count)
#print("Done")
#####################################################################################################

#Open the file romeo.txt and read it line by line. 
#For each line, split the line into a list of words using the split() method. 
#The program should build a list of words. For each word on each line check to see if the 
#word is already in the list and if not append it to the list. When the program completes, 
#sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt



fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    line = line.split()
    for i in line: # observe indentation here
        if i not in lst:
            lst.append(i)
            
lst.sort() # observe indentation here.  this is where i made mistakes..
print(lst)


#8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.

#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

fname = raw_input("Enter file name: ")
fh = open(fname)
count=0
for line in fh:
    if not line.startswith("From "):
       continue
    else:
        list=line.split()
        print(list[1])
        count=count+1
      
print ("There were",count,"lines in the file with From as the first word")

#9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
#After the dictionary is produced,the program reads through the dictionary using a maximum loop to find the most prolific committer.


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
testDic = dict()
line2 = list()
for line in handle:
    if line.startswith("From "):
		line = line.split()
		line2.append(line[1])
#Prints the list of mails
#print(line2)


for mails in line2:
    testDic[mails] = testDic.get(mails,0)+1
#Prints the list of email with counts
#print (testDic)

#To check the most repeated email id 

bigKey = None 
bigValue = None

for word,count in testDic.items():
    if bigValue is None or count > bigValue:
        bigKey = word
        bigValue = count

print(bigKey,bigValue)
