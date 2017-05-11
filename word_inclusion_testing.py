def in_array(array1, array2):
    return_list = []
    for word in array1:
        for cand_word in array2:
            if word in cand_word:
                return_list.append(word)
    return_list = list(set(return_list))
    return_list.sort()
    return return_list