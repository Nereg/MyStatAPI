import API
token = API.getKey('PASSWORD','USERNAME')
print('Your token : {}'.format(token))
print('Your refresh token : {}'.format(token[1]))
token = token[0]
name = API.GetUserData(token)['full_name']
leaderboard = API.GetClassLeaderboard(token)
print('-------------------- Таблица лидеров группы --------------------')
for place in leaderboard:
    print('Место {}: {} Очков: {}'.format(place['position'],place['full_name'],place['amount']))
leaderboard = API.GetStreamLeaderboard(token)
#print(leaderboard)
print('-------------------- Таблица лидеров потока --------------------')
for place in leaderboard:
    print('Место {}: {}'.format(place['position'],place['full_name']))
print('-------------------- Информация о пользователе --------------------')
user = API.GetUserData(token)
print('Ваша имя: {}'.format(user['full_name']))
print('Ваш уровень: {}'.format(user['level']))
print('Ссылочка на фотку: {}'.format(user['photo']))
points = API.GetPoints(token)
print('У вас {} коинов , {} алмазиков и {} очков'.format(points[1],points[0],points[2]))
print('У вас {} ачивок.'.format(user['achieves_count']))
get = API.GetHomeworks(token)
print('Всего домашек: {} , сделанных: {} , просроченных: {}'.format(get[0],get[1],get[2]))
future = API.GetFutureExsams(token)
for exam in future:
    print('Так у тебя {} Когда ? Да вот {}'.format(exam['spec'],exam['date']))
