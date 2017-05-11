def namelist(names):
    name_list = []; return_str = ""
    
    #Exception clauses 
    if len(names)==0:
        return ""
    
    if len(names)==1:
        return_str = str(names[0]['name'])
        return return_str
    
    for index in range(len(names)):
        name_list.append(str(names[index]['name']))
        
    for index in range(len(name_list)):
        if index == len(name_list)-1:
            return_str = return_str[:len(return_str)-2]
            return_str += " & "+ name_list[index]
            return return_str
        
        return_str += name_list[index] + ", "