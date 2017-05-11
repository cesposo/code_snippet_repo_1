def find_it(seq):
    count = []; final_list = []
    for i in set(seq):
        count.append([seq.count(i),i])

    final_list = [count[j] for j in range(len(count)) if count[j][0]%2==1]
    
    return final_list[0][1]