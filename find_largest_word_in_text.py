def largest_word(text):
    words = text.split()
    
    max_length = 0
    for word in words:
        # print(len(word))
        if len(word) > max_length:
            max_length = len(word)
            # print(max_length) # output: 11
    
    print('The longest words is: \n')
    for word in words:
        if len(word) == max_length:
            print(f"{word}, {max_length} letters")
        
largest_word('Programming in Python is very interesting')