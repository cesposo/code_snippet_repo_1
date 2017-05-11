import re

def to_camel_case(text):
    #your code here
    return_list = []
    if text == "":
        return ""
    return_list = re.split("-|_", text)
            
    return_list1 = [return_list[word][0].upper()+return_list[word][1:] for word in range(1,len(return_list))]
    return_string = return_list[0]+"".join([words for words in return_list1])
    return return_string 