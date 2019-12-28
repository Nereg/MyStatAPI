import API
token = API.getKey('YOUR_PASSWORD','YOUR_USERNAME')
print('Your token : {}'.format(token))
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
