import numpy as np

puzzle = [
            ['v','b','r','e','e','f','i','s','h','r','a','c','h','p'],
            ['a','n','a','c','z','o','c','o','x','i','b','e','e','b'],
            ['a','o','s','t','r','i','c','h','t','e','g','r','d','a'],
            ['i','a','d','d','h','c','h','e','e','t','a','h','g','d'],
            ['b','h','r','o','d','r','y','v','a','n','e','n','e','g'],
            ['e','y','w','d','l','s','a','m','z','l','e','l','h','e'],
            ['a','r','t','p','v','p','r','c','b','o','l','r','o','r'],
            ['r','h','t','o','a','a','h','b','r','o','n','a','g','h'],
            ['c','a','a','x','n','o','r','i','a','z','e','b','r','a'],
            ['r','a','n','y','t','a','e','k','n','i','n','a','w','a']
        ]

answers=[['bat','fish','hedgehog','badger','ostrich','cheetah','bear','eel',
        'dolphin','rat','ant','zebra']]

# [arr.append(i)for i in range(10)  if i==9 ]
sps = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (0, 1),
       (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (0, 13)]



dMax=9

# for i, (_x, _y) in enumerate(sps):
#         diagLenths=[]
#         for j in range(dMax):
#                 diagLenths.append(dMax-(_x+_y))
#                 # diagLenths.insert(0,j)
#         print(diagLenths)

        
#         cmb = ''.join([puzzle[_x+j][_y+j]
#                            for j in [_ for _ in range(dMax-(_x+_y))]])
        
        

# x,y = len(puzzle),len(puzzle[0])
# puzzle = np.array(puzzle)
# print (f"{puzzle}\n")
# diags = [puzzle[::-1,:].diagonal(i) for i in range(-puzzle.shape[0]+1,puzzle.shape[1])]
# diags.extend(puzzle.diagonal(i) for i in range(puzzle.shape[1]-1,-puzzle.shape[0],-1))
# print ([n.tolist() for n in diags])


x,y = len(puzzle),len(puzzle[0])
puzzle = np.array(puzzle)
diags = [puzzle[::-1,:].diagonal(i) for i in range(-puzzle.shape[0]+1,puzzle.shape[1])]
diags.extend(puzzle.diagonal(i) for i in range(puzzle.shape[1]-1,-puzzle.shape[0],-1))


# print([n.tolist() for n in diags])

# cmb=''
# cmb.join([''.join(x) for x in [n for n in diags]])
# print(cmb)

print(''.join([_ for _ in diags][2]))
# for c in [_ for _ in diags]:
#         cmb=''.join(c)
        # for ans in answers[0]:
        #         try:
        #                 print(cmb.index(ans))
        #                 print(cmb)
                        
        #         except:
        #                 pass
