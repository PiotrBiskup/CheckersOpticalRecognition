def CreateTemps(chessboard, bigVector, tempboard):                         #magiczna funkcja tworzenia tablic mozliwych ruchow
    for x in chessboard:
        tempboard.append(chessboard.gameTiles[x].pieceOnTile.toString())
    bigVector.append(tempboard)

def Compare(chessboard, bigVector):                                          #mniej magiczna funkcja sprawdzajaca obecny stan z tablicami
    #obecna = []
    #for x in chessboard():
    #    obecna.append(chessboard.gameTiles[x].pieceOnTile.toString())
    for y in bigVector:
        if chessboard == y:
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

        if chessboard.gameTiles[x].pieceOnTile.toString() == 'M':
            if x == 7 or x == 23 or x == 39 or x == 55:
                if chessboard.gameTiles[x + 7].pieceOnTile.toString() == '-':
                    wewnetrzne[x] = '-'
                    wewnetrzne[x + 7] = 'M'
                    zaszly_zmiany = 1
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
            elif x == 8 or x == 24 or x == 40:
                if chessboard.gameTiles[x + 9].pieceOnTile.toString() == '-':
                    wewnetrzne[x] = '-'
                    wewnetrzne[x + 9] = 'M'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    zaszly_zmiany = 1
            elif x == 56 or x == 58 or x == 60 or x == 62:
                pass

            else:
                if chessboard.gameTiles[x + 9].pieceOnTile.toString() == '-':
                    wewnetrzne[x] = '-'
                    wewnetrzne[x + 9] = 'M'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    for z in range(64):
                        wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
                if chessboard.gameTiles[x + 7].pieceOnTile.toString() == '-':
                    wewnetrzne[x] = '-'
                    wewnetrzne[x + 7] = 'M'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    zaszly_zmiany = 1

        elif chessboard.gameTiles[x].pieceOnTile.toString() == 'm':
            if x == 8 or x == 24 or x == 40 or x==56:
                if chessboard.gameTiles[x - 7].pieceOnTile.toString() == '-':
                    wewnetrzne[x] = '-'
                    wewnetrzne[x - 7] = 'm'
                    zaszly_zmiany = 1
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
            elif x == 55 or x == 23 or x == 39:
                if chessboard.gameTiles[x - 9].pieceOnTile.toString() == '-':
                    wewnetrzne[x] = '-'
                    wewnetrzne[x - 9] = 'm'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    zaszly_zmiany = 1
            elif x == 1 or x == 3 or x == 5 or x == 6:
                print()

            else:
                if x>8 and chessboard.gameTiles[x - 9].pieceOnTile.toString() == '-':
                    wewnetrzne[x] = '-'
                    wewnetrzne[x - 9] = 'm'
                    bigVector.append(wewnetrzne.copy())
                    del wewnetrzne[:]
                    for z in range(64):
                        wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
                if chessboard.gameTiles[x - 7].pieceOnTile.toString() == '-':
                    wewnetrzne[x] = '-'
                    wewnetrzne[x - 7] = 'm'
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

        if wewnetrzne[x] == 'M' and (x == 7 or x == 23 or x == 39 or x == 14 or x == 30 or x == 46) and wewnetrzne[x + 7] == 'm' and wewnetrzne[x + 14] == '-':
                        wewnetrzne[x] = '-'
                        wewnetrzne[x + 7] = '-'
                        wewnetrzne[x+14] = 'M'
                        zaszly_zmiany = 1
                        wiecej_bic_for_one(bigVector, wewnetrzne,x+14)
                        bigVector.append(wewnetrzne.copy())
                        del wewnetrzne[:]
        elif wewnetrzne[x] == 'M' and (x == 8 or x == 24 or x == 40 or x==1 or x==17 or x==33) and wewnetrzne[x + 9] == 'm' and wewnetrzne[x + 18] == '-':
                        wewnetrzne[x] = '-'
                        wewnetrzne[x + 9] = '-'
                        wewnetrzne[x+18]='M'
                        bigVector.append(wewnetrzne.copy())
                        wiecej_bic_for_one(bigVector, wewnetrzne, x + 18)
                        del wewnetrzne[:]
                        zaszly_zmiany = 1
        elif wewnetrzne[x] == 'M' and (x == 56 or x == 58 or x == 60 or x == 62 or x==49 or x==51 or x==53 or x ==55):
            print()
        elif wewnetrzne[x] == 'M':
            if wewnetrzne[x + 9] == 'm' and wewnetrzne[x + 18] == '-':
                            wewnetrzne[x] = '-'
                            wewnetrzne[x + 9] = '-'
                            wewnetrzne[x + 18] = 'M'
                            bigVector.append(wewnetrzne.copy())
                            wiecej_bic_for_one(bigVector, wewnetrzne, x + 18)
                            del wewnetrzne[:]
                            for z in range(64):
                                wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
            if wewnetrzne[x] == 'M' and wewnetrzne[x + 7] == 'm' and wewnetrzne[x + 14] == '-':
                            wewnetrzne[x] = '-'
                            wewnetrzne[x + 7] = '-'
                            wewnetrzne[x + 14] = 'M'
                            wiecej_bic_for_one(bigVector, wewnetrzne, x + 14)
                            bigVector.append(wewnetrzne.copy())
                            del wewnetrzne[:]
                            zaszly_zmiany = 1

def wiecej_bic_for_one(bigVector, wewnetrzne,x):
    if wewnetrzne[x] == 'M' and (x == 7 or x == 23 or x == 39 or x == 14 or x == 30 or x == 46) and wewnetrzne[x + 7] == 'm' and wewnetrzne[x + 14] == '-':
        wewnetrzne[x] = '-'
        wewnetrzne[x + 7] = '-'
        wewnetrzne[x + 14] = 'M'
        wiecej_bic_for_one(bigVector, wewnetrzne, x + 14)
        bigVector.append(wewnetrzne.copy())
        del wewnetrzne[:]
    elif wewnetrzne[x] == 'M' and (x == 8 or x == 24 or x == 40 or x == 1 or x == 17 or x == 33) and wewnetrzne[x + 9] == 'm' and wewnetrzne[x + 18] == '-':
        wewnetrzne[x] = '-'
        wewnetrzne[x + 9] = '-'
        wewnetrzne[x + 18] = 'M'
        wiecej_bic_for_one(bigVector, wewnetrzne, x + 18)
        bigVector.append(wewnetrzne.copy())
        del wewnetrzne[:]
    elif wewnetrzne[x] == 'M' and (
            x == 56 or x == 58 or x == 60 or x == 62 or x == 49 or x == 51 or x == 53 or x == 55):
        print()
    elif wewnetrzne[x] == 'M':
        if wewnetrzne[x + 9] == 'm' and wewnetrzne[x + 18] == '-' and wewnetrzne[x + 7] == 'm' and wewnetrzne[x + 14] == '-':
            wewnetrzne2 = wewnetrzne [:]
            wewnetrzne[x] = '-'
            wewnetrzne[x + 9] = '-'
            wewnetrzne[x + 18] = 'M'
            wiecej_bic_for_one(bigVector, wewnetrzne, x + 18)
            bigVector.append(wewnetrzne.copy())

            wewnetrzne2[x] = '-'
            wewnetrzne2[x + 7] = '-'
            wewnetrzne2[x + 14] = 'M'
            wiecej_bic_for_one(bigVector, wewnetrzne2, x + 14)
            bigVector.append(wewnetrzne2.copy())

        elif wewnetrzne[x + 9] == 'm' and wewnetrzne[x + 18] == '-':
            wewnetrzne[x] = '-'
            wewnetrzne[x + 9] = '-'
            wewnetrzne[x + 18] = 'M'
            wiecej_bic_for_one(bigVector, wewnetrzne, x + 18)
            bigVector.append(wewnetrzne.copy())
            del wewnetrzne[:]
            # for z in range(64):
            #     wewnetrzne.append(chessboard.gameTiles[z].pieceOnTile.toString())
        elif wewnetrzne[x] == 'M' and wewnetrzne[x + 7] == 'm' and wewnetrzne[x + 14] == '-':
            wewnetrzne[x] = '-'
            wewnetrzne[x + 7] = '-'
            wewnetrzne[x + 14] = 'M'
            wiecej_bic_for_one(bigVector, wewnetrzne, x + 14)
            bigVector.append(wewnetrzne.copy())
            del wewnetrzne[:]
            zaszly_zmiany = 1