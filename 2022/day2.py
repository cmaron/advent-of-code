MOVE_DATA = {
    'A': {'name': 'Rock',     'beats': 'Z', 'beaten_by': 'B', 'score': 1},
    'B': {'name': 'Paper',    'beats': 'X', 'beaten_by': 'C', 'score': 2},
    'C': {'name': 'Scissors', 'beats': 'Y', 'beaten_by': 'A', 'score': 3},
    'X': {'name': 'Rock',     'beats': 'C', 'beaten_by': 'Y', 'score': 1},
    'Y': {'name': 'Paper',    'beats': 'A', 'beaten_by': 'Z', 'score': 2},
    'Z': {'name': 'Scissors', 'beats': 'B', 'beaten_by': 'X', 'score': 3},
}

WIN_SCORE = 6
TIE_SCORE = 3
LOSE_SCORE = 0

DRAW = 3


def day2a(file_name):
    total_score = 0
    with open(file_name) as f:
        for line in f:
            opponent_move, suggested_move = line.strip().split()
            opponent_move_data = MOVE_DATA[opponent_move]
            suggested_move_data = MOVE_DATA[suggested_move]
            total_score += suggested_move_data['score']
            if opponent_move_data['name'] == suggested_move_data['name']:
                total_score += TIE_SCORE
            elif suggested_move_data['beats'] == opponent_move:
                total_score += WIN_SCORE

    print(total_score)


def day2b(file_name):
    total_score = 0
    with open(file_name) as f:
        for line in f:
            opponent_move, outcome = line.strip().split()
            opponent_move_data = MOVE_DATA[opponent_move]

            target_move = opponent_move_data['beaten_by']
            if outcome == 'X':  # lose
                total_score += LOSE_SCORE
                target_move = opponent_move_data['beats']
            elif outcome == 'Y':  # draw
                total_score += TIE_SCORE
                target_move = opponent_move
            else:  # win
                total_score += WIN_SCORE

            target_move_data = MOVE_DATA[target_move]
            total_score += target_move_data['score']

    print(total_score)


if __name__ == '__main__':
    day2a('day2.txt')
    day2b('day2.txt')
