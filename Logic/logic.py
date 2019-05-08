def CreateTemps(chessboard, bigVector, tempboard):                         #magiczna funkcja tworzenia tablic mozliwych ruchow
    for x in chessboard:
        tempboard.append(chessboard.gameTiles[x].pieceOnTile.toString())
    bigVector.append(tempboard)

def Compare(chessboard, bigVector):                                          #mniej magiczna funkcja sprawdzajaca obecny stan z tablicami
    #obecna = []
    tocompare=[]
    #for x in chessboard():
    #    obecna.append(chessboard.gameTiles[x].pieceOnTile.toString())
    for z in range(64):
        tocompare.append(chessboard.gameTiles[z].pieceOnTile.toString())

    for y in bigVector:
        if tocompare == y:
            print("git")
            break



def mozliwy_ruch(chessboard, wewnetrzne, bigVector):
    zaszly_zmiany = 0
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

        elif chessboard.gameTiles[x].pieceOnTile.toString() == 'WM':
            if x == 8 or x == 24 or x == 40 or x==56:
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
                print()

            else:
                if x>8 and chessboard.gameTiles[x - 9].pieceOnTile.toString() == 'n':
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

def mozliwe_bicia(chessboard, wewnetrzne, bigVector):
    zaszly_zmiany = 0


    for z in range(64):
        wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())

    for x in range(64):
        if zaszly_zmiany == 1:
            for z in range(64):
                wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            zaszly_zmiany = 0

        if wewnetrzne[x] == 'BM' and (x == 7 or x == 23 or x == 39 or x == 14 or x == 30 or x == 46) and wewnetrzne[x + 7] == 'WM' and wewnetrzne[x + 14] == 'n':
                        wewnetrzne[x] = 'n'
                        wewnetrzne[x + 7] = 'n'
                        wewnetrzne[x+14] = 'BM'
                        zaszly_zmiany = 1
                        wiecej_bic_for_one(bigVector, wewnetrzne,x+14)
                        bigVector.append(wewnetrzne.copy())
                        del wewnetrzne[:]
        elif wewnetrzne[x] == 'BM' and (x == 8 or x == 24 or x == 40 or x==1 or x==17 or x==33) and wewnetrzne[x + 9] == 'WM' and wewnetrzne[x + 18] == 'n':
                        wewnetrzne[x] = 'n'
                        wewnetrzne[x + 9] = 'n'
                        wewnetrzne[x+18]='BM'
                        bigVector.append(wewnetrzne.copy())
                        wiecej_bic_for_one(bigVector, wewnetrzne, x + 18)
                        del wewnetrzne[:]
                        zaszly_zmiany = 1
        elif wewnetrzne[x] == 'BM' and (x == 56 or x == 58 or x == 60 or x == 62 or x==49 or x==51 or x==53 or x ==55):
            print()
        elif wewnetrzne[x] == 'BM':
            if wewnetrzne[x + 9] == 'WM' and wewnetrzne[x + 18] == 'n':
                            wewnetrzne[x] = 'n'
                            wewnetrzne[x + 9] = 'n'
                            wewnetrzne[x + 18] = 'BM'
                            bigVector.append(wewnetrzne.copy())
                            wiecej_bic_for_one(bigVector, wewnetrzne, x + 18)
                            del wewnetrzne[:]
                            for z in range(64):
                                wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            if wewnetrzne[x] == 'BM' and wewnetrzne[x + 7] == 'WM' and wewnetrzne[x + 14] == 'n':
                            wewnetrzne[x] = 'n'
                            wewnetrzne[x + 7] = 'n'
                            wewnetrzne[x + 14] = 'BM'
                            wiecej_bic_for_one(bigVector, wewnetrzne, x + 14)
                            bigVector.append(wewnetrzne.copy())
                            del wewnetrzne[:]
                            zaszly_zmiany = 1

def wiecej_bic_for_one(bigVector, wewnetrzne,x):
    if wewnetrzne[x] == 'BM' and (x == 7 or x == 23 or x == 39 or x == 14 or x == 30 or x == 46) and wewnetrzne[x + 7] == 'WM' and wewnetrzne[x + 14] == 'n':
        wewnetrzne[x] = 'n'
        wewnetrzne[x + 7] = 'n'
        wewnetrzne[x + 14] = 'BM'
        wiecej_bic_for_one(bigVector, wewnetrzne, x + 14)
        bigVector.append(wewnetrzne.copy())
        del wewnetrzne[:]
    elif wewnetrzne[x] == 'BM' and (x == 8 or x == 24 or x == 40 or x == 1 or x == 17 or x == 33) and wewnetrzne[x + 9] == 'WM' and wewnetrzne[x + 18] == 'n':
        wewnetrzne[x] = 'n'
        wewnetrzne[x + 9] = 'n'
        wewnetrzne[x + 18] = 'BM'
        wiecej_bic_for_one(bigVector, wewnetrzne, x + 18)
        bigVector.append(wewnetrzne.copy())
        del wewnetrzne[:]
    elif wewnetrzne[x] == 'BM' and (
            x == 56 or x == 58 or x == 60 or x == 62 or x == 49 or x == 51 or x == 53 or x == 55):
        print()
    elif wewnetrzne[x] == 'BM':
        if wewnetrzne[x + 9] == 'WM' and wewnetrzne[x + 18] == 'n' and wewnetrzne[x + 7] == 'WM' and wewnetrzne[x + 14] == 'n':
            wewnetrzne2 = wewnetrzne [:]
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 9] = 'n'
            wewnetrzne[x + 18] = 'BM'
            wiecej_bic_for_one(bigVector, wewnetrzne, x + 18)
            bigVector.append(wewnetrzne.copy())

            wewnetrzne2[x] = 'n'
            wewnetrzne2[x + 7] = 'n'
            wewnetrzne2[x + 14] = 'BM'
            wiecej_bic_for_one(bigVector, wewnetrzne2, x + 14)
            bigVector.append(wewnetrzne2.copy())

        elif wewnetrzne[x + 9] == 'WM' and wewnetrzne[x + 18] == 'n':
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 9] = 'n'
            wewnetrzne[x + 18] = 'BM'
            wiecej_bic_for_one(bigVector, wewnetrzne, x + 18)
            bigVector.append(wewnetrzne.copy())
            del wewnetrzne[:]
            # for z in range(64):
            #     wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
        elif wewnetrzne[x] == 'BM' and wewnetrzne[x + 7] == 'WM' and wewnetrzne[x + 14] == 'n':
            wewnetrzne[x] = 'n'
            wewnetrzne[x + 7] = 'n'
            wewnetrzne[x + 14] = 'BM'
            wiecej_bic_for_one(bigVector, wewnetrzne, x + 14)
            bigVector.append(wewnetrzne.copy())
            del wewnetrzne[:]
            zaszly_zmiany = 1