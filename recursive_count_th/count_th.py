'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    # if word length is less than 2, no way "th" can exist
    if len(word) < 2 :
        return False
    # first two letters th?
    elif word[0] == 't' and word [1] == 'h':
        #return true and keep going left of the 2 letters
        return 1 + count_th(word[1:]) 
    else:
        #if first letters are not 'th' keep recursing till we enter elif block
        return count_th(word[1:])

    
print(count_th("chthchth"))
