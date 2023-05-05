sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!."
sentence_replace = sentence.replace("!"," ", 8)
final_sentence = sentence_replace.replace("!","")
print(final_sentence)
#The task wanted me to replace every ! with a space and gave an example of what should be printed.
#But the example isn't what would happen if you replaced every ! with a space. 
#So I replaced every ! with a space for the first 8, then set another replace function to remove the final !.
#I'd imagen this could be done in one line without having to set a new varible, but I couldn't workout how.
#I also set the final_sentence valriable so that i could use an upper() function on it and reverse it, wasn't sure how to do this without setting a new variable.
print(final_sentence.upper())
print(final_sentence[43::-1])