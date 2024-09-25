team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451

def result(score_1, score_2, team1_time, team2_time):
    result = None
    if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
        result = 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
        result = 'Победа команды Волшебники Данных!'
    else:
        result = 'Ничья!'
    return result

def total_avg(score_1, score_2, team1_time, team2_time):
    total_avg = (team1_time + team2_time) / (score_1 + score_2)
    return total_avg

print('В команде Мастера кода участников: %s' % (team1_num) + '!')
print('Итого сегодня в командах участников: %(num1)s и %(num2)s' % {'num1': team1_num, 'num2': team2_num} + '!')
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('Волшебники данных решили задачи за {}c!'.format(team2_time))
print(f'Команды решили {score_1} и {score_2} задач')
print(f'Результат битвы: {result(score_1, score_2, team1_time, team2_time)}')
print(f'Сегодня было решено {score_1 + score_2} задач, в среднем по {round(total_avg(score_1, score_2, team1_time, team2_time), 2)} секунды на задачу!')