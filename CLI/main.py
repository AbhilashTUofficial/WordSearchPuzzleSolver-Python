from solver import PuzzleSolver

def main(i):
    solve = PuzzleSolver(puzzles[i], answers[i])
    # solve.horiCheck(puzzles[i], answers[i])
    # solve.vertCheck(puzzles[i], answers[i])
    solve.diagCheck(puzzles[i], answers[i])
    solve.disResult()


if __name__ == '__main__':


    # puzzles<list> will store the charecters in the puzzle
    puzzles = [
        [
            ['w', 'f', 'b', 's', 'w'],
            ['e', 'i', 'r', 'e', 'a'],
            ['t', 's', 'e', 'a', 't'],
            ['w', 'h', 'a', 'l', 'e'],
            ['b', 'l', 'u', 'e', 'r']
        ],
        [
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
    ]
    # answers<list> will store all possible answers
    answers = [
        ['aes', 'blue', 'fish', 'whale', 'water', 'wet', 'seal'],
        ['bat','fish','hedgehog','badger','ostrich','cheetah','bear','eel',
        'dolphin','rat','ant','zebra']
        ]

    main(1)