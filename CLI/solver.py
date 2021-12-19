from math import comb


# * answerCoor<list> will store all coordinates of right answer charecters
# * in a tuble : (x,y)
answerCoor = []
# g : green color for answer charecters
# w : red color for extra charecters
g = '\033[92m'
r = '\033[91m'
header='\033[93m'
footer='\033[93m'
class PuzzleSolver:

    def __init__(self, puzzle, answers):

        self.puzzle = puzzle
        self.answers = answers

    

    def checkWordHori(self, answers, x, cmb):
        # Clear all text from log file.
        open('CLI/logs.txt', 'w').write("")
        # ? loop through all words in answers<list>
        for word in answers:
            # ? if the word is not in the layer
            # ? write it to the log file.
            try:
                # ! In Horizontal check `x` value of all the answer chars
                # ! will be same
                # ? beginn ing of the answer word: y = cmb.index(word) or cmb.index(word[::-1])
                # ! Reverse order of the answer string is also a possibility : word[::-1]
                # ! loop through all answer chars by incrementing y : y+=1
                # ? then remove the word from answers<list>
                try:

                    y = cmb.index(word)
                    for _ in range(len(word)):
                        answerCoor.append((x, y))
                        y += 1

                except:
                    y = cmb.index(word[::-1])
                    for _ in range(len(word)):
                        answerCoor.append((x, y))
                        y += 1

                answers.remove(word)

            except Exception as e:
                log = open('CLI/logs.txt', 'a')
                log.write(f"{e}\n{word} is not in {cmb}")

    def checkWordVert(self, answers, y, cmp):
        # Clear all text from log file.
        open('CLI/logs.txt', 'w').write("")
        # ? loop through all words in answers<list>
        for word in answers:
            # ? if the word is not in the layer
            # ? write it to the log file.
            try:
                # ! In Vertical check `y` value of all the answer chars
                # ! will be same :
                # ! x = cmb.index(word) or cmb.index(word[::-1])
                # ! Reverse order of the answer string is also a possibility : word[::-1]
                # ! loop through all answer chars by incrementing x : x+=1
                # ? then remove the word from answers<list>
                try:

                    x = cmp.index(word)
                    for _ in range(len(word)):
                        answerCoor.append((x, y))
                        x += 1
                except:
                    x = cmp.index(word[::-1])
                    for _ in range(len(word)):
                        answerCoor.append((x, y))
                        x += 1
                answers.remove(word)

            except Exception as e:
                log = open('CLI/logs.txt', 'a')
                log.write(f"{e}\n{word} is not in {cmp}")

    def checkWordDiag(self, answers, y, cmp):
        open('CLI/logs.txt', 'w').write("")
        for word in answers:
            try:

                try:
                    answerCoor.append(
                        [(cmp.index(word), y), (cmp.index(word)+len(word)-1, y)])
                except:
                    answerCoor.append(
                        [(cmp.index(word[::-1]), y), (cmp.index(word[::-1])+len(word)-1, y)])
                answers.remove(word)

            except Exception as e:
                log = open('CLI/logs.txt', 'a')
                log.write(f"{e}\n{word} is not in {cmp}")


    def disResult(self):
        # ? disResult will loop through all charecters `puzzle[x][y]`
        # ? and check whether it's a answer char or a extra char
        # ? if it's answer Char : print in green color
        # ? hence,              : print in red color
        # ? then remove it from answerCoor<list>

        print(f"\n\t{header} PUZZLE COMPLETE\n")

        for x in range(len(self.puzzle)):
            for y in range(len(self.puzzle[0])):
                if((x, y) in answerCoor):
                    print(f'{g}{self.puzzle[x][y].capitalize()}', end='\t')
                    answerCoor.remove((x, y))
                else:
                    print(f'{r}{self.puzzle[x][y].capitalize()}', end='\t')

            print("\n")
        print(f'\t{footer}Unsolved words: {len(self.answers)}\n')

    def horiCheck(self, puzzle, answers):
        # ? In horizontal check all the combinations will
        # ? start at puzzle[-][0]
        # ? loop through all layers, join the chartecters to a string
        # ? pass the string checkWordHori() for check whether the word
        # ? is in it or not

        for i, w in enumerate(puzzle):
            cmb = ''.join(w)
            self.checkWordHori(answers, i, cmb)

    def vertCheck(self, puzzle, answers):
        # ? In vertical check all the combinations will
        # ? start at puzzle[0][-]
        # ? loop through all layers, join the chartecters to a string
        # ? pass the string checkWordVert() for check whether the word
        # ? is in it or not

        for j in range(len(puzzle[0])):
            cmb = ''.join([puzzle[i][j] for i in range(len(puzzle))])
            self.checkWordVert( answers, j, cmb)

    def diagCheck(self, puzzle, answers):

        # ! Positive diagonal
        # ? top-left to bottom-right
        # ? dMax<int> : The maximum length of the diagonal
        dMax = min(len(puzzle), len(puzzle[0]))
        _y = 0
        # ? Starting Points : sps
        sps = [(_, 0)for _ in range(len(puzzle))]+[(0, _)
                                                   for _ in range(1, len(puzzle[0]))]
        print(sps)

        for i, (_x, _y) in enumerate(sps):
            diagLenths=[]
            cmb = ''.join([puzzle[_x+j][_y+j]
                           for j in [_ for _ in range(dMax-(_x+_y))]])

            for word in answers:
                try:

                    try:

                        if (i < len(puzzle)):
                            x = i
                            y = cmb.index(word)
                            for _ in range(len(word)):
                                answerCoor.append((x, y))
                                y += 1
                        else:
                            y = len(puzzle[0])-i
                            x = cmb.index(word)
                            for _ in range(len(word)):
                                answerCoor.append((x, y))
                                x += 1

                    except:
                        if (i < len(puzzle)):
                            x = i
                            y = cmb.index(word[::-1])
                            for _ in range(len(word)):
                                answerCoor.append((x, y))
                                y += 1

                        else:
                            y = len(puzzle[0])-i
                            x = cmb.index(word[::-1])
                            for _ in range(len(word)):
                                answerCoor.append((x, y))
                                x += 1

                    answers.remove(word)

                except Exception as e:
                    log = open('CLI/logs.txt', 'a')
                    log.write(f"{e}\n{word} is not in {cmb}")

        # print(answerCoor)



