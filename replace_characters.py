# https://github.com/ecdegroot/replace_characters
# This python program replaces multiple characters in a word or sentence, example:
# text_input = "Intelligence is the ability to adapt to change"
# text_output = "1N73LL1G3NC3 15 7H3 4B1L17Y 70 4D4P7 70 CH4NG3"

# enter a word or sentence
input_str = input("Type someting: ")

# convert all letters to uppercase
input_str_upper = input_str.upper()

# print output with replaced letters and in uppercase.
print ( input_str_upper
        .replace ( 'I', '1' )
        .replace ( 'T', '7' )
        .replace ( 'E', '3' )
        .replace ( 'S', '5' )
        .replace ( 'A', '4' )
        .replace ( 'O', '0' )
        )
