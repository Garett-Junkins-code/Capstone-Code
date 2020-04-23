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

    vn = random.randrange(0, 100)
    #print('---------')
    #print ('ht_win:')
    #print (ht_win)
    #print ('vt_win:')
    #print (vt_win)
    #print ('victory number:')
    #print (vn)

    if vn <=  ht_win:
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
                #print(home_team.name + 'vs' + visitingteam.name)
                if z == 'ht':
                    #print (home_team.name)
                    add_win(home_team.name) #add win to winning team
                elif z == 'vt':
                    #print (visitingteam.name)
                    add_win(visitingteam.name) #add win to winning team
                else:
                    print ('nobody won so something is wrong')
                
        #print('AL East:')        
        #print(alEast)
        #print('AL Central:')
        #print(alCentral)
        #print('AL West:')
        #print(alWest)
        #print('NL East:')
        #print(nlEast)
        #print('NL Central:')
        #print(nlCentral)
        #print('NL West:')
        #print(nlWest)

        
        #post season teams will be put in lists depending on thier record to see who plays who
        #index 0 thru 2 are division winners 0 = best record 1 = second best 2 = third best 3 and 4 are wild card teams
        #index 3 and 4 WC winner becomes 3
        #index 0 vs 3 and 1 vs 2 in DS winners are then 0 and 1
        #index 0 vs 1 in CS
        #then winners of both play in WS

        #division winners

        #ALeast
        leader = 0
        for team, wins in alEast.items():
            t = wins
            if t > leader:
                leader = t
                ALE_leader = [team, leader]
            else:
                continue
        del alEast[ALE_leader[0]]
        
        #ALcentral
        leader = 0
        for team, wins in alCentral.items():
            t = wins
            if t > leader:
                leader = t
                ALC_leader = [team, leader]
            else:
                continue
        del alCentral[ALC_leader[0]]
        
        #ALwest
        leader = 0
        for team, wins in alWest.items():
            t = wins
            if t > leader:
                leader = t
                ALW_leader = [team, leader]
            else:
                continue
        del alWest[ALW_leader[0]]
        
        #NLeast
        leader = 0
        for team, wins in nlEast.items():
            t = wins
            if t > leader:
                leader = t
                NLE_leader = [team, leader]
            else:
                continue
        del nlEast[NLE_leader[0]]
        
        #NLcentral
        leader = 0
        for team, wins in nlCentral.items():
            t = wins
            if t > leader:
                leader = t
                NLC_leader = [team, leader]
            else:
                continue
        del nlCentral[NLC_leader[0]]
        
        #NLwest
        leader = 0
        for team, wins in nlWest.items():
            t = wins
            if t > leader:
                leader = t
                NLW_leader = [team, leader]
            else:
                continue
        del nlWest[NLW_leader[0]]

        #add teams to al and nl dicts
        #al
        for team, wins in alEast.items():
            al[team] = wins
        for team, wins in alCentral.items():
            al[team] = wins
        for team, wins in alWest.items():
            al[team] = wins
        #nl
        for team, wins in nlEast.items():
            nl[team] = wins
        for team, wins in nlCentral.items():
            nl[team] = wins
        for team, wins in nlWest.items():
            nl[team] = wins

        # get wildcard teams
        #alWC1
        ALWCteam1 = 0
        for team, wins in al.items():
            t = wins
            if t > ALWCteam1:
                ALWCteam1 = t
                ALWildcard1 = [team, ALWCteam1]
            else:
                continue
        del al[ALWildcard1[0]]
        #alWC2
        ALWCteam2 = 0
        for team, wins in al.items():
            t = wins
            if t > ALWCteam2:
                ALWCteam2 = t
                ALWildcard2 = [team, ALWCteam2]
            else:
                continue
        del al[ALWildcard2[0]]

        #nlWC1
        NLWCteam1 = 0
        for team, wins in nl.items():
            t = wins
            if t > NLWCteam1:
                NLWCteam1 = t
                NLWildcard1 = [team, NLWCteam1]
            else:
                continue
        del nl[NLWildcard1[0]]
        #nlWC2
        NLWCteam2 = 0
        for team, wins in nl.items():
            t = wins
            if t > NLWCteam2:
                NLWCteam2 = t
                NLWildcard2 = [team, NLWCteam2]
            else:
                continue
        del nl[NLWildcard2[0]]

        #now put in corect order
        #only have to do division winners because WC teams are always 4 and 5
        ALpost = []
        NLpost = []
        #AL
        if ALE_leader[1] > ALC_leader[1] and ALE_leader[1] > ALW_leader[1]:
            #it doesnt really matter if the 1 and 2 spot are wrong because they play each other and there is no homefeild advantage
            ALpost = [ALE_leader[0], ALC_leader[0], ALW_leader[0], ALWildcard1[0], ALWildcard2[0]]
        
        if ALC_leader[1] > ALE_leader[1] and ALC_leader[1] > ALW_leader[1]:
            ALpost = [ALC_leader[0], ALE_leader[0], ALW_leader[0], ALWildcard1[0], ALWildcard2[0]]

        if ALW_leader[1] > ALE_leader[1] and ALW_leader[1] > ALC_leader[1]:
            ALpost = [ALW_leader[0], ALC_leader[0], ALE_leader[0], ALWildcard1[0], ALWildcard2[0]]

        #NL
        if NLE_leader[1] > NLC_leader[1] and NLE_leader[1] > NLW_leader[1]:
            NLpost = [NLE_leader[0], NLC_leader[0], NLW_leader[0], NLWildcard1[0], NLWildcard2[0]]

        if NLC_leader[1] > NLE_leader[1] and NLC_leader[1] > NLW_leader[1]:
            NLpost = [NLC_leader[0], NLE_leader[0], NLW_leader[0], NLWildcard1[0], NLWildcard2[0]]

        if NLW_leader[1] > NLE_leader[1] and NLW_leader[1] > NLC_leader[1]:
            NLpost = [NLW_leader[0], NLC_leader[0], NLE_leader[0], NLWildcard1[0], NLWildcard2[0]]

        #start the post season
        #print(ALpost)
        #print(NLpost)
        #AL first
        #ALWC
        team1 = get_stats(ALpost[3])
        team2 = get_stats(ALpost[4])

        ALWCt1 = Team(team1[0], team1[1], team1[2])
        ALWCt2 = Team(team2[0], team2[1], team2[2])

        wc = sim_game(ALWCt1.ops, ALWCt1.era, ALWCt2.ops, ALWCt2.era)
        if wc == 'ht':
            ALpost.pop(4)
        elif wc == 'vt':
            ALpost.pop(3)
        else:
            print ('nobody won so something is wrong')

        #ALDS
        team1 = get_stats(ALpost[0])
        team4 = get_stats(ALpost[3])
        team2 = get_stats(ALpost[1])
        team3 = get_stats(ALpost[2])

        ALDS1 = Team(team1[0], team1[1], team1[2])
        ALDS1win = 0
        ALDS2 = Team(team2[0], team2[1], team2[2])
        ALDS2win = 0
        ALDS3 = Team(team3[0], team3[1], team3[2])
        ALDS3win = 0
        ALDS4 = Team(team4[0], team4[1], team4[2])
        ALDS4win = 0

        #ALDS1
        for g in range(5):
            alds1 = sim_game(ALDS1.ops, ALDS1.era, ALDS4.ops, ALDS4.era)
            if alds1 == 'ht':
                ALDS1win = ALDS1win + 1
                if ALDS1win == 3:
                    ALpost.pop(3)
                    break
            else:
                ALDS4win = ALDS4win + 1
                if ALDS4win == 3:
                    ALpost.pop(0)
                    break
        
        #ALDS2
        for g in range(5):
            alds2 = sim_game(ALDS2.ops, ALDS2.era, ALDS3.ops, ALDS3.era)
            if alds2 == 'ht':
                ALDS2win = ALDS2win + 1
                if ALDS2win == 3:
                    ALpost.pop(2)
                    break
            else:
                ALDS3win = ALDS3win + 1
                if ALDS3win == 3:
                    ALpost.pop(1)
                    break
        #ALCS
        team1 = get_stats(ALpost[0])
        team2 = get_stats(ALpost[1])

        ALCS1 = Team(team1[0], team1[1], team1[2])
        ALCS1win = 0
        ALCS2 = Team(team2[0], team2[1], team2[2])
        ALCS2win = 0

        for g in range(7):
            alcs = sim_game(ALCS1.ops, ALCS1.era, ALCS2.ops, ALCS2.era)
            if alcs == 'ht':
                ALCS1win = ALCS1win + 1
                if ALCS1win == 4:
                    ALpost.pop(1)
                    break
            else:
                ALCS2win = ALCS2win + 1
                if ALCS2win == 4:
                    ALpost.pop(0)
                    break

        #NL post season
        #NLWC
        team1 = get_stats(NLpost[3])
        team2 = get_stats(NLpost[4])

        NLWCt1 = Team(team1[0], team1[1], team1[2])
        NLWCt2 = Team(team2[0], team2[1], team2[2])

        wc = sim_game(NLWCt1.ops, NLWCt1.era, NLWCt2.ops, NLWCt2.era)
        if wc == 'ht':
            NLpost.pop(4)
        elif wc == 'vt':
            NLpost.pop(3)
        else:
            print ('nobody won so something is wrong')

        #NLDS
        team1 = get_stats(NLpost[0])
        team4 = get_stats(NLpost[3])
        team2 = get_stats(NLpost[1])
        team3 = get_stats(NLpost[2])

        NLDS1 = Team(team1[0], team1[1], team1[2])
        NLDS1win = 0
        NLDS2 = Team(team2[0], team2[1], team2[2])
        NLDS2win = 0
        NLDS3 = Team(team3[0], team3[1], team3[2])
        NLDS3win = 0
        NLDS4 = Team(team4[0], team4[1], team4[2])
        NLDS4win = 0

        #NLDS1
        for g in range(5):
            nlds1 = sim_game(NLDS1.ops, NLDS1.era, NLDS4.ops, NLDS4.era)
            if nlds1 == 'ht':
                NLDS1win = NLDS1win + 1
                if NLDS1win == 3:
                    NLpost.pop(3)
                    break
            else:
                NLDS4win = NLDS4win + 1
                if NLDS4win == 3:
                    NLpost.pop(0)
                    break
        
        #NLDS2
        for g in range(5):
            nlds2 = sim_game(NLDS2.ops, NLDS2.era, NLDS3.ops, NLDS3.era)
            if nlds2 == 'ht':
                NLDS2win = NLDS2win + 1
                if NLDS2win == 3:
                    NLpost.pop(2)
                    break
            else:
                NLDS3win = NLDS3win + 1
                if NLDS3win == 3:
                    NLpost.pop(1)
                    break
        #NLCS
        team1 = get_stats(NLpost[0])
        team2 = get_stats(NLpost[1])

        NLCS1 = Team(team1[0], team1[1], team1[2])
        NLCS1win = 0
        NLCS2 = Team(team2[0], team2[1], team2[2])
        NLCS2win = 0

        for g in range(7):
            nlcs = sim_game(NLCS1.ops, NLCS1.era, NLCS2.ops, NLCS2.era)
            if nlcs == 'ht':
                NLCS1win = NLCS1win + 1
                if NLCS1win == 4:
                    NLpost.pop(1)
                    break
            else:
                NLCS2win = NLCS2win + 1
                if NLCS2win == 4:
                    NLpost.pop(0)
                    break
        print(NLpost)
        print(ALpost)

        #world series

        team1 = get_stats(ALpost[0])
        team2 = get_stats(NLpost[0])

        WS1 = Team(team1[0], team1[1], team1[2])
        WS1win = 0
        WS2 = Team(team2[0], team2[1], team2[2])
        WS2win = 0

        for g in range(7):
            ws = sim_game(  WS1.ops, WS1.era, WS2.ops, WS2.era)
            if ws == 'ht':
                WS1win = WS1win + 1
                if WS1win == 4:
                    print('world series champions:')
                    print(WS1.name)
                    break
            else:
                WS2win = WS2win + 1
                if WS2win == 4:
                    print('world series champions:')
                    print(WS2.name)
                    break





        
        


        

#testing
season()