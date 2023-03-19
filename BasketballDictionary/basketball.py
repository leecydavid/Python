# Challenge 1: Update the Constructor
# Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.

class Player:
    def __init__(self, player_data):
        self.name = player_data['name']
        self.age = player_data['age']
        self.position = player_data['position']
        self.team = player_data['team']

# Challenge 2: Create instances using individual player dictionaries.
    # Given these variables, create Player instances for each of the following dictionaries.
    # Be sure to instantiate these outside the class definition, in the outer scope.

    def __repr__(self):
        return (f"Player: {self.name}, Age: {self.age}, Pos: {self.position}, Team: {self.team}")


kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets"
}

print(kevin['name'])
player_kevin = Player(kevin)
print(player_kevin)

player_jason = Player(jason)
print(player_jason)

player_kyrie = Player(kyrie)
print(player_kyrie)

# Challenge 3: Make a list of Player instances from a list of dictionaries
# Finally, given the example list of players at the top of this module (the one with many players) 
# write a for loop that will populate an empty list with Player objects from the original list of dictionaries.

players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

# We need to create a for-loop over the dictionaries 
    # each time we loop, we want to use the dictionary info to create a new player instance 
new_team = []
for player_dict in players:
    player = Player(player_dict)
    new_team.append(player)

print(new_team)








