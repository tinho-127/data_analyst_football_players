import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():

    
    #path_folder =
    file_name = "2022-2023_Football_Player_Stats.csv"
    df_origin = pd.read_csv(file_name, sep = ";", encoding='latin-1')
    df = df_origin
    #U21_PlayAtLeast_1Match(df)
    #Unique_nationality(df)
    #top_5_scorer_each_league(df)
    
   
def U21_PlayAtLeast_1Match(df):
    #U21_PlayAtLeast_1Match
    color_league_alphabet = ['red','orange', 'navy', 'purple', 'blue']
    font_size_lable = 21
    df.set_index('Rk', inplace = True)

    df_U21 = df[ (df['Age'] < 22) & (df['MP'] > 3)]    
    
    plt.figure(figsize=(19,10))
    
    df_U21 = df_U21.sort_values(by=['Comp'], ascending=True)
    df_U21.rename(columns={'Comp': 'League'}, inplace=True)
    plot1 = df_U21.groupby(['League']).size().plot.bar(color = color_league_alphabet)

    #annotate bars
    plot1.bar_label(plot1.containers[0], fontsize = font_size_lable)
    plt.xticks(rotation=30, horizontalalignment="center", fontsize = font_size_lable - 10)
    plt.title("U21 Players Play At Least 3 Match", fontsize = font_size_lable - 4, fontweight = 900)
    plt.savefig('U21_PlayAtLeast_3Match.png')

def Unique_nationality(df):
    #Unique Nat
    leagues_5 = ['Bundesliga', "La Liga", "Ligue 1", "Premier League", "Serie A"]
    font_size_lable = 21
                    
    plt.figure(figsize=(19,10))
    temp = df[df['Nation'].str.startswith(('A','B','C','D','E'), na=False)]
    plot2 = temp.groupby(['Nation']).size().plot.barh(xlim=[0,400])
    plot2.bar_label(plot2.containers[0])
    plt.title("Nationality_distribution_part1", fontsize = font_size_lable - 4, fontweight = 900)
    plt.savefig('Nationality_distribution_part1.png')

    plt.figure(figsize=(19,10))
    temp = df[df['Nation'].str.startswith(('F','G','H','I','J','K','L','M','N'), na=False)]
    plot2 = temp.groupby(['Nation']).size().plot.barh(xlim=[0,400])
    plot2.bar_label(plot2.containers[0])
    plt.title("Nationality_distribution_part2", fontsize = font_size_lable - 4, fontweight = 900)
    plt.savefig('Nationality_distribution_part2.png')
    
    plt.figure(figsize=(19,10))
    temp = df[df['Nation'].str.startswith(('O','P','Q','R','S','T','U','V','W','X', 'Y', 'Z'), na=False)]
    plot2 = temp.groupby(['Nation']).size().plot.barh(xlim=[0,400])
    plot2.bar_label(plot2.containers[0])
    plt.title("Nationality_distribution_part3", fontsize = font_size_lable - 4, fontweight = 900)
    plt.savefig('Nationality_distribution_part3.png')
    
 
def top_5_scorer_each_league(df):
    font_size_lable = 21
    df_temp = df[['Player', 'Comp','Goals','MP']].copy()
    df_temp.sort_values(by=["Comp"],ascending=True, inplace=True)

    plt.figure(figsize=(19,10))

    custom_palette = {}
    for x in df_temp["Comp"]:
        if x == "Bundesliga":
            custom_palette[x] = 'r'
        elif  x == "La Liga":
            custom_palette[x] = 'orange'
        elif  x == "Ligue 1":
            custom_palette[x] = 'navy'
        elif  x == "Premier League":
            custom_palette[x] = 'purple'
        else:
            custom_palette[x] = 'blue'

    sns.barplot(x = 'Comp',
            y = 'Goals',
            data = df_temp,
            errorbar = None,
            palette=custom_palette,
            estimator=sum)
    plt.title("Total Goal for 22-23 Seasons", fontsize = font_size_lable - 4, fontweight = 900)
    plt.savefig('Total_Goal_for_22-23_Seasons.png')

    df_temp = df[['Player', 'Comp','Goals','MP']].copy()
    temp = df_temp[df_temp['Comp'] == 'Bundesliga'].sort_values(by=['Goals'], ascending = False)
    temp = temp.drop_duplicates(subset=["Goals"], keep='first') 

    df_top_goal_each_league = temp[['Goals']].copy().head(5)
    df_top_goal_each_league.insert(1, "Comp", ["Bundesliga"]*5)
    df_top_goal_each_league.insert(2, "Top",['#1 Most Goal','#2 Most Goal','#3 Most Goal','#4 Most Goal','#5 Most Goal'])


    temp = df_temp[df_temp['Comp'] == 'La Liga'].sort_values(by=['Goals'], ascending = False)
    temp = temp.drop_duplicates(subset=["Goals"], keep='first') 
    temp = temp[['Goals','Comp']].copy().head(5)
    temp.insert(2, "Top",['#1 Most Goal','#2 Most Goal','#3 Most Goal','#4 Most Goal','#5 Most Goal'])
    df_top_goal_each_league = pd.concat([df_top_goal_each_league ,temp], ignore_index = True)

    temp = df_temp[df_temp['Comp'] == 'Ligue 1'].sort_values(by=['Goals'], ascending = False)
    temp = temp.drop_duplicates(subset=["Goals"], keep='first') 
    temp = temp[['Goals','Comp']].copy().head(5)
    temp.insert(2, "Top",['#1 Most Goal','#2 Most Goal','#3 Most Goal','#4 Most Goal','#5 Most Goal'])
    df_top_goal_each_league = pd.concat([df_top_goal_each_league ,temp], ignore_index = True)

    temp = df_temp[df_temp['Comp'] == 'Premier League'].sort_values(by=['Goals'], ascending = False)
    temp = temp.drop_duplicates(subset=["Goals"], keep='first') 
    temp = temp[['Goals','Comp']].copy().head(5)
    temp.insert(2, "Top",['#1 Most Goal','#2 Most Goal','#3 Most Goal','#4 Most Goal','#5 Most Goal'])
    df_top_goal_each_league = pd.concat([df_top_goal_each_league ,temp], ignore_index = True)

    temp = df_temp[df_temp['Comp'] == 'Serie A'].sort_values(by=['Goals'], ascending = False)
    temp = temp.drop_duplicates(subset=["Goals"], keep='first') 
    temp = temp[['Goals','Comp']].copy().head(5)
    temp.insert(2, "Top",['#1 Most Goal','#2 Most Goal','#3 Most Goal','#4 Most Goal','#5 Most Goal'])
    df_top_goal_each_league = pd.concat([df_top_goal_each_league ,temp], ignore_index = True)


    custom_palette = {}
    for x in df_top_goal_each_league["Comp"]:
        if x == "Bundesliga":
            custom_palette[x] = 'r'
        elif  x == "La Liga":
            custom_palette[x] = 'orange'
        elif  x == "Ligue 1":
            custom_palette[x] = 'navy'
        elif  x == "Premier League":
            custom_palette[x] = 'purple'
        else:
            custom_palette[x] = 'blue'

    plt.figure(figsize=(19,10))
    sns.barplot(x = 'Top',
            y = 'Goals',
            hue = 'Comp', 
            data = df_top_goal_each_league,
            errorbar = None,
            palette=custom_palette,
            estimator=sum)
    
    plt.grid(axis='y')
    plt.title("Top 5 Scorer each League 22-23", fontsize = font_size_lable - 4, fontweight = 900)
    plt.savefig('Top_5_Scorer_each_League_22-23.png')


    df_temp = df[['Player', 'Comp','Goals','MP']].copy()
    df_temp.sort_values(by=['Goals'],ascending=False, inplace=True)
    df_temp = df_temp.head(25)
        
    plt.figure(figsize=(19,10))
    custom_palette = {}
    for x in df_temp["Comp"]:
        if x == "Bundesliga":
            custom_palette[x] = 'r'
        elif  x == "La Liga":
            custom_palette[x] = 'orange'
        elif  x == "Ligue 1":
            custom_palette[x] = 'navy'
        elif  x == "Premier League":
            custom_palette[x] = 'purple'
        else:
            custom_palette[x] = 'blue'
    sns.barplot(x = 'Player',
            y = 'Goals',
            hue = 'Comp', 
            data = df_temp,
            errorbar = None,
            palette=custom_palette,
            dodge=False,
            estimator=sum
            )
    plt.xticks(rotation=30, horizontalalignment="center", fontsize = font_size_lable - 15)
    plt.title("Top Scorer League 22-23", fontsize = font_size_lable - 4, fontweight = 900)
    plt.grid(axis='y')
    plt.savefig('Top_Scorer_League_22-23.png')





if __name__=="__main__":
    main()
    
