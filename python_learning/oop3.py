def uniq(list):
    """ 
    Returns unique values of a list 
    """
    u_list = []
    for item in list:
        if item not in u_list:
            u_list.append(item)
    return u_list
horsemen =['war','famine','death','pestilence']
i = 0;
num = len(horsemen)
while i < num:
    print (horsemen[i])
    i+=1