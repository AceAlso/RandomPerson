#Randomizer biorący Imię i losujący mu osobę do kupienia prezentu na mikołajki
import random, time, pyperclip as clip

def Its_Random_I_Swear():
    OTPT = (10 * '*') + '|LISTA|' + (10 * '*')
    Santas = []
    Parents = []
    Elves = int(input('Ile osób bierze udział?:'))
    for x in range(Elves):
        Santas.append(input('Dodaj Mikołaja #' + str(len(Santas)+1) +':'))
    Parents = Santas.copy()
    GoodKidsR = []
    z = None
    while Parents != []:
        z = random.choice(Parents)
        GoodKidsR.append(z)
        if GoodKidsR[len(GoodKidsR)-1] == Santas[len(GoodKidsR)-1]:
            GoodKidsR.remove(z)
        elif GoodKidsR[len(GoodKidsR)-1] == 'Dorota' or GoodKidsR[len(GoodKidsR)-1] == 'Gadom':
            if Santas[len(GoodKidsR)-1] == 'Dorota' or Santas[len(GoodKidsR)-1] == 'Gadom':
                GoodKidsR.remove(z)
            else:
                Parents.remove(z)
        else:
            Parents.remove(z)

    Relation = dict(zip(Santas, GoodKidsR))
    for mikus in Relation:
        OTPT = OTPT + '\n' + str(mikus) + ' kupuje prezent ' + str(Relation[mikus])
    OTPT = OTPT + '\n' + (27*'*')
    print('\n' + OTPT)
    clip.copy(OTPT)
    time.sleep(30)
Its_Random_I_Swear()
