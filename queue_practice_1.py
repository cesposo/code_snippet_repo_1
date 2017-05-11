def queue_time(customers, n):
    # TODO
    sub_list = []; tot_time = 0 ; final_list = []

    # Partitioning Procedure 
    customers_new = customers[n:]
    # Corner case exception clause 
    if n==0:
        return 0 
    if len(customers)==0:
        return 0  
    if len(customers) < n:
        return max(customers)
        
    # Initial deposit platform  
    sub_list = [customers[time] for time in range(n)]

    if n==1:
        return sum(customers)
    else:
        final_list = sub_list
        for j in range(len(customers_new)):
            final_list[final_list.index(min(final_list))] += customers_new[j]
    return max(final_list)
