# Randomizer biorący Imię i losujący mu osobę do kupienia prezentu na mikołajki
import random
import time
import pyperclip as clip


def its_random_i_swear():
    otpt = (10 * '*') + '|LISTA|' + (10 * '*')
    santas = []
    elves = int(input('Ile osób bierze udział?:'))
    for x in range(elves):
        santas.append(input('Dodaj Mikołaja #' + str(len(santas)+1) + ':'))
    parents = santas.copy()
    good_kids_r = []
    while parents:
        z = random.choice(parents)
        good_kids_r.append(z)
        if good_kids_r[len(good_kids_r)-1] == santas[len(good_kids_r)-1]:
            good_kids_r.remove(z)
        elif good_kids_r[len(good_kids_r)-1] == 'Dorota' or good_kids_r[len(good_kids_r)-1] == 'Gadom':
            if santas[len(good_kids_r)-1] == 'Dorota' or santas[len(good_kids_r)-1] == 'Gadom':
                good_kids_r.remove(z)
            else:
                parents.remove(z)
        else:
            parents.remove(z)

    relation = dict(zip(santas, good_kids_r))
    for mikus in relation:
        otpt = otpt + '\n' + str(mikus) + ' kupuje prezent ' + str(relation[mikus])
    otpt = otpt + '\n' + (27*'*')
    print('\n' + otpt)
    clip.copy(otpt)
    time.sleep(30)


its_random_i_swear()
