import random
import collections
"""
        Room 1    Room 2
      _____________________
1:    |_________|_________|
2:    |_________|_________|
3:    |_________|_________|
4;    |_________|_________|


Talks: a, b, c, d, e, f, g, h
Times; 1, 2, 3, 4

rooms = {room1: [], room2: []}

{user_1: [a, b, c, d], user_2: [d, e, f, g]}
"""

ROOM_LIST = ['a','b','c','d','e','f','g','h']
POPULARITY_HASH = {}
# FITNESS_PERCENTS = []
VOTE_LIST = []
USER_DATA = [
 {'user1': ['e', 'd', 'b', 'h']},
 {'user2': ['a', 'h', 'f', 'c']},
 {'user3': ['e', 'h', 'd', 'b']},
 {'user4': ['h', 'd', 'a', 'c']}]

def update():
    for user_data in USER_DATA:
        for user, data in user_data.items():
            update_votes(data)

def update_votes(user_data):
    for vote in user_data:
        VOTE_LIST.append(vote)

def create_model_rooms():
    model = {
    "room1": {1: "",
              2: "",
              3: "",
              4: ""
             },
    "room2": {1: "",
              2: "",
              3: "",
              4: ""
             }
    }

    # for room in ROOM_LIST:
    #     model['room1'] = 

def find_happiness():
    pass

def choose_best_model(room_models):
    pass

def display_vote_count():
    vote_distribution = collections.Counter(VOTE_LIST)
    print(vote_distribution)

update()
display_vote_count()

