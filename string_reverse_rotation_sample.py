def revrot(strng, sz):
    # your code
    print(strng)
    print(sz)
    return_string = ""
    temp_string = ""
    # Exceptions 
    if sz <= 0 or len(strng)==0 or (sz > len(strng)):
        return ""
    for i in range(0,int(len(strng)),sz):
        temp_string = strng[i:i+sz]
        if len(temp_string) != sz:
            return return_string
        else:
            num_list = [int(i)**3 for i in temp_string]
            if sum(num_list)%2==0:
                for j in range(len(temp_string)):
                    return_string += temp_string[len(temp_string)-1-j]
                    
            else:
                for k in range(len(temp_string)):
                    return_string += temp_string[(k+1)%(len(temp_string))]
                
    return return_string