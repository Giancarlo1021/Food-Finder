import requests


def results(location, food):
    food_list = [0] * 3, [0] * 3, [0] * 3, [0] * 3, [0] * 3, [0] * 3, [0] * 3, [0] * 3, [0] * 3, [0] * 3

    key = "iezk6GhSPIb0DE_upiTyZWPcsCJgZr3GJKH2mRIFJrQZJbyzIS89NO" \
          "-mgB_z1vKbumXpLHEyA68Jpn5wIMt6OGKnAahiQe9WiJX2mNhRv9kGIq9IDJ149g92A-eFYXYx "

    url = 'https://api.yelp.com/v3/businesses/search'

    headers = {
        "Authorization": 'Bearer %s' % key
    }

    parameters = {
        'location': location,
        'term': food,
        'radius': 7500,
        'limit': 10
    }

    response = requests.get(url, headers=headers, params=parameters)

    restaurant_query = response.json()['businesses']

    for i, j in enumerate(restaurant_query, 0):
        food_list[i][0] = str((j['name']))
        food_list[i][1] = str((j['rating']))
        food_list[i][2] = str((j['url']))

    print('from RR: ', food_list[0][0], '\n', food_list[0][1], '\n', food_list[0][2])

    return food_list

