# Given names and phone numbers, assemble a phone book that maps friends' names 
#to their respective phone numbers. You will then be given an unknown number of 
#names to query your phone book for. For name each queried, print the associated entry 
#from your phone book on a new line in the form name=phoneNumber; if an entry for name
#is not found, print Not found instead.



# Read input and assemble Phone Book
n = int(raw_input())
phonebook = dict(raw_input().split() for _ in range(n))

for k,v in phonebook.iteritems():
    contact = raw_input() # make queries
    if contact in phonebook:
        print contact+"="+phonebook[contact]
    else:
        print "Not found"
