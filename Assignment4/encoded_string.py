"""
File: encoded_string.py
Margariete Malenda
CS106a Spring 2023
Due May 15th
-----------------------
This program expands strings encoded with run-length encoding.
"""


def expand_encoded_string(encoded):
    """
    This function is passed a run-length encoded string and
    returns the expanded version of that string.
    >>> expand_encoded_string('B4')
    'BBBB'
    >>> expand_encoded_string('m1e2t1')
    'meet'
    >>> expand_encoded_string('B1o2k2e2p1e1r1!3')
    'Bookkeeper!!!'
    """
    letters=""
    nums=""

    for i in range (0,len(encoded)):
        #first get the numbers from the encoded string
        if i%2 != 0:
            nums=nums+(encoded[i])
            #now get the letters from the encoded string
        else:
            letters=letters+(encoded[i])

    #now set up a variable for the new word
    new_word="'"

    for i in range (0, len(letters)):
        #for each value in the nums string, turn the numbers into integers and use this to append letters
        k = (int(nums[i]))
        #append the letters according to the number of values we have
        while k > 0:
            new_word=new_word + letters[i]
            k = k-1

    new_word=new_word + "'"
    print(new_word)


# Remove this line and write your code here


def main():
    result = expand_encoded_string('B4')
    #print(result)      # should print: BBBB

    #result = expand_encoded_string('m1e2t1')
    #print(result)      # should print: meet

    #result = expand_encoded_string('B1o2k2e2p1e1r1!3')
    #print(result)      # should print: Bookkeeper!!!


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
