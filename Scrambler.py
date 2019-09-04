from fonctions_deplacement import *
import random
List_mvt_str = ["R", "L", "U", "D", "F", "B"]
List_add = ["'", "2", ""]


def chek(a , a_ant , a_list):
    is_ok = False
    if a != a_ant:
        is_ok = True
    a_cycle = a//2
    if is_ok:
        if a_cycle == a_list[0]:
            if a_list[1]<2:
                a_list[1] += 1
            else:
                is_ok = False
        else:
            a_list[0] = a_cycle
            a_list[1] = 0
    return(is_ok , a_list)


def generate_scramble():

    list_scramble = []
    a_ant = 42
    a_list = [42,0]

    for i in range(20):

        b = random.randint(0,2)
        mvt = List_add[b]
        is_ok = False

        while not is_ok:
            a = random.randint(0,5)
            is_ok , a_list = chek(a,a_ant,a_list)
        a_ant = a

        mvt += List_mvt_str[a]
        list_scramble.append(mvt)

    return(list_scramble)


def execute_move(list_scramble, arretes, coins,centres):
    '''A partir d'une liste de chaine de caractères contenant des mouvements de cube, on applique ces mouvements dans l'ordre a la liste arretes et coins '''
    for i in list_scramble:
        a = 1
        for j in i:
            if j == "'":
                a = 3
            elif j == '2':
                a = 2

            if j == "R":
                for u in range(0,a):
                    arretes, coins = right(arretes, coins)

            elif j == "L":
                for u in range(0,a):
                    arretes, coins = left(arretes, coins)

            elif j == "U":
                for u in range(0, a):
                    arretes, coins = up(arretes, coins)
            elif j == "D":
                for u in range(0,a):
                    arretes, coins = down(arretes, coins)
            elif j == "F":
                for u in range(0,a):
                    arretes, coins = front(arretes, coins)
            elif j == "B":
                for u in range(0,a):
                    arretes, coins = back(arretes, coins)
            elif j == "M":
                for u in range(0,a):
                    arretes, centres = middle(arretes, centres)
            elif j == "E":
                for u in range(0,a):
                    arretes, centrs = equator(arretes, centres)
    return arretes, coins,centres


def ajust_scramble(list_internet):
    '''list_internet est une chaine de caractère que l'on transforme afin de pouvoir lui appliquer execute_scramble'''
    list_internet = list_internet.split(" ")
    true_list = []
    for i in list_internet:
        if len(i) == 2:
            element = i[1]+i[0]
            true_list += [element]
        if len(i) == 1:
            element = i[0]
            true_list += [element]
    return(true_list)


def readable_scramble(list_scramble):
    '''renvoie une chaine de caractère lisible d'une liste d'un mélange'''
    readable_list = ''
    for i in list_scramble:
        if len(i) == 1:
            readable_list += str(i) + ' '
        if  len(i) == 2:
            element = str(i[1]) + str(i[0]) + ' '
            readable_list += element
    return(readable_list)

