#• Read the football data from cfb.csv using Pandas.
import pandas as pd
CFBData = pd.read_csv('cfb.csv')

#Create a Python program that allows a user to explore college football results from
#the provided CSV file.
#Your program should ask the user which season they would like to analyze. It
print("Welcome to the College Football Results Analyzer!")
#• Allow the user to select a season.
season = int(input("Enter the season you would like to analyze (e.g., 2020): "))
#should then organize the teams from that season into four categories:

#• 10 or more wins
#• 8–9 wins
#• 6–7 wins
#• Fewer than 6 wins
if season in CFBData['Season'].values:
    data = CFBData[CFBData['Season'] == season]
    #• Use a dictionary to organize the teams into the four win categories.
    win_categories = {
        "10 or more wins": [],
        "8–9 wins": [],
        "6–7 wins": [],
        "Fewer than 6 wins": []
    }
#• Use loops and selection to process the teams.
    for index, row in data.iterrows():
        wins = row['Win']
        team_name = row['Team']

        if wins >= 10:
            win_categories["10 or more wins"].append(team_name)
        elif 8 <= wins <= 9:
            win_categories["8–9 wins"].append(team_name)
        elif 6 <= wins <= 7:
            win_categories["6–7 wins"].append(team_name)
        else:
            win_categories["Fewer than 6 wins"].append(team_name)

    # Display the teams in each category
    for category, teams in win_categories.items():
        print(f"\n{category}:")
        if teams:
            for team in teams:
                print(f"- {team}")
        else:
            print("No teams in this category.")
    #• Let the user know if the requested season is not found.
else:
    print(f"No data available for the {season} season.")

#Display the teams in each category clearly for the user. 
# Your program should:
#• Work with any season included in the CSV file.
#• Avoid hard-coding the team names or results.