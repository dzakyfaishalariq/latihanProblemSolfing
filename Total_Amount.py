def points(games):
    games = [x.split(":") for x in games]
    games = [3 if i[0] > i[1] else 0 if i[0] < i[1] else 1 for i in games]
    return sum(games)


print(points(['1:0', '2:0', '3:0', '4:0', '2:1',
      '3:1', '4:1', '3:2', '4:2', '4:3']))
