import pandas as pd

ball_data = pd.read_csv("/home/namita/Music/IPL_Ball-by-Ball_2008-2020.csv")
matches_data = pd.read_csv("/home/namita/Music/IPL_Matches_2008-2020.csv")
 
def first_and_last_ball(df):
    # to find player who faced first ball 
    first_df = df.sort_values(["inning", "over", "ball"], ascending=True).head(1) 
    # to find player who faced last ball
    last_df = df.sort_values(["inning", "over", "ball"], ascending=True).tail(1)
    return first_df,last_df

def highest_lowest_run(df):
    #To find played how secured highest run
    highest_run=df.groupby('batsman').sum('total_runs').sort_values(["total_runs"], ascending=True).tail(1)
    #To find played how secured lowest run
    lowest_run=df.groupby('batsman').sum('total_runs').sort_values(["total_runs"], ascending=True).head(1)
    return highest_run,lowest_run

def matches_per_season(df):
    #To find total count of matches per date
    matches=df.groupby('date').id.count().sort_values( ascending=True)
    return matches

def run_per_season(df):
    # To find total runs by date
    pass

def toss_winner(df):
    # To find Toss winner
    toss_winner=df["toss_winner"].value_counts(ascending=True)
    return toss_winner


print(first_and_last_ball(ball_data))
print(highest_lowest_run(ball_data))
print(matches_per_season(matches_data))
#print(run_per_season(matches_data))
print(toss_winner(matches_data))



