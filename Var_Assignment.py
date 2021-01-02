text_file = 'D:\\MyScripts\\2021_100DOC\\VarSearch.txt'
string_to_find = 'hidden'

with open(text_file, 'rb') as f:
    text = f.read()
    if string_to_find in f:
        found_string = string_to_find
        print(found_string)

# What are you even trying to achieve here?
    