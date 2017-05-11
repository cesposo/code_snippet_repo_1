def duplicate_count(text):
    temp_list = []; temp_list_2 = []
    for i in text.lower():
        if i not in set(temp_list):
            temp_list.append(i)
        else:
            temp_list_2.append(i)
            
    return(len(set(temp_list_2)))