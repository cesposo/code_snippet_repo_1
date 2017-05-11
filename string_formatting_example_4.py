def mix(s1, s2):
    # your code
    lower_case_string = "abcdefghijklmnopqrstuvwxyz"
    s1_count = []; s2_count = []
    return_string = []; ret_string = ""
    
    if len(s1)==0 and len(s2)==0:
        return ""
    
    s1_count = [[i, s1.count(i)] for i in lower_case_string] 
    s2_count = [[i, s2.count(i)] for i in lower_case_string]
    
    for j in range(len(s1_count)):
        if s1_count[j][1] > s2_count[j][1] and s1_count[j][1] >= 2:
            return_string.append("1:"+s1_count[j][0]*s1_count[j][1]+"/")
        elif s1_count[j][1] < s2_count[j][1] and s2_count[j][1] >= 2:
            return_string.append("2:"+s2_count[j][0]*s2_count[j][1]+"/")
        elif s1_count[j][1] == s2_count[j][1] and s1_count[j][1] >= 2 and s2_count[j][1] >= 2:
            return_string.append("=:"+s1_count[j][0]*s1_count[j][1]+"/")
            
    return_string.sort()
    return_string.sort(key=len, reverse=True)    
    ret_string = str("".join(return_string)[:-1])
            
    return ret_string