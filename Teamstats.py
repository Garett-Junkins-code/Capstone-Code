import random
import csv

def sim_game(ht_ops, ht_era, vt_ops, vt_era): #ht is home team vt is visting team
    #make the variable a float
    ht_ops = float(ht_ops)
    ht_era = float(ht_era)
    vt_ops = float(vt_ops)
    vt_era = float(vt_era)
    #.757 is league average OPS
    #4.49 is league average ERA
    ht_win = 50 
    vt_win = 50 
    #winning percantage bracket

    #ht_ops

    if ht_ops > .775:
        ht_win = ht_win + 5
        vt_win = vt_win - 5

    if ht_ops > .800:
        ht_win = ht_win + 5
        vt_win = vt_win - 5

    if ht_ops > .825:
        ht_win = ht_win + 5
        vt_win = vt_win - 5

    if ht_ops < .775:
        ht_win = ht_win - 5
        vt_win = vt_win + 5

    if ht_ops < .740:
        ht_win = ht_win - 5
        vt_win = vt_win + 5

    if ht_ops < .710:
        ht_win = ht_win - 5
        vt_win = vt_win + 5

    #vt_ops

    if vt_ops > .775:
        ht_win = ht_win - 5
        vt_win = vt_win + 5

    if vt_ops > .800:
        ht_win = ht_win - 5
        vt_win = vt_win + 5

    if vt_ops > .825:
        ht_win = ht_win - 5
        vt_win = vt_win + 5

    if vt_ops < .775:
        ht_win = ht_win + 5
        vt_win = vt_win - 5

    if vt_ops < .740:
        ht_win = ht_win + 5
        vt_win = vt_win - 5

    if vt_ops < .710:
        ht_win = ht_win + 5
        vt_win = vt_win - 5

    #ht_era

    if ht_era < 4.25:
        ht_win = ht_win + 5
        vt_win = vt_win - 5

    if ht_era < 4.00:
        ht_win = ht_win + 5
        vt_win = vt_win - 5

    if ht_era < 3.50:
        ht_win = ht_win + 5
        vt_win = vt_win - 5

    if ht_era > 4.50:
        ht_win = ht_win - 5
        vt_win = vt_win + 5

    if ht_era > 5.00:
        ht_win = ht_win - 5
        vt_win = vt_win + 5

    if ht_era > 6.00:
        ht_win = ht_win - 5
        vt_win = vt_win + 5

    #vt_era

    if vt_era < 4.25:
        ht_win = ht_win - 5
        vt_win = vt_win + 5

    if vt_era < 4.00:
        ht_win = ht_win - 5
        vt_win = vt_win + 5

    if vt_era < 3.50:
        ht_win = ht_win - 5
        vt_win = vt_win + 5

    if vt_era > 4.50:
        ht_win = ht_win - 5
        vt_win = vt_win + 5

    if vt_era > 5.00:
        ht_win = ht_win - 5
        vt_win = vt_win + 5

    if vt_era > 6.00:
        ht_win = ht_win - 5
        vt_win = vt_win + 5

    v = random.randrange(0, 100)
    if ht_win <= v:
        return('hometeam')
    else:
        return('Vistingteam')

def get_stats(team):
    with open('UsefulTeamStats.csv') as stats:
        statscsv = csv.reader(stats)
        for row in statscsv:
            if row[0] == team:
                teamstats = [row[0], row[1], row[2]]
            else:
                continue
        return teamstats
    

class Team: #team class will be home team and road team, 
    def __init__(self, name, ops, era):
        self.name = name
        self.ops = ops
        self.era = era

def season():
    with open('2020MLBschedule.csv') as schedule:
        schedulecsv = csv.reader(schedule)
        for row in schedulecsv: #each row is a day of games
            for col in row: # each column is a game being played
                x = col
                if x == "": #have to add this because some days dont have the same number of games, those parts of the csv are empty and i dont want error
                    break
                game = x.split("@")
                vt = game[0] #vt is the visting team
                ht = game[1] #ht is home team

                #now get teams stats
                visitors = get_stats(vt)
                hometeam = get_stats(ht)

                #make team objects
                visitingteam = Team(visitors[0], visitors[1], visitors[2])

                home_team = Team(hometeam[0], hometeam[1], hometeam[2])


                #simgame
                z = sim_game(home_team.ops, home_team.era, visitingteam.ops, visitingteam.era)
                if z == 'hometeam':
                    print (home_team.name)
                elif z == 'visitingteam':
                    print (visitingteam.name)
                else:
                    print ('nobody won so something is wrong')



#post season

                

    




#testing
season()
