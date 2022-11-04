# Write your code here.
from pprint import pprint
def get_number_of_teams() -> int:    
    num_teams = 0
    while(num_teams < 2):
        num_teams = int(input("Enter the number of teams in the tournament: "))
        if num_teams >= 2:
            break
        print("The minimum number of teams is 2, try again.")
    return num_teams

def get_team_names(num_teams) -> list:
    team_names = []
    for team_number in range(num_teams):        
       while(True):
            team_name = input(f"Enter the name for team #{team_number + 1}: ")   
            number_of_words_teams = team_name.split(" ")  
            if len(number_of_words_teams) > 2:
                print("Team names may have at most 2 words, try again.")
                continue
            if len(number_of_words_teams) == 1:
                if(len(number_of_words_teams[0])) <= 1:
                    print("Team names must have at least 2 characters, try again.")
                    continue
            team_names.append(team_name)
            break            
    return team_names

def get_number_of_games_played(num_teams) -> int:
    num_of_games = 0
    while(True):
        num_of_games = int(input("Enter the number of games played by each team: "))
        if num_of_games < num_teams - 1:
            print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
            continue
        break
    return num_of_games

def get_team_wins(team_names, games_played) -> dict:
    team_wins = {}
    for team in team_names:
        while(True):
            num_of_wins = int(input(f"Enter the number of wins Team {team} had:"))
            if num_of_wins > games_played:
                print(f"The maximum number of wins is {games_played}, try again.")
                continue
            if num_of_wins < 0:
                print("The minimum number of wins is 0, try again.")
                continue
            team_wins[team] = num_of_wins
            break
    return team_wins
def pair_teams(team_wins) -> str:
    team_wins_sorted = sorted(team_wins.items(), key = lambda item : item[1])
    game_generated_str = ""
    for idx in range(len(team_wins_sorted)//2):
        game_generated_str +=  'Home: ' +  team_wins_sorted[idx][0] + ' VS Away: ' + team_wins_sorted[-(idx+1)][0] + '\n'
    return game_generated_str
    
# It is not necessary to use the functions defined above. There are simply here
# to help give your code some structure and provide a starting point.
num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
games_played = get_number_of_games_played(num_teams)
team_wins = get_team_wins(team_names, games_played)
print("Generating the games to be played in the first round of the tournament...")
pairing = pair_teams(team_wins)
print(pairing)