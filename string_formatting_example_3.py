def likes(names):
    #your code here
    if len(names)==0:
        return "no one likes this"
    if len(names) >= 4:
        return_string = names[0]+", "+names[1]+" and "+str(len(names)-2)+" others like this"
        return return_string
    if len(names) == 2:
        return_string = names[0]+" and "+names[1]+" like this"
        return return_string
    if len(names) == 1:
        return_string = names[0]+" likes this"
        return return_string
    if len(names) == 3:
        return_string = names[0]+", "+names[1]+" and "+names[2]+" like this"
        return return_string
        