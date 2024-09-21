from utils import printOrder, printSample

# All members of the league
league_members = ["Isaac", "June", "Sam", "Andrew", "London", "Chris D", "Chris R", "Hannah", "Jason", "Shashank"]

# League members who can not have first overall pick
last_year_playoff_teams = ["Isaac", "June", "Andrew", "London"]

# Sample the order generation a large number of times to prove randomness
printSample(league_members, last_year_playoff_teams, 100000000, picks=3)

# Print the official order using a seed
# this ensures that I couldn't keep generating an order until I got one I liked
printOrder(league_members, last_year_playoff_teams, picks=3, seed="The Mighty Drunks, Season 5")
