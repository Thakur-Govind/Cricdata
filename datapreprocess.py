bats = pd.read_csv('bats.csv')
bowls = pd.read_csv('bowl.csv')
a='MS Dhoni '
print("_____________________AS A BATSMAN_______________")
if a in list(bats['Batsman']):
    df1 = bats[bats['Batsman']==a]
    print("Runs in life: {}".format(df1['Runs'].sum()))
    print("Total 4s: {}".format(df1['4s'].sum()))
    print("Total 6s: {}".format(df1['6s'].sum()))
    print("Average SR: {}".format(df1['SR'].mean()))
    print("Total Balls Faced: {}".format(df1['BF'].sum()))
else:
    print("Runs in life: Nan")
    print("Total 4s: Nan")
    print("Total 6s: Nan")
    print("Average SR: Nan")
    print("Total Balls Faced: Nan")
    
if a in list(bats['Batsman']):
    print("_____________________AS A BOWLER_______________")
    df2 = bowls[bowls['Bowler']==a]
    print("Overs in life: {}".format(df2['Overs'].sum()))
    print("Maidens in life: {}".format(df2['Mdns'].sum()))
    print("Total Wickets: {}".format(df2['Wkts'].sum()))
    print("Average Economy: {}".format(df2['Econ'].mean()))
    print("Average Strike Rate: {}".format(df2['SR'].mean()))
else:
    print("Overs in life:Nan")
    print("Maidens in life: Nan")
    print("Total Wickets: Nan")
    print("Average Economy: Nan")
    print("Average Strike Rate: Nan")