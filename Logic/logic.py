def CreateTemps(chessboard, bigVector, tempboard):                         #magiczna funkcja tworzenia tablic mozliwych ruchow
    for x in chessboard:
        tempboard.append(chessboard.gameTiles[x].pieceOnTile.toString())
    bigVector.append(tempboard)


def zamien_na_damki_biale(ruchy,bicia,wielokrotne):
    for y in ruchy:
        for x in range (1,7):
            if y[x]=='WM':
                y[x]='WK'
    for y in bicia:
        for x in range(1, 7):
            if y[x] == 'WM':
                y[x] = 'WK'
    for y in wielokrotne:
        for x in range(1, 7):
            if y[x] == 'WM':
                y[x] = 'WK'

def zamien_na_damki_czarne(ruchy,bicia,wielokrotne):
    for y in ruchy:
        for x in range (56,63):
            if y[x]=='BM':
                y[x]='BK'
    for y in bicia:
        for x in range(56,63):
            if y[x] == 'BM':
                y[x] = 'BK'
    for y in wielokrotne:
        for x in range(56,63):
            if y[x] == 'BM':
                y[x] = 'BK'


def Compare(chessboard, bigVector):                                          #mniej magiczna funkcja sprawdzajaca obecny stan z tablicami
    #obecna = []
    tocompare=[]
    #for x in chessboard():
    #    obecna.append(chessboard.gameTiles[x].pieceOnTile.toString())
    for z in range(64):
        tocompare.append(chessboard.gameTiles[z].pieceOnTile.toString())

    for y in bigVector:
        if tocompare == y:
            return True
    return False

def Komunikaty(chessboard,ruchy,bicia,wielokrotne):
    tocompare = []
    for z in range(64):
        tocompare.append(chessboard.gameTiles[z].pieceOnTile.toString())
    for y in wielokrotne:
        if y==tocompare:
            return 1            #jezeli jest wielokrotne bicie to git, nie ma nawet co wywalic
    for y in bicia:
        if y==tocompare and not wielokrotne:
            return 1             #jezeli jest bicie, a wielokrotnego nie ma, to git
        elif y==tocompare:
            return 2            #jak jest bicie, ale mogloby byc wielokrotne, to nie git :/
    for y in ruchy:
        if y==tocompare and ((not wielokrotne) or (not bicia)):
            return 1  #git
        if y==tocompare and not bicia:
            return 1
        elif y==tocompare:
            return 3             #mozliwe bicie jakiekolwiek, nie git
    #Generator_czarnych(chessboard,ruchy,bicia,wielokrotne)
    #Generator_bialych(chessboard, ruchy, bicia, wielokrotne)
    return 4           #jak nie znalezlismy, to walic to


def Generator_bialych(chessboard, ruchy, bicia, wielokrotne):
    # tocompare=[]
    # for z in range(64):
    #     tocompare.append(chessboard.gameTiles[z].pieceOnTile.toString())
    # ruchy.append(tocompare)
    ruchy_bialych(chessboard,ruchy)
    mozliwe_bicia_dla_bialych(chessboard,bicia,wielokrotne)
    mozliwe_ruchy_dla_bialej_damy(ruchy,chessboard)
    mozliwe_bicia_dla_bialej_damy(chessboard,bicia,wielokrotne)
    # zamien_na_damki_biale(ruchy,bicia,wielokrotne)

def Generator_czarnych(chessboard, ruchy, bicia, wielokrotne):
    # tocompare=[]
    # for z in range(64):
    #     tocompare.append(chessboard.gameTiles[z].pieceOnTile.toString())
    # ruchy.append(tocompare)
    mozliwy_ruch(chessboard,ruchy)
    mozliwe_bicia(chessboard,bicia,wielokrotne)
    mozliwe_ruchy_dla_czarnej_damy(ruchy,chessboard)
    mozliwe_bicia_dla_czarnej_damy(chessboard,bicia,wielokrotne)
    # zamien_na_damki_czarne(ruchy,bicia,wielokrotne)

def mozliwy_ruch(chessboard, bigVector):
    zaszly_zmiany = 0
    wewnetrzne = []
    for z in range(64):
        wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())

    for x in range(64):
        if zaszly_zmiany == 1:
            for z in range(64):
                wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            zaszly_zmiany = 0

        if chessboard.gameTiles[x].pieceOnTile.toString() == 'BM':
            if x == 7 or x == 23 or x == 39 or x == 55:
                if chessboard.gameTiles[x + 7].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x + 7] = 'BM'
                    zaszly_zmiany = 1
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
            elif x == 8 or x == 24 or x == 40:
                if chessboard.gameTiles[x + 9].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x + 9] = 'BM'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    zaszly_zmiany = 1
            elif x == 56 or x == 58 or x == 60 or x == 62:
                pass

            else:
                if chessboard.gameTiles[x + 9].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x + 9] = 'BM'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    for z in range(64):
                        wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
                if chessboard.gameTiles[x + 7].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x + 7] = 'BM'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    zaszly_zmiany = 1

def ruchy_bialych(chessboard, bigVector):
    zaszly_zmiany = 0
    wewnetrzne = []
    for z in range(64):
        wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())


    for x in range(64):
        if zaszly_zmiany == 1:
            for z in range(64):
                wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            zaszly_zmiany = 0

        if chessboard.gameTiles[x].pieceOnTile.toString() == 'WM':
            if x == 8 or x == 24 or x == 40 or x == 56:
                if chessboard.gameTiles[x - 7].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x - 7] = 'WM'
                    zaszly_zmiany = 1
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
            elif x == 55 or x == 23 or x == 39:
                if chessboard.gameTiles[x - 9].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x - 9] = 'WM'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    zaszly_zmiany = 1
            elif x == 1 or x == 3 or x == 5 or x == 6:
                pass

            else:
                if x > 8 and chessboard.gameTiles[x - 9].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x - 9] = 'WM'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    for z in range(64):
                        wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
                if chessboard.gameTiles[x - 7].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x - 7] = 'WM'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    zaszly_zmiany = 1

#czarne pionki
def mozliwe_bicia(chessboard, bigVector, drugalista):
    wewnetrzne = []
    zaszly_zmiany = 0


    for z in range(64):
        wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())

    for x in range(64):
        if zaszly_zmiany == 1:
            for z in range(64):
                wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            zaszly_zmiany = 0

        if wewnetrzne[x] == 'BM' and (x == 7 or x == 23 or x == 39 or x == 14 or x == 30 or x == 46):
            if wewnetrzne[x + 7] == 'WM' and wewnetrzne[x + 14] == 'n':
                        wewnetrzne[x] = 'n'
                        wewnetrzne[x + 7] = 'n'
                        wewnetrzne[x+14] = 'BM'
                        zaszly_zmiany = 1
                        wiecej_bic_for_one(drugalista, wewnetrzne,x+14)
                        bigVector.append(wewnetrzne.copy())
                        del wewnetrzne[:]
            elif wewnetrzne[x + 7] == 'WK' and wewnetrzne[x + 14] == 'n':
                wewnetrzne[x] = 'n'
                wewnetrzne[x + 7] = 'n'
                wewnetrzne[x + 14] = 'BM'
                zaszly_zmiany = 1
                wiecej_bic_for_one(drugalista, wewnetrzne, x + 14)
                bigVector.append(wewnetrzne.copy())
                del wewnetrzne[:]
        elif wewnetrzne[x] == 'BM' and (x == 8 or x == 24 or x == 40 or x==1 or x==17 or x==33):
            if wewnetrzne[x + 9] == 'WM' and wewnetrzne[x + 18] == 'n':
                        wewnetrzne[x] = 'n'
                        wewnetrzne[x + 9] = 'n'
                        wewnetrzne[x+18]='BM'
                        bigVector.append(wewnetrzne.copy())
                        wiecej_bic_for_one(drugalista, wewnetrzne, x + 18)
                        del wewnetrzne[:]
                        zaszly_zmiany = 1
            elif wewnetrzne[x + 9] == 'WK' and wewnetrzne[x + 18] == 'n':
                wewnetrzne[x] = 'n'
                wewnetrzne[x + 9] = 'n'
                wewnetrzne[x + 18] = 'BM'
                bigVector.append(wewnetrzne.copy())
                wiecej_bic_for_one(drugalista, wewnetrzne, x + 18)
                del wewnetrzne[:]
                zaszly_zmiany = 1
        elif wewnetrzne[x] == 'BM' and (x == 56 or x == 58 or x == 60 or x == 62 or x==49 or x==51 or x==53 or x ==55):
            pass
        elif wewnetrzne[x] == 'BM':
            if wewnetrzne[x + 9] == 'WM' and wewnetrzne[x + 18] == 'n':
                            wewnetrzne[x] = 'n'
                            wewnetrzne[x + 9] = 'n'
                            wewnetrzne[x + 18] = 'BM'
                            bigVector.append(wewnetrzne.copy())
                            wiecej_bic_for_one(drugalista, wewnetrzne, x + 18)
                            del wewnetrzne[:]
                            for z in range(64):
                                wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            elif wewnetrzne[x + 9] == 'WK' and wewnetrzne[x + 18] == 'n':
                            wewnetrzne[x] = 'n'
                            wewnetrzne[x + 9] = 'n'
                            wewnetrzne[x + 18] = 'BM'
                            bigVector.append(wewnetrzne.copy())
                            wiecej_bic_for_one(drugalista, wewnetrzne, x + 18)
                            del wewnetrzne[:]
                            for z in range(64):
                                wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            if wewnetrzne[x] == 'BM' and wewnetrzne[x + 7] == 'WM' and wewnetrzne[x + 14] == 'n':
                            wewnetrzne[x] = 'n'
                            wewnetrzne[x + 7] = 'n'
                            wewnetrzne[x + 14] = 'BM'
                            wiecej_bic_for_one(drugalista, wewnetrzne, x + 14)
                            bigVector.append(wewnetrzne.copy())
                            del wewnetrzne[:]
                            zaszly_zmiany = 1
            elif wewnetrzne[x] == 'BM' and wewnetrzne[x + 7] == 'WK' and wewnetrzne[x + 14] == 'n':
                            wewnetrzne[x] = 'n'
                            wewnetrzne[x + 7] = 'n'
                            wewnetrzne[x + 14] = 'BM'
                            wiecej_bic_for_one(drugalista, wewnetrzne, x + 14)
                            bigVector.append(wewnetrzne.copy())
                            del wewnetrzne[:]
                            zaszly_zmiany = 1
def wiecej_bic_for_one(bigVector, wewnetrzne,x):
    if wewnetrzne[x] == 'BM' and (x == 7 or x == 23 or x == 39 or x == 14 or x == 30 or x == 46):
        if wewnetrzne[x + 7] == 'WM' and wewnetrzne[x + 14] == 'n':
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 7] = 'n'
            wewnetrzne[x + 14] = 'BM'
            wiecej_bic_for_one(bigVector, wewnetrzne, x + 14)
            bigVector.append(wewnetrzne.copy())
            del wewnetrzne[:]
        if wewnetrzne[x + 7] == 'WK' and wewnetrzne[x + 14] == 'n':
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 7] = 'n'
            wewnetrzne[x + 14] = 'BM'
            wiecej_bic_for_one(bigVector, wewnetrzne, x + 14)
            bigVector.append(wewnetrzne.copy())
            del wewnetrzne[:]
    elif wewnetrzne[x] == 'BM' and (x == 8 or x == 24 or x == 40 or x == 1 or x == 17 or x == 33):
        if wewnetrzne[x + 9] == 'WM' and wewnetrzne[x + 18] == 'n':
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 9] = 'n'
            wewnetrzne[x + 18] = 'BM'
            wiecej_bic_for_one(bigVector, wewnetrzne, x + 18)
            bigVector.append(wewnetrzne.copy())
            del wewnetrzne[:]
        if wewnetrzne[x + 9] == 'WK' and wewnetrzne[x + 18] == 'n':
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 9] = 'n'
            wewnetrzne[x + 18] = 'BM'
            wiecej_bic_for_one(bigVector, wewnetrzne, x + 18)
            bigVector.append(wewnetrzne.copy())
            del wewnetrzne[:]
    elif wewnetrzne[x] == 'BM' and (
            x == 56 or x == 58 or x == 60 or x == 62 or x == 49 or x == 51 or x == 53 or x == 55):
        pass
    elif wewnetrzne[x] == 'BM':
        if wewnetrzne[x + 9] == 'WM' and wewnetrzne[x + 18] == 'n' and wewnetrzne[x + 7] == 'WM' and wewnetrzne[x + 14] == 'n':
            wewnetrzne2 = wewnetrzne [:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 9] = 'n'
            wewnetrzne[x + 18] = 'BM'
            wiecej_bic_for_one(bigVector, wewnetrzne, x + 18)
            bigVector.append(wewnetrzne.copy())
            del wewnetrzne[:]
            wewnetrzne2[x] = 'n'
            wewnetrzne2[x + 7] = 'n'
            wewnetrzne2[x + 14] = 'BM'
            wiecej_bic_for_one(bigVector, wewnetrzne2, x + 14)
            bigVector.append(wewnetrzne2.copy())
            del wewnetrzne2[:]
        elif wewnetrzne[x + 9] == 'WK' and wewnetrzne[x + 18] == 'n' and wewnetrzne[x + 7] == 'WK' and wewnetrzne[x + 14] == 'n':
            wewnetrzne2 = wewnetrzne [:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 9] = 'n'
            wewnetrzne[x + 18] = 'BM'
            wiecej_bic_for_one(bigVector, wewnetrzne, x + 18)
            bigVector.append(wewnetrzne.copy())
            del wewnetrzne[:]
            wewnetrzne2[x] = 'n'
            wewnetrzne2[x + 7] = 'n'
            wewnetrzne2[x + 14] = 'BM'
            wiecej_bic_for_one(bigVector, wewnetrzne2, x + 14)
            bigVector.append(wewnetrzne2.copy())
            del wewnetrzne2[:]
        elif wewnetrzne[x + 9] == 'WM' and wewnetrzne[x + 18] == 'n':
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 9] = 'n'
            wewnetrzne[x + 18] = 'BM'
            wiecej_bic_for_one(bigVector, wewnetrzne, x + 18)
            bigVector.append(wewnetrzne.copy())
            del wewnetrzne[:]
        elif wewnetrzne[x + 9] == 'WK' and wewnetrzne[x + 18] == 'n':
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 9] = 'n'
            wewnetrzne[x + 18] = 'BM'
            wiecej_bic_for_one(bigVector, wewnetrzne, x + 18)
            bigVector.append(wewnetrzne.copy())
            del wewnetrzne[:]

        elif wewnetrzne[x] == 'BM' and wewnetrzne[x + 7] == 'WM' and wewnetrzne[x + 14] == 'n':
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 7] = 'n'
            wewnetrzne[x + 14] = 'BM'
            wiecej_bic_for_one(bigVector, wewnetrzne, x + 14)
            bigVector.append(wewnetrzne.copy())
            del wewnetrzne[:]
            zaszly_zmiany = 1
        elif wewnetrzne[x] == 'BM' and wewnetrzne[x + 7] == 'WK' and wewnetrzne[x + 14] == 'n':
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 7] = 'n'
            wewnetrzne[x + 14] = 'BM'
            wiecej_bic_for_one(bigVector, wewnetrzne, x + 14)
            bigVector.append(wewnetrzne.copy())
            del wewnetrzne[:]
            zaszly_zmiany = 1

#biale pionki
def mozliwe_bicia_dla_bialych(chessboard, bigVector, drugalista):
    wewnetrzne =[]
    zaszly_zmiany = 0


    for z in range(64):
        wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())

    for x in range(64):
        if zaszly_zmiany == 1:
            for z in range(64):
                wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            zaszly_zmiany = 0

        if wewnetrzne[x] == 'WM' and (x == 56 or x == 40 or x == 24 or x == 49 or x == 33 or x == 17):
            if wewnetrzne[x - 7] == 'BM' or (wewnetrzne[x - 7] == 'BK') and wewnetrzne[x - 14] == 'n':
                        wewnetrzne[x] = 'n'
                        wewnetrzne[x - 7] = 'n'
                        wewnetrzne[x-14] = 'WM'
                        zaszly_zmiany = 1
                        wiecej_bic_for_one_dla_bialych(drugalista, wewnetrzne,x-14)
                        bigVector.append(wewnetrzne.copy())
                        del wewnetrzne[:]
        elif wewnetrzne[x] == 'WM' and (x == 62 or x == 55 or x == 46 or x==39 or x==30 or x==23):
            if (wewnetrzne[x - 9] == 'BM' or wewnetrzne[x-9]=='BK') and wewnetrzne[x - 18] == 'n':
                        wewnetrzne[x] = 'n'
                        wewnetrzne[x - 9] = 'n'
                        wewnetrzne[x-18]='WM'
                        bigVector.append(wewnetrzne.copy())
                        wiecej_bic_for_one_dla_bialych(drugalista, wewnetrzne, x - 18)
                        del wewnetrzne[:]
                        zaszly_zmiany = 1

        elif wewnetrzne[x] == 'WM' and (x == 1 or x == 3 or x == 5 or x == 7 or x== 8 or x==10 or x==12 or x ==14):
            pass
        elif wewnetrzne[x] == 'WM':
            if wewnetrzne[x - 9] == 'BM' or (wewnetrzne[x - 9] == 'BK') and wewnetrzne[x - 18] == 'n':
                            wewnetrzne[x] = 'n'
                            wewnetrzne[x - 9] = 'n'
                            wewnetrzne[x - 18] = 'WM'
                            bigVector.append(wewnetrzne.copy())
                            wiecej_bic_for_one_dla_bialych(drugalista, wewnetrzne, x - 18)
                            del wewnetrzne[:]
                            for z in range(64):
                                wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            if wewnetrzne[x] == 'WM' and (wewnetrzne[x - 7] == 'BM' or wewnetrzne[x - 7] == 'BK') and wewnetrzne[x - 14] == 'n':
                            wewnetrzne[x] = 'n'
                            wewnetrzne[x - 7] = 'n'
                            wewnetrzne[x - 14] = 'WM'
                            wiecej_bic_for_one_dla_bialych(drugalista, wewnetrzne, x - 14)
                            bigVector.append(wewnetrzne.copy())
                            del wewnetrzne[:]
                            zaszly_zmiany = 1

def wiecej_bic_for_one_dla_bialych(bigVector, wewnetrzne,x):
    if wewnetrzne[x] == 'WM' and (x == 24 or x == 40 or x == 56 or x == 49 or x == 33 or x == 17):
        if wewnetrzne[x - 7] == 'BM' and wewnetrzne[x - 14] == 'n':
            wewnetrzne[x] = 'n'
            wewnetrzne[x - 7] = 'n'
            wewnetrzne[x - 14] = 'WM'
            wiecej_bic_for_one(bigVector, wewnetrzne, x - 14)
            bigVector.append(wewnetrzne.copy())
            del wewnetrzne[:]
        if wewnetrzne[x - 7] == 'BK' and wewnetrzne[x - 14] == 'n':
            wewnetrzne[x] = 'n'
            wewnetrzne[x - 7] = 'n'
            wewnetrzne[x - 14] = 'WM'
            wiecej_bic_for_one(bigVector, wewnetrzne, x - 14)
            bigVector.append(wewnetrzne.copy())
            del wewnetrzne[:]
    elif wewnetrzne[x] == 'WM' and (x == 62 or x == 55 or x == 46 or x == 39 or x == 30 or x == 23):
        if wewnetrzne[x - 9] == 'BM' and wewnetrzne[x - 18] == 'n':
            wewnetrzne[x] = 'n'
            wewnetrzne[x - 9] = 'n'
            wewnetrzne[x - 18] = 'WM'
            wiecej_bic_for_one(bigVector, wewnetrzne, x - 18)
            bigVector.append(wewnetrzne.copy())
            del wewnetrzne[:]
        if wewnetrzne[x - 9] == 'BK' and wewnetrzne[x - 18] == 'n':
            wewnetrzne[x] = 'n'
            wewnetrzne[x - 9] = 'n'
            wewnetrzne[x - 18] = 'WM'
            wiecej_bic_for_one(bigVector, wewnetrzne, x - 18)
            bigVector.append(wewnetrzne.copy())
            del wewnetrzne[:]
    elif wewnetrzne[x] == 'WM' and (
            x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12 or x == 14):
        pass
    elif wewnetrzne[x] == 'WM':
        if wewnetrzne[x - 9] == 'BM' and wewnetrzne[x - 18] == 'n' and wewnetrzne[x - 7] == 'BM' and wewnetrzne[x - 14] == 'n':
            wewnetrzne2 = wewnetrzne [:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x - 9] = 'n'
            wewnetrzne[x - 18] = 'WM'
            wiecej_bic_for_one(bigVector, wewnetrzne, x - 18)
            bigVector.append(wewnetrzne.copy())
            del wewnetrzne [:]

            wewnetrzne2[x] = 'n'
            wewnetrzne2[x - 7] = 'n'
            wewnetrzne2[x - 14] = 'WM'
            wiecej_bic_for_one(bigVector, wewnetrzne2, x - 14)
            bigVector.append(wewnetrzne2.copy())
            del wewnetrzne2[:]
        if (wewnetrzne[x - 9] == 'BK' or wewnetrzne[x - 9] == 'BM') and wewnetrzne[x - 18] == 'n' and (wewnetrzne[x - 7] == 'BK' or wewnetrzne[x - 7] == 'BM')  and wewnetrzne[x - 14] == 'n':
            wewnetrzne2 = wewnetrzne [:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x - 9] = 'n'
            wewnetrzne[x - 18] = 'WM'
            wiecej_bic_for_one(bigVector, wewnetrzne, x - 18)
            bigVector.append(wewnetrzne.copy())
            del wewnetrzne[:]
            wewnetrzne2[x] = 'n'
            wewnetrzne2[x - 7] = 'n'
            wewnetrzne2[x - 14] = 'WM'
            wiecej_bic_for_one(bigVector, wewnetrzne2, x - 14)
            bigVector.append(wewnetrzne2.copy())
            del wewnetrzne2[:]
        elif (wewnetrzne[x - 9] == 'BM' or wewnetrzne[x - 9] == 'BK') and wewnetrzne[x - 18] == 'n':
            wewnetrzne[x] = 'n'
            wewnetrzne[x - 9] = 'n'
            wewnetrzne[x - 18] = 'WM'
            wiecej_bic_for_one(bigVector, wewnetrzne, x - 18)
            bigVector.append(wewnetrzne.copy())
            del wewnetrzne[:]
            # for z in range(64):
            #     wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
        elif wewnetrzne[x] == 'WM' and (wewnetrzne[x - 7] == 'BM' or wewnetrzne[x - 7] == 'BK') and wewnetrzne[x - 14] == 'n':
            wewnetrzne[x] = 'n'
            wewnetrzne[x - 7] = 'n'
            wewnetrzne[x - 14] = 'WM'
            wiecej_bic_for_one(bigVector, wewnetrzne, x - 14)
            bigVector.append(wewnetrzne.copy())
            del wewnetrzne[:]
            zaszly_zmiany = 1


#damki
def mozliwe_ruchy_dla_czarnej_damy(bigVector,chessboard):
    zaszly_zmiany = 0
    wewnetrzne = []
    for z in range(64):
        wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())

    for x in range(64):
        if zaszly_zmiany == 1:
            for z in range(64):
                wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            zaszly_zmiany = 0

        if chessboard.gameTiles[x].pieceOnTile.toString() == 'BK':
            if x == 7:
                if chessboard.gameTiles[x + 7].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x + 7] = 'BK'
                    zaszly_zmiany = 1
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
            if x == 56:
                if chessboard.gameTiles[x - 7].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x - 7] = 'BK'
                    zaszly_zmiany = 1
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
            elif x == 8 or x == 24 or x == 40:
                if chessboard.gameTiles[x + 9].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x + 9] = 'BK'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    for z in range(64):
                        wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
                if chessboard.gameTiles[x -7].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x - 7] = 'BK'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    zaszly_zmiany = 1
            elif x == 23 or x == 39 or x == 55:
                if chessboard.gameTiles[x - 9].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x - 9] = 'BK'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    for z in range(64):
                        wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
                if chessboard.gameTiles[x + 7].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x + 7] = 'BK'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    zaszly_zmiany = 1
            elif x == 1 or x == 3 or x == 5:
                if chessboard.gameTiles[x + 9].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x + 9] = 'BK'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    for z in range(64):
                        wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
                if chessboard.gameTiles[x + 7].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x + 7] = 'BK'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    zaszly_zmiany = 1

            else:
                if chessboard.gameTiles[x + 9].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x + 9] = 'BK'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    for z in range(64):
                        wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
                if chessboard.gameTiles[x + 7].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x + 7] = 'BK'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    for z in range(64):
                        wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
                if chessboard.gameTiles[x - 7].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x - 7] = 'BK'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    for z in range(64):
                        wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
                if chessboard.gameTiles[x - 9].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x - 9] = 'BK'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    for z in range(64):
                        wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())

def mozliwe_ruchy_dla_bialej_damy(bigVector,chessboard):
    zaszly_zmiany = 0
    wewnetrzne = []
    for z in range(64):
        wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())

    for x in range(64):
        if zaszly_zmiany == 1:
            for z in range(64):
                wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            zaszly_zmiany = 0

        if chessboard.gameTiles[x].pieceOnTile.toString() == 'WK':
            if x == 7:
                if chessboard.gameTiles[x + 7].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x + 7] = 'WK'
                    zaszly_zmiany = 1
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
            if x == 56:
                if chessboard.gameTiles[x - 7].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x - 7] = 'WK'
                    zaszly_zmiany = 1
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
            elif x == 8 or x == 24 or x == 40:
                if chessboard.gameTiles[x + 9].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x + 9] = 'WK'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    for z in range(64):
                        wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
                if chessboard.gameTiles[x -7].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x - 7] = 'WK'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    zaszly_zmiany = 1
            elif x == 23 or x == 39 or x == 55:
                if chessboard.gameTiles[x - 9].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x - 9] = 'WK'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    for z in range(64):
                        wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
                if chessboard.gameTiles[x + 7].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x + 7] = 'WK'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    zaszly_zmiany = 1
            elif x == 1 or x == 3 or x == 5:
                if chessboard.gameTiles[x + 9].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x + 9] = 'WK'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    for z in range(64):
                        wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
                if chessboard.gameTiles[x + 7].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x + 7] = 'WK'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    zaszly_zmiany = 1

            else:
                if chessboard.gameTiles[x + 9].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x + 9] = 'WK'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    for z in range(64):
                        wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
                if chessboard.gameTiles[x + 7].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x + 7] = 'WK'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    for z in range(64):
                        wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
                if chessboard.gameTiles[x - 7].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x - 7] = 'WK'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    for z in range(64):
                        wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
                if chessboard.gameTiles[x - 9].pieceOnTile.toString() == 'n':
                    wewnetrzne[x] = 'n'
                    wewnetrzne[x - 9] = 'WK'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    for z in range(64):
                        wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())




def mozliwe_bicia_dla_czarnej_damy(chessboard, bigVector, drugalista):
    wewnetrzne = []
    zaszly_zmiany = 0


    for z in range(64):
        wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())

    for x in range(64):
        if zaszly_zmiany == 1:
            for z in range(64):
                wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            zaszly_zmiany = 0

        if wewnetrzne[x] == 'BK' and (x == 7 or x == 14):
            if (wewnetrzne[x + 7] == 'WM' or wewnetrzne[x + 7] == 'WK') and wewnetrzne[x + 14] == 'n':
                        wewnetrzne[x] = 'n'
                        wewnetrzne[x + 7] = 'n'
                        wewnetrzne[x+14] = 'BK'
                        zaszly_zmiany = 1
                        wiecej_bic_dla_czarnej_damy(drugalista, wewnetrzne,x+14)
                        bigVector.append(wewnetrzne.copy())
                        del wewnetrzne[:]
        elif wewnetrzne[x] == 'BK' and (x == 8 or x == 1):
            if (wewnetrzne[x + 9] == 'WM' or wewnetrzne[x + 9] == 'WK') and wewnetrzne[x + 18] == 'n':
                        wewnetrzne[x] = 'n'
                        wewnetrzne[x + 9] = 'n'
                        wewnetrzne[x+18]='BK'
                        bigVector.append(wewnetrzne.copy())
                        wiecej_bic_dla_czarnej_damy(drugalista, wewnetrzne, x + 18)
                        del wewnetrzne[:]
                        zaszly_zmiany = 1
        elif wewnetrzne[x] == 'BK' and (x == 56 or x==49):
            if (wewnetrzne[x - 7] == 'WM' or wewnetrzne[x - 7] == 'WK') and wewnetrzne[x - 14] == 'n':
                        wewnetrzne[x] = 'n'
                        wewnetrzne[x - 7] = 'n'
                        wewnetrzne[x-14]='BK'
                        bigVector.append(wewnetrzne.copy())
                        wiecej_bic_dla_czarnej_damy(drugalista, wewnetrzne, x - 14)
                        del wewnetrzne[:]
                        zaszly_zmiany = 1
        elif wewnetrzne[x] == 'BK' and (x == 55 or x == 62):
            if (wewnetrzne[x - 9] == 'WM' or wewnetrzne[x - 9] == 'WK') and wewnetrzne[x + 18] == 'n':
                            wewnetrzne[x] = 'n'
                            wewnetrzne[x - 9] = 'n'
                            wewnetrzne[x - 18] = 'BK'
                            bigVector.append(wewnetrzne.copy())
                            wiecej_bic_dla_czarnej_damy(drugalista, wewnetrzne, x - 18)
                            del wewnetrzne[:]
                            for z in range(64):
                                wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
        elif wewnetrzne[x] == 'BK' and (x == 24 or x == 40 or x ==17 or x==33):
            if (wewnetrzne[x - 7] == 'WM' or wewnetrzne[x - 7] == 'WK') and wewnetrzne[x - 14] == 'n':
                wewnetrzne[x] = 'n'
                wewnetrzne[x - 7] = 'n'
                wewnetrzne[x - 14] = 'BK'
                bigVector.append(wewnetrzne.copy())
                wiecej_bic_dla_czarnej_damy(drugalista, wewnetrzne, x - 14)
                del wewnetrzne[:]
                for z in range(64):
                    wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            if (wewnetrzne[x + 9] == 'WM' or wewnetrzne[x + 9] == 'WK') and wewnetrzne[x + 18] == 'n':
                wewnetrzne[x] = 'n'
                wewnetrzne[x + 9] = 'n'
                wewnetrzne[x + 18] = 'BK'
                bigVector.append(wewnetrzne.copy())
                wiecej_bic_dla_czarnej_damy(drugalista, wewnetrzne, x + 18)
                del wewnetrzne[:]
                for z in range(64):
                    wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
        elif wewnetrzne[x] == 'BK' and (x == 23 or x == 30 or x==39 or x==46):
            if (wewnetrzne[x + 7] == 'WM' or wewnetrzne[x + 7] == 'WK') and wewnetrzne[x + 14] == 'n':
                wewnetrzne[x] = 'n'
                wewnetrzne[x + 7] = 'n'
                wewnetrzne[x + 14] = 'BK'
                bigVector.append(wewnetrzne.copy())
                wiecej_bic_dla_czarnej_damy(drugalista, wewnetrzne, x + 14)
                del wewnetrzne[:]
                for z in range(64):
                    wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            if (wewnetrzne[x - 9] == 'WM' or wewnetrzne[x - 9] == 'WK') and wewnetrzne[x - 18] == 'n':
                wewnetrzne[x] = 'n'
                wewnetrzne[x - 9] = 'n'
                wewnetrzne[x - 18] = 'BK'
                bigVector.append(wewnetrzne.copy())
                wiecej_bic_dla_czarnej_damy(drugalista, wewnetrzne, x - 18)
                del wewnetrzne[:]
                for z in range(64):
                    wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
        elif wewnetrzne[x] == 'BK' and (x == 3 or x == 5 or x== 10 or x==12):
            if (wewnetrzne[x + 7] == 'WM' or wewnetrzne[x + 7] == 'WK') and wewnetrzne[x + 14] == 'n':
                wewnetrzne[x] = 'n'
                wewnetrzne[x + 7] = 'n'
                wewnetrzne[x + 14] = 'BK'
                bigVector.append(wewnetrzne.copy())
                wiecej_bic_dla_czarnej_damy(drugalista, wewnetrzne, x + 14)
                del wewnetrzne[:]
                for z in range(64):
                    wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            if (wewnetrzne[x + 9] == 'WM' or wewnetrzne[x + 9] == 'WK') and wewnetrzne[x + 18] == 'n':
                wewnetrzne[x] = 'n'
                wewnetrzne[x + 9] = 'n'
                wewnetrzne[x + 18] = 'B'
                bigVector.append(wewnetrzne.copy())
                wiecej_bic_dla_czarnej_damy(drugalista, wewnetrzne, x + 18)
                del wewnetrzne[:]
                for z in range(64):
                    wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
        elif wewnetrzne[x] == 'BK' and (x == 24 or x == 40 or x ==17 or x==33):
            if (wewnetrzne[x - 7] == 'WM' or wewnetrzne[x - 7] == 'WK') and wewnetrzne[x - 14] == 'n':
                wewnetrzne[x] = 'n'
                wewnetrzne[x - 7] = 'n'
                wewnetrzne[x - 14] = 'BK'
                bigVector.append(wewnetrzne.copy())
                wiecej_bic_dla_czarnej_damy(drugalista, wewnetrzne, x - 14)
                del wewnetrzne[:]
                for z in range(64):
                    wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            if (wewnetrzne[x - 9] == 'WM' or wewnetrzne[x - 9] == 'WK') and wewnetrzne[x - 18] == 'n':
                wewnetrzne[x] = 'n'
                wewnetrzne[x - 9] = 'n'
                wewnetrzne[x - 18] = 'BK'
                bigVector.append(wewnetrzne.copy())
                wiecej_bic_dla_czarnej_damy(drugalista, wewnetrzne, x - 18)
                del wewnetrzne[:]
                for z in range(64):
                    wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
        elif wewnetrzne[x] == 'BK' and (x == 26 or x == 19 or x ==28 or x==21 or x==35 or x==42 or x==44 or x==37):
            if (wewnetrzne[x - 7] == 'WM' or wewnetrzne[x - 7] == 'WK') and wewnetrzne[x - 14] == 'n':
                wewnetrzne[x] = 'n'
                wewnetrzne[x - 7] = 'n'
                wewnetrzne[x - 14] = 'BK'
                bigVector.append(wewnetrzne.copy())
                wiecej_bic_dla_czarnej_damy(drugalista, wewnetrzne, x - 14)
                del wewnetrzne[:]
                for z in range(64):
                    wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            if (wewnetrzne[x - 9] == 'WM' or wewnetrzne[x - 9] == 'WK') and wewnetrzne[x - 18] == 'n':
                wewnetrzne[x] = 'n'
                wewnetrzne[x - 9] = 'n'
                wewnetrzne[x - 18] = 'BK'
                bigVector.append(wewnetrzne.copy())
                wiecej_bic_dla_czarnej_damy(drugalista, wewnetrzne, x - 18)
                del wewnetrzne[:]
                for z in range(64):
                    wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            if (wewnetrzne[x + 7] == 'WM' or wewnetrzne[x + 7] == 'WK') and wewnetrzne[x + 14] == 'n':
                wewnetrzne[x] = 'n'
                wewnetrzne[x + 7] = 'n'
                wewnetrzne[x + 14] = 'BK'
                bigVector.append(wewnetrzne.copy())
                wiecej_bic_dla_czarnej_damy(drugalista, wewnetrzne, x + 14)
                del wewnetrzne[:]
                for z in range(64):
                    wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            if (wewnetrzne[x + 9] == 'WM' or wewnetrzne[x + 9] == 'WK') and wewnetrzne[x + 18] == 'n':
                wewnetrzne[x] = 'n'
                wewnetrzne[x + 9] = 'n'
                wewnetrzne[x + 18] = 'BK'
                bigVector.append(wewnetrzne.copy())
                wiecej_bic_dla_czarnej_damy(drugalista, wewnetrzne, x + 18)
                del wewnetrzne[:]
                for z in range(64):
                    wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
def wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne,x):
    if wewnetrzne[x] == 'BK' and (x == 7 or x == 14):
        if (wewnetrzne[x + 7] == 'WM' or wewnetrzne[x + 7] == 'WK') and wewnetrzne[x + 14] == 'n':
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 7] = 'n'
            wewnetrzne[x + 14] = 'BK'
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x + 14)
            bigVector.append(wewnetrzne.copy())
            del wewnetrzne[:]
    elif wewnetrzne[x] == 'BK' and (x == 8 or x == 1):
        if (wewnetrzne[x + 9] == 'WM' or wewnetrzne[x + 9] == 'WK') and wewnetrzne[x + 18] == 'n':
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 9] = 'n'
            wewnetrzne[x + 18] = 'BK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x + 18)
            del wewnetrzne[:]
    elif wewnetrzne[x] == 'BK' and (x == 56 or x == 49):
        if (wewnetrzne[x - 7] == 'WM' or wewnetrzne[x - 7] == 'WK') and wewnetrzne[x - 14] == 'n':
            wewnetrzne[x] = 'n'
            wewnetrzne[x - 7] = 'n'
            wewnetrzne[x - 14] = 'BK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x - 14)
            del wewnetrzne[:]
    elif wewnetrzne[x] == 'BK' and (x == 55 or x == 62):
        if (wewnetrzne[x - 9] == 'WM' or wewnetrzne[x - 9] == 'WK') and wewnetrzne[x + 18] == 'n':
            chessboard = wewnetrzne [:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x - 9] = 'n'
            wewnetrzne[x - 18] = 'BK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x - 18)
            del wewnetrzne[:]
            for z in range(64):
                wewnetrzne.append(chessboard[z])
    elif wewnetrzne[x] == 'BK' and (x == 24 or x == 40 or x == 17 or x == 33):
        if (wewnetrzne[x - 7] == 'WM' or wewnetrzne[x - 7] == 'WK') and wewnetrzne[x - 14] == 'n':
            chessboard = wewnetrzne[:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x - 7] = 'n'
            wewnetrzne[x - 14] = 'BK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x - 14)
            del wewnetrzne[:]
            for z in range(64):
                wewnetrzne.append(chessboard[z])
        if (wewnetrzne[x + 9] == 'WM' or wewnetrzne[x + 9] == 'WK') and wewnetrzne[x + 18] == 'n':
            chessboard = wewnetrzne[:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 9] = 'n'
            wewnetrzne[x + 18] = 'BK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x + 18)
            del wewnetrzne[:]
            for z in range(64):
                wewnetrzne.append(chessboard[z])
    elif wewnetrzne[x] == 'BK' and (x == 23 or x == 30 or x == 39 or x == 46):
        if (wewnetrzne[x + 7] == 'WM' or wewnetrzne[x + 7] == 'WK') and wewnetrzne[x + 14] == 'n':
            chessboard = wewnetrzne[:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 7] = 'n'
            wewnetrzne[x + 14] = 'BK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x + 14)
            del wewnetrzne[:]
            for z in range(64):
                wewnetrzne.append(chessboard[z])
        if (wewnetrzne[x - 9] == 'WM' or wewnetrzne[x - 9] == 'WK') and wewnetrzne[x - 18] == 'n':
            chessboard = wewnetrzne[:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x - 9] = 'n'
            wewnetrzne[x - 18] = 'BK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x - 18)
            del wewnetrzne[:]
            for z in range(64):
                wewnetrzne.append(chessboard[z])
    elif wewnetrzne[x] == 'BK' and (x == 3 or x == 5 or x == 10 or x == 12):
        if (wewnetrzne[x + 7] == 'WM' or wewnetrzne[x + 7] == 'WK') and wewnetrzne[x + 14] == 'n':
            chessboard = wewnetrzne[:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 7] = 'n'
            wewnetrzne[x + 14] = 'BK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x + 14)
            del wewnetrzne[:]
            for z in range(64):
                wewnetrzne.append(chessboard[z])
        if (wewnetrzne[x + 9] == 'WM' or wewnetrzne[x + 9] == 'WK') and wewnetrzne[x + 18] == 'n':
            chessboard = wewnetrzne[:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 9] = 'n'
            wewnetrzne[x + 18] = 'BK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x + 18)
            del wewnetrzne[:]
            for z in range(64):
                wewnetrzne.append(chessboard[z])
    elif wewnetrzne[x] == 'BK' and (x == 24 or x == 40 or x == 17 or x == 33):
        if (wewnetrzne[x - 7] == 'WM' or wewnetrzne[x - 7] == 'WK') and wewnetrzne[x - 14] == 'n':
            chessboard = wewnetrzne[:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x - 7] = 'n'
            wewnetrzne[x - 14] = 'BK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x - 14)
            del wewnetrzne[:]
            for z in range(64):
                wewnetrzne.append(chessboard[z])
        if (wewnetrzne[x - 9] == 'WM' or wewnetrzne[x - 9] == 'WK') and wewnetrzne[x - 18] == 'n':
            chessboard = wewnetrzne[:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x - 9] = 'n'
            wewnetrzne[x - 18] = 'BK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x - 18)
            del wewnetrzne[:]
            for z in range(64):
                wewnetrzne.append(chessboard[z])
    elif wewnetrzne[x] == 'BK' and (
            x == 26 or x == 19 or x == 28 or x == 21 or x == 35 or x == 42 or x == 44 or x == 37):
        if (wewnetrzne[x - 7] == 'WM' or wewnetrzne[x - 7] == 'WK') and wewnetrzne[x - 14] == 'n':
            chessboard = wewnetrzne[:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x - 7] = 'n'
            wewnetrzne[x - 14] = 'BK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x - 14)
            del wewnetrzne[:]
            for z in range(64):
                wewnetrzne.append(chessboard[z])
        if (wewnetrzne[x - 9] == 'WM' or wewnetrzne[x - 9] == 'WK') and wewnetrzne[x - 18] == 'n':
            chessboard = wewnetrzne[:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x - 9] = 'n'
            wewnetrzne[x - 18] = 'BK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x - 18)
            del wewnetrzne[:]
            for z in range(64):
                wewnetrzne.append(chessboard[z])
        if (wewnetrzne[x + 7] == 'WM' or wewnetrzne[x + 7] == 'WK') and wewnetrzne[x + 14] == 'n':
            chessboard = wewnetrzne[:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 7] = 'n'
            wewnetrzne[x + 14] = 'BK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x + 14)
            del wewnetrzne[:]
            for z in range(64):
                wewnetrzne.append(chessboard[z])
        if (wewnetrzne[x + 9] == 'WM' or wewnetrzne[x + 9] == 'WK') and wewnetrzne[x + 18] == 'n':
            chessboard = wewnetrzne[:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 9] = 'n'
            wewnetrzne[x + 18] = 'BK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x + 18)
            del wewnetrzne[:]
            for z in range(64):
                wewnetrzne.append(chessboard[z])


def mozliwe_bicia_dla_bialej_damy(chessboard, bigVector,drugalista):
    wewnetrzne = []
    zaszly_zmiany = 0


    for z in range(64):
        wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())

    for x in range(64):
        if zaszly_zmiany == 1:
            for z in range(64):
                wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            zaszly_zmiany = 0

        if wewnetrzne[x] == 'WK' and (x == 7 or x == 14):
            if (wewnetrzne[x + 7] == 'BM' or wewnetrzne[x + 7] == 'BK') and wewnetrzne[x + 14] == 'n':
                        wewnetrzne[x] = 'n'
                        wewnetrzne[x + 7] = 'n'
                        wewnetrzne[x+14] = 'WK'
                        zaszly_zmiany = 1
                        wiecej_bic_dla_bialej_damy(drugalista, wewnetrzne,x+14)
                        bigVector.append(wewnetrzne.copy())
                        del wewnetrzne[:]
        elif wewnetrzne[x] == 'WK' and (x == 8 or x == 1):
            if (wewnetrzne[x + 9] == 'BM' or wewnetrzne[x + 9] == 'BK') and wewnetrzne[x + 18] == 'n':
                        wewnetrzne[x] = 'n'
                        wewnetrzne[x + 9] = 'n'
                        wewnetrzne[x+18]='WK'
                        bigVector.append(wewnetrzne.copy())
                        wiecej_bic_dla_bialej_damy(drugalista, wewnetrzne, x + 18)
                        del wewnetrzne[:]
                        zaszly_zmiany = 1
        elif wewnetrzne[x] == 'WK' and (x == 56 or x==49):
            if (wewnetrzne[x - 7] == 'BM' or wewnetrzne[x - 7] == 'BK') and wewnetrzne[x - 14] == 'n':
                        wewnetrzne[x] = 'n'
                        wewnetrzne[x - 7] = 'n'
                        wewnetrzne[x-14]='WK'
                        bigVector.append(wewnetrzne.copy())
                        wiecej_bic_dla_bialej_damy(drugalista, wewnetrzne, x - 14)
                        del wewnetrzne[:]
                        zaszly_zmiany = 1
        elif wewnetrzne[x] == 'WK' and (x == 55 or x == 62):
            if (wewnetrzne[x - 9] == 'BM' or wewnetrzne[x - 9] == 'BK') and wewnetrzne[x + 18] == 'n':
                            wewnetrzne[x] = 'n'
                            wewnetrzne[x - 9] = 'n'
                            wewnetrzne[x - 18] = 'WK'
                            bigVector.append(wewnetrzne.copy())
                            wiecej_bic_dla_bialej_damy(drugalista, wewnetrzne, x - 18)
                            del wewnetrzne[:]
                            for z in range(64):
                                wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
        elif wewnetrzne[x] == 'WK' and (x == 24 or x == 40 or x ==17 or x==33):
            if (wewnetrzne[x - 7] == 'BM' or wewnetrzne[x - 7] == 'BK') and wewnetrzne[x - 14] == 'n':
                wewnetrzne[x] = 'n'
                wewnetrzne[x - 7] = 'n'
                wewnetrzne[x - 14] = 'WK'
                bigVector.append(wewnetrzne.copy())
                wiecej_bic_dla_bialej_damy(drugalista, wewnetrzne, x - 14)
                del wewnetrzne[:]
                for z in range(64):
                    wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            if (wewnetrzne[x + 9] == 'BM' or wewnetrzne[x + 9] == 'BK') and wewnetrzne[x + 18] == 'n':
                wewnetrzne[x] = 'n'
                wewnetrzne[x + 9] = 'n'
                wewnetrzne[x + 18] = 'WK'
                bigVector.append(wewnetrzne.copy())
                wiecej_bic_dla_bialej_damy(drugalista, wewnetrzne, x + 18)
                del wewnetrzne[:]
                for z in range(64):
                    wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
        elif wewnetrzne[x] == 'WK' and (x == 23 or x == 30 or x==39 or x==46):
            if (wewnetrzne[x + 7] == 'BM' or wewnetrzne[x + 7] == 'BK') and wewnetrzne[x + 14] == 'n':
                wewnetrzne[x] = 'n'
                wewnetrzne[x + 7] = 'n'
                wewnetrzne[x + 14] = 'WK'
                bigVector.append(wewnetrzne.copy())
                wiecej_bic_dla_bialej_damy(drugalista, wewnetrzne, x + 14)
                del wewnetrzne[:]
                for z in range(64):
                    wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            if (wewnetrzne[x - 9] == 'BM' or wewnetrzne[x - 9] == 'BK') and wewnetrzne[x - 18] == 'n':
                wewnetrzne[x] = 'n'
                wewnetrzne[x - 9] = 'n'
                wewnetrzne[x - 18] = 'WK'
                bigVector.append(wewnetrzne.copy())
                wiecej_bic_dla_bialej_damy(drugalista, wewnetrzne, x - 18)
                del wewnetrzne[:]
                for z in range(64):
                    wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
        elif wewnetrzne[x] == 'WK' and (x == 3 or x == 5 or x== 10 or x==12):
            if (wewnetrzne[x + 7] == 'BM' or wewnetrzne[x + 7] == 'BK') and wewnetrzne[x + 14] == 'n':
                wewnetrzne[x] = 'n'
                wewnetrzne[x + 7] = 'n'
                wewnetrzne[x + 14] = 'WK'
                bigVector.append(wewnetrzne.copy())
                wiecej_bic_dla_bialej_damy(drugalista, wewnetrzne, x + 14)
                del wewnetrzne[:]
                for z in range(64):
                    wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            if (wewnetrzne[x + 9] == 'BM' or wewnetrzne[x + 9] == 'BK') and wewnetrzne[x + 18] == 'n':
                wewnetrzne[x] = 'n'
                wewnetrzne[x + 9] = 'n'
                wewnetrzne[x + 18] = 'B'
                bigVector.append(wewnetrzne.copy())
                wiecej_bic_dla_bialej_damy(drugalista, wewnetrzne, x + 18)
                del wewnetrzne[:]
                for z in range(64):
                    wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
        elif wewnetrzne[x] == 'WK' and (x == 24 or x == 40 or x ==17 or x==33):
            if (wewnetrzne[x - 7] == 'BM' or wewnetrzne[x - 7] == 'BK') and wewnetrzne[x - 14] == 'n':
                wewnetrzne[x] = 'n'
                wewnetrzne[x - 7] = 'n'
                wewnetrzne[x - 14] = 'WK'
                bigVector.append(wewnetrzne.copy())
                wiecej_bic_dla_bialej_damy(drugalista, wewnetrzne, x - 14)
                del wewnetrzne[:]
                for z in range(64):
                    wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            if (wewnetrzne[x - 9] == 'BM' or wewnetrzne[x - 9] == 'BK') and wewnetrzne[x - 18] == 'n':
                wewnetrzne[x] = 'n'
                wewnetrzne[x - 9] = 'n'
                wewnetrzne[x - 18] = 'WK'
                bigVector.append(wewnetrzne.copy())
                wiecej_bic_dla_bialej_damy(drugalista, wewnetrzne, x - 18)
                del wewnetrzne[:]
                for z in range(64):
                    wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
        elif wewnetrzne[x] == 'WK' and (x == 26 or x == 19 or x ==28 or x==21 or x==35 or x==42 or x==44 or x==37):
            if (wewnetrzne[x - 7] == 'BM' or wewnetrzne[x - 7] == 'BK') and wewnetrzne[x - 14] == 'n':
                wewnetrzne[x] = 'n'
                wewnetrzne[x - 7] = 'n'
                wewnetrzne[x - 14] = 'WK'
                bigVector.append(wewnetrzne.copy())
                wiecej_bic_dla_bialej_damy(drugalista, wewnetrzne, x - 14)
                del wewnetrzne[:]
                for z in range(64):
                    wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            if (wewnetrzne[x - 9] == 'BM' or wewnetrzne[x - 9] == 'BK') and wewnetrzne[x - 18] == 'n':
                wewnetrzne[x] = 'n'
                wewnetrzne[x - 9] = 'n'
                wewnetrzne[x - 18] = 'WK'
                bigVector.append(wewnetrzne.copy())
                wiecej_bic_dla_bialej_damy(drugalista, wewnetrzne, x - 18)
                del wewnetrzne[:]
                for z in range(64):
                    wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            if (wewnetrzne[x + 7] == 'BM' or wewnetrzne[x + 7] == 'BK') and wewnetrzne[x + 14] == 'n':
                wewnetrzne[x] = 'n'
                wewnetrzne[x + 7] = 'n'
                wewnetrzne[x + 14] = 'WK'
                bigVector.append(wewnetrzne.copy())
                wiecej_bic_dla_bialej_damy(drugalista, wewnetrzne, x + 14)
                del wewnetrzne[:]
                for z in range(64):
                    wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            if (wewnetrzne[x + 9] == 'BM' or wewnetrzne[x + 9] == 'BK') and wewnetrzne[x + 18] == 'n':
                wewnetrzne[x] = 'n'
                wewnetrzne[x + 9] = 'n'
                wewnetrzne[x + 18] = 'WK'
                bigVector.append(wewnetrzne.copy())
                wiecej_bic_dla_bialej_damy(drugalista, wewnetrzne, x + 18)
                del wewnetrzne[:]
                for z in range(64):
                    wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
def wiecej_bic_dla_bialej_damy(bigVector, wewnetrzne,x):
    if wewnetrzne[x] == 'WK' and (x == 7 or x == 14):
        if (wewnetrzne[x + 7] == 'BM' or wewnetrzne[x + 7] == 'BK') and wewnetrzne[x + 14] == 'n':
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 7] = 'n'
            wewnetrzne[x + 14] = 'WK'
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x + 14)
            bigVector.append(wewnetrzne.copy())
            del wewnetrzne[:]
    elif wewnetrzne[x] == 'WK' and (x == 8 or x == 1):
        if (wewnetrzne[x + 9] == 'BM' or wewnetrzne[x + 9] == 'BK') and wewnetrzne[x + 18] == 'n':
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 9] = 'n'
            wewnetrzne[x + 18] = 'WK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x + 18)
            del wewnetrzne[:]
    elif wewnetrzne[x] == 'WK' and (x == 56 or x == 49):
        if (wewnetrzne[x - 7] == 'BM' or wewnetrzne[x - 7] == 'BK') and wewnetrzne[x - 14] == 'n':
            wewnetrzne[x] = 'n'
            wewnetrzne[x - 7] = 'n'
            wewnetrzne[x - 14] = 'WK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x - 14)
            del wewnetrzne[:]
    elif wewnetrzne[x] == 'WK' and (x == 55 or x == 62):
        if (wewnetrzne[x - 9] == 'BM' or wewnetrzne[x - 9] == 'BK') and wewnetrzne[x + 18] == 'n':
            chessboard = wewnetrzne [:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x - 9] = 'n'
            wewnetrzne[x - 18] = 'WK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x - 18)
            del wewnetrzne[:]
            for z in range(64):
                wewnetrzne.append(chessboard[z])
    elif wewnetrzne[x] == 'WK' and (x == 24 or x == 40 or x == 17 or x == 33):
        if (wewnetrzne[x - 7] == 'BM' or wewnetrzne[x - 7] == 'BK') and wewnetrzne[x - 14] == 'n':
            chessboard = wewnetrzne[:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x - 7] = 'n'
            wewnetrzne[x - 14] = 'WK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x - 14)
            del wewnetrzne[:]
            for z in range(64):
                wewnetrzne.append(chessboard[z])
        if (wewnetrzne[x + 9] == 'BM' or wewnetrzne[x + 9] == 'BK') and wewnetrzne[x + 18] == 'n':
            chessboard = wewnetrzne[:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 9] = 'n'
            wewnetrzne[x + 18] = 'WK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x + 18)
            del wewnetrzne[:]
            for z in range(64):
                wewnetrzne.append(chessboard[z])
    elif wewnetrzne[x] == 'WK' and (x == 23 or x == 30 or x == 39 or x == 46):
        if (wewnetrzne[x + 7] == 'BM' or wewnetrzne[x + 7] == 'BK') and wewnetrzne[x + 14] == 'n':
            chessboard = wewnetrzne[:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 7] = 'n'
            wewnetrzne[x + 14] = 'WK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x + 14)
            del wewnetrzne[:]
            for z in range(64):
                wewnetrzne.append(chessboard[z])
        if (wewnetrzne[x - 9] == 'BM' or wewnetrzne[x - 9] == 'BK') and wewnetrzne[x - 18] == 'n':
            chessboard = wewnetrzne[:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x - 9] = 'n'
            wewnetrzne[x - 18] = 'WK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x - 18)
            del wewnetrzne[:]
            for z in range(64):
                wewnetrzne.append(chessboard[z])
    elif wewnetrzne[x] == 'WK' and (x == 3 or x == 5 or x == 10 or x == 12):
        if (wewnetrzne[x + 7] == 'BM' or wewnetrzne[x + 7] == 'BK') and wewnetrzne[x + 14] == 'n':
            chessboard = wewnetrzne[:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 7] = 'n'
            wewnetrzne[x + 14] = 'WK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x + 14)
            del wewnetrzne[:]
            for z in range(64):
                wewnetrzne.append(chessboard[z])
        if (wewnetrzne[x + 9] == 'BM' or wewnetrzne[x + 9] == 'BK') and wewnetrzne[x + 18] == 'n':
            chessboard = wewnetrzne[:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 9] = 'n'
            wewnetrzne[x + 18] = 'WK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x + 18)
            del wewnetrzne[:]
            for z in range(64):
                wewnetrzne.append(chessboard[z])
    elif wewnetrzne[x] == 'WK' and (x == 24 or x == 40 or x == 17 or x == 33):
        if (wewnetrzne[x - 7] == 'BM' or wewnetrzne[x - 7] == 'BK') and wewnetrzne[x - 14] == 'n':
            chessboard = wewnetrzne[:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x - 7] = 'n'
            wewnetrzne[x - 14] = 'WK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x - 14)
            del wewnetrzne[:]
            for z in range(64):
                wewnetrzne.append(chessboard[z])
        if (wewnetrzne[x - 9] == 'BM' or wewnetrzne[x - 9] == 'BK') and wewnetrzne[x - 18] == 'n':
            chessboard = wewnetrzne[:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x - 9] = 'n'
            wewnetrzne[x - 18] = 'WK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x - 18)
            del wewnetrzne[:]
            for z in range(64):
                wewnetrzne.append(chessboard[z])
    elif wewnetrzne[x] == 'WK' and (
            x == 26 or x == 19 or x == 28 or x == 21 or x == 35 or x == 42 or x == 44 or x == 37):
        if (wewnetrzne[x - 7] == 'BM' or wewnetrzne[x - 7] == 'BK') and wewnetrzne[x - 14] == 'n':
            chessboard = wewnetrzne[:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x - 7] = 'n'
            wewnetrzne[x - 14] = 'WK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x - 14)
            del wewnetrzne[:]
            for z in range(64):
                wewnetrzne.append(chessboard[z])
        if (wewnetrzne[x - 9] == 'BM' or wewnetrzne[x - 9] == 'BK') and wewnetrzne[x - 18] == 'n':
            chessboard = wewnetrzne[:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x - 9] = 'n'
            wewnetrzne[x - 18] = 'WK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x - 18)
            del wewnetrzne[:]
            for z in range(64):
                wewnetrzne.append(chessboard[z])
        if (wewnetrzne[x + 7] == 'BM' or wewnetrzne[x + 7] == 'BK') and wewnetrzne[x + 14] == 'n':
            chessboard = wewnetrzne[:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 7] = 'n'
            wewnetrzne[x + 14] = 'WK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x + 14)
            del wewnetrzne[:]
            for z in range(64):
                wewnetrzne.append(chessboard[z])
        if (wewnetrzne[x + 9] == 'BM' or wewnetrzne[x + 9] == 'BK') and wewnetrzne[x + 18] == 'n':
            chessboard = wewnetrzne[:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 9] = 'n'
            wewnetrzne[x + 18] = 'WK'
            bigVector.append(wewnetrzne.copy())
            wiecej_bic_dla_czarnej_damy(bigVector, wewnetrzne, x + 18)
            del wewnetrzne[:]
            for z in range(64):
                wewnetrzne.append(chessboard[z])

