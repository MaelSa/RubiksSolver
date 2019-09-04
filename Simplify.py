def determine_nb_move(L):
    '''Renvoie le nombre de tours que ce mouvement nécessite réellement'''
    nb_move = 1
    if L[0]=="'":
        nb_move=3
    elif L[0]=="2":
        nb_move=2
    return(nb_move)

def simplify(list_move):
    '''Retourne une liste de coups optimisée d'une liste de mouvements'''
    arg = 0
    num_move = 0
    list_possibilités_move=["","2","'"]
    while arg!=len(list_move):
        nb_coups = determine_nb_move(list_move[num_move])
        i=1
        while len(list_move)>num_move+i and list_move[num_move+i][-1] == list_move[num_move][-1]:
            nb_coups+=determine_nb_move(list_move[num_move+i])
            i+=1
        list_move_end=list_move[num_move+i:]
        list_move_start = list_move[:num_move]
        nb_coups_final = nb_coups%4
        arg = len(list_move_start)
        if nb_coups_final == 0:
            list_move = list_move_start + list_move_end
        else:
            list_move = list_move_start +[list_possibilités_move[nb_coups_final-1]+list_move[num_move][-1]]+ list_move_end
            arg +=1
            num_move+=1
    return(list_move)