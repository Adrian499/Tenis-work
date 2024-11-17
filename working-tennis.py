    PLAYER_1 = 'A'
    PLAYER_2 = 'B'
    MIN_PTOS_TO_WIN = 4
    MIN_DIFFERENCE = 2
    MIN_GAMES_TO_WIN_SET = 6
    MIN_PTOS_TIEBREAK = 7
    pa_points = 0
    pb_points = 0
    pa_games = 0
    pb_games = 0
    pa_tie_break = 0
    pb_tie_break = 0
    result = ''

    for set_game in points:
        # Sumando cada punto
        if set_game == PLAYER_1:
            pa_points += 1
        else:
            pb_points += 1

        # Filtro empate o no
        if pa_games == 6 and pb_games == 6:
            if set_game == PLAYER_1:
                pa_tie_break += 1
            elif set_game == PLAYER_2:
                pb_tie_break += 1

            if pa_tie_break >= MIN_PTOS_TIEBREAK and pa_tie_break - pb_tie_break >= MIN_DIFFERENCE:
                pa_games += 1
                result += f'{pa_games}-{pb_games} '
                pa_games = 0
                pb_games = 0
                pa_tie_break = 0
                pb_tie_break = 0
                pa_points = 0
                pb_points = 0
            elif (
                pb_tie_break >= MIN_PTOS_TIEBREAK and pb_tie_break - pa_tie_break >= MIN_DIFFERENCE
            ):
                pb_games += 1
                result += f'{pa_games}-{pb_games} '
                pa_games = 0
                pb_games = 0
                pa_tie_break = 0
                pb_tie_break = 0
                pa_points = 0
                pb_points = 0
        else:
            if pa_points >= MIN_PTOS_TO_WIN and pa_points - pb_points >= MIN_DIFFERENCE:
                pa_games += 1
                pa_points = 0
                pb_points = 0
                pb_tie_break = 0
            elif pb_points >= MIN_PTOS_TO_WIN and pb_points - pa_points >= MIN_DIFFERENCE:
                pb_games += 1
                pa_points = 0
                pb_points = 0
                pb_tie_break = 0
            # Sets fácil (1-6)
            if pa_games >= MIN_GAMES_TO_WIN_SET and pa_games - pb_games >= MIN_DIFFERENCE:
                result += f'{pa_games}-{pb_games} '
                # Reseteo sets
                pa_games = 0
                pb_games = 0
            elif pb_games >= MIN_GAMES_TO_WIN_SET and pb_games - pa_games >= MIN_DIFFERENCE:
                result += f'{pa_games}-{pb_games} '
                # Reseteo sets
                pa_games = 0
                pb_games = 0
