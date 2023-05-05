#Asking for sentence input.
sentence = str(input("Please enter your sentance.\n"))

#running through string, turning every even index lower case and odd upper, then printing.
result = ""
for idx in range(len(sentence)):
    if idx % 2:
        result = result + sentence[idx].lower()
    else:
        result = result + sentence[idx].upper()
print("\nThis is you sentence with every other character uppercase and all other characters lowercase.\n" + result)

# spliting sentance at every space, turning evey even word lower case and odd upper.
split_sentance = sentence.split(" ")
letter_storage = ""
letter = 1   
for i in split_sentance:
    if letter != 1:
        letter_storage += " "  #adding space back between words as we spit on spaces
    if letter % 2 == 0:        
        letter_storage += i.lower()
    else:
        letter_storage += i.upper()
    letter += 1
print("\nThis is you sentence with every other word uppercase and all other word lowercase.\n" + letter_storage)
 

    



