# CONSTANTES
    PLAYER_1 = 'A'
    PLAYER_2 = 'B'

    # variables
    pa_points = 0
    pb_points = 0
    pa_sets = 0
    pb_sets = 0
    win_match_a = 0
    win_match_b = 0
    pa_tie_break = 0
    pb_tie_break = 0
    result = ''

    for set_game in points:
        # Sumando cada punto
        if set_game == PLAYER_1:
            pa_points += 1
        elif set_game == PLAYER_2:
            pb_points += 1

        # Victoria fácil (15-50)
        if pa_points >= 4 and pa_points - pb_points >= 2:
            pa_sets += 1
            pa_points = 0
            pb_points = 0
        elif pb_points >= 4 and pb_points - pa_points >= 2:
            pb_sets += 1
            pa_points = 0
            pb_points = 0
        # Filtro q si es empate o no
        if pa_sets == 6 and pb_sets == 6:
            if set_game == PLAYER_1:
                pa_tie_break += 1

            if set_game == PLAYER_2:
                pb_tie_break += 1

        # Sets fácil (1-6)
        if pa_sets >= 6 and pa_sets - pb_sets >= 2:
            result += f'{pa_sets}-{pb_sets} '
            win_match_a += 1
            # Reseteo sets
            pa_sets = 0
            pb_sets = 0
        elif pb_sets >= 6 and pb_sets - pa_sets >= 2:
            result += f'{pa_sets}-{pb_sets} '
            win_match_b += 1
            # Reseteo sets
            pa_sets = 0
            pb_sets = 0

    return result
