import random

def sim_game(ht_ops, ht_era, vt_ops, vt_era): #ht is home team vt is visting team
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
        print('home team wins')
    else:
        print('Visting team wins')
   

class Team: #team class each team will be one, 
    def __init__(self, era, ops, wins, loses, league, division):
        self.era = era
        self.ops = ops
        self.wins = wins
        self.loses = loses
        self.league = league
        self.division = division

    def record(self): #returns teams record
        return(wins + " - " + loses)
    

#testing
sim_game(.700, 4.00, .800, 3.00)