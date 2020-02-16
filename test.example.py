import API
import time
password = 'YOUR_PASSWORD'
username = 'YOUR_USERNAME'
token = API.getKey(password,username)
print('Your token : {}'.format(token[0]))
print('Your refresh token : {}'.format(token[1]))
refreshed = API.RefreshToken(token[1])
print('Your refreshed access token: {}'.format(refreshed[0]))
print('Your refresh token : {}'.format(refreshed[1]))
timing = API.getRefreshTime(password,username)
print('Your access token will expire :{}'.format(time.ctime(int(timing[0]))))
print('Your refresh token will expire :{}'.format(time.ctime(int(timing[1]))))
token = token[0]
name = API.GetUserData(token)['full_name']
leaderboard = API.GetClassLeaderboard(token)
print('-------------------- Таблица лидеров группы --------------------')
for place in leaderboard:
    print('Место {}: {} Очков: {}'.format(place['position'],place['full_name'],place['amount']))
leaderboard = API.GetStreamLeaderboard(token)
print(leaderboard)
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
print('Всего домашек: {} , сделанных: {} , просроченных: {} , текущих: {}'.format(get[0],get[1],get[2],get[3]))
future = API.GetFutureExsams(token)
for exam in future:
    print('Так у тебя {} Когда ? Да вот {}'.format(exam['spec'],exam['date']))
