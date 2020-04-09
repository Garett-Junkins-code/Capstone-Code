import random
import csv

#dictionaries will hold teams records
#have dict for each division
# will only have team and number of wins 

#AL
al = {} #will only be used to determine the wild card teams and playoff postitioning

alEast = {
    "BAL": 0,
    "BOS": 0,
    "NYY": 0,
    "TBD": 0,
    "TOR": 0
    }

alCentral = {
    "CWS": 0,
    "CLE": 0,
    "DET": 0,
    "KCR": 0,
    "MIN": 0
}

alWest = {
    "HOU": 0,
    "ANA": 0,
    "OAK": 0,
    "SEA": 0,
    "TEX": 0
}

#NL

nl = {}#same as al

nlEast = {
    "ATL": 0,
    "MIA": 0,
    "NYM": 0,
    "PHI": 0,
    "WAS": 0
}

nlCentral = {
    "CHC": 0,
    "CIN": 0,
    "MIL": 0,
    "PIT": 0,
    "STL": 0
}

nlWest = {
    "ARI": 0,
    "COL": 0,
    "LAD": 0,
    "SDP": 0,
    "SFG": 0
}

def add_win(teamName): #adds win to winning teams dictionary
    # have to do this for each dictionary
    #alEast
    for x in alEast:
        y = alEast.get(x)
        if teamName == x:
            alEast[x] = y + 1
            break
    #alCentral
    for x in alCentral:
        y = alCentral.get(x)
        if teamName == x:
            alCentral[x] = y + 1
            break
    #alWest
    for x in alWest:
        y = alWest.get(x)
        if teamName == x:
            alWest[x] = y + 1
            break
    #nlEast
    for x in nlEast:
        y = nlEast.get(x)
        if teamName == x:
            nlEast[x] = y + 1
            break
    #nlCentral
    for x in nlCentral:
        y = nlCentral.get(x)
        if teamName == x:
            nlCentral[x] = y + 1
            break
    #nlwest
    for x in nlWest:
        y = nlWest.get(x)
        if teamName == x:
            nlWest[x] = y + 1
            break


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

    if ht_era < 3.80:
        ht_win = ht_win + 5
        vt_win = vt_win - 5

    if ht_era > 4.50:
        ht_win = ht_win - 5
        vt_win = vt_win + 5

    if ht_era > 4.75:
        ht_win = ht_win - 5
        vt_win = vt_win + 5

    if ht_era > 5.00:
        ht_win = ht_win - 5
        vt_win = vt_win + 5

    #vt_era

    if vt_era < 4.25:
        ht_win = ht_win - 5
        vt_win = vt_win + 5

    if vt_era < 4.00:
        ht_win = ht_win - 5
        vt_win = vt_win + 5

    if vt_era < 3.80:
        ht_win = ht_win - 5
        vt_win = vt_win + 5

    if vt_era > 4.50:
        ht_win = ht_win - 5
        vt_win = vt_win + 5

    if vt_era > 4.75:
        ht_win = ht_win - 5
        vt_win = vt_win + 5

    if vt_era > 5.00:
        ht_win = ht_win - 5
        vt_win = vt_win + 5

    v = random.randrange(0, 100)
    print('---------')
    print ('ht_win:')
    print (ht_win)
    print ('vt_win:')
    print (vt_win)
    print ('victory number:')
    print (v)

    if v <=  ht_win:
        return('ht')
    #elif ht_win < v:
        #return('vt')
    else: 
        return('vt')

def get_stats(team): #gets stats for each team
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
                print(home_team.name + 'vs' + visitingteam.name)
                if z == 'ht':
                    print (home_team.name)
                    add_win(home_team.name) #add win to winning team
                elif z == 'vt':
                    print (visitingteam.name)
                    add_win(home_team.name) #add win to winning team
                else:
                    print ('nobody won so something is wrong')
                
        print('AL East:')        
        print(alEast)
        print('AL Central:')
        print(alCentral)
        print('AL West:')
        print(alWest)
        print('NL East:')
        print(nlEast)
        print('NL Central:')
        print(nlCentral)
        print('NL West:')
        print(nlWest)





#post season

                

    




#testing
season()