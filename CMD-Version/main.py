import numpy as np


puzzle = [
    ['w', 'f', 'b', 's', 'w'],
    ['e', 'i', 'r', 'e', 'a'],
    ['t', 's', 'e', 'a', 't'],
    ['w', 'h', 'a', 'l', 'e'],
    ['b', 'l', 'u', 'e', 'r']
]
answers = ['aes', 'blue', 'fish', 'whale', 'water', 'wet', 'seal']
answerCoor = []
g = '\033[92m'
w = '\033[97m'


def getAllCoors():
    allCoors = [[]]
    i = 0
    # for start,end in answerCoor:
    #     allCoors[i].insert(0,start)
    #     x0,y0=start
    #     x1,y1=end
    #     for x in range(len(puzzle)):
    #         for y in range(len(puzzle[0])):
    #             if(x0-x1)*(y0-y)==(x1-x)*(y0-y1):
    #                 allCoors[i].append((x,y))
    #     allCoors[i].append(end)
    for start, end in [[(0, 0), (0, 2)], [(0, 1), (1, 2)], [(0, 2), (2, 2)]]:
        allCoors.append([start])
        x0, y0 = start
        x1, y1 = end
        for x in range(3):
            for y in range(3):
                if(x0-x1)*(y0-y) == (x1-x)*(y0-y1):
                    allCoors[i].append((x, y))
        # allCoors[i].append(end)
        i += 1

    print(allCoors)


def disResult():
    getAllCoors()
    # ans=0
    # for i in range(len(puzzle)):
    #     print("\n")
    #     for j in range(len(puzzle[0])):
    #         if(i>=answerCoor[ans][0][0] and i<=answerCoor[ans][1][0]):
    #             print(f'{g}{puzzle[i][j]}',end="\t")
    #             if(ans<2):
    #                 ans+=1
    #         else:
    #             print(f'{w}{puzzle[i][j]}',end="\t")


def horiCheck():
    for i, x in enumerate(puzzle):
        cmp = ''.join(x)
        checkWordHori(i, cmp)


def vertCheck():

    for j in range(len(puzzle[0])):
        cmp = ''.join([puzzle[i][j] for i in range(len(puzzle))])
        checkWordVert(j, cmp)


def diagCheck():
    for i, x in enumerate(puzzle):
        cmp = ''.join(x)
        checkWordDiag(i, cmp)

    print(answerCoor)


def checkWordHori(x, cmp):
    open('CMD-Version/logs.txt', 'w').write("")
    for word in answers:
        try:

            try:
                answerCoor.append(
                    [(x, cmp.index(word)), (x, cmp.index(word)+len(word)-1)])
            except:
                answerCoor.append(
                    [(x, cmp.index(word[::-1])), (x, cmp.index(word[::-1])+len(word)-1)])
            answers.remove(word)

        except Exception as e:
            log = open('CMD-Version/logs.txt', 'a')
            log.write(f"{e}\n{word} is not in {cmp}")


def checkWordVert(y, cmp):
    open('CMD-Version/logs.txt', 'w').write("")
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
            log = open('CMD-Version/logs.txt', 'a')
            log.write(f"{e}\n{word} is not in {cmp}")


def checkWordDiag(y, cmp):
    open('CMD-Version/logs.txt', 'w').write("")
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
            log = open('CMD-Version/logs.txt', 'a')
            log.write(f"{e}\n{word} is not in {cmp}")


def main():
    horiCheck()
    vertCheck()
    # checkWordDiag()
    disResult()


if __name__ == '__main__':
    main()
