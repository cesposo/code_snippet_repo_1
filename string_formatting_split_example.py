def solution(s):
    # Exception clause
    if len(s)==0:
        return []
    
    return_list = []
    n = len(s)
    if n%2==0:
        for i in range(0,int(n),2):
            return_list.append(s[i:i+2])
        return return_list
    if n%2==1:
        for j in range(0, int(n)+1,2):
            if j==len(s)-1:
                return_list.append(s[j]+"_")
                return return_list
            return_list.append(s[j:j+2])