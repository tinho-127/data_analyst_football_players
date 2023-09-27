import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.colors as mcolors

#from adjustText import adjust_text



def main():

    
    #path_folder =
    file_name = "2022-2023_Football_Player_Stats.csv"
    df_origin = pd.read_csv(file_name, sep = ";", encoding='latin-1')
    df = df_origin
    #U21_PlayAtLeast_1Match(df)
    #Unique_nationality(df)
    #top_5_scorer_each_league(df)
    #most_assist_league_22_23(df)
    #man_city_stat(df)
    #top_club_for_young(df)
    #nationality_distribution_U25(df)
    #U25_total_contri(df)
    #U25_top_assist(df)


def U25_top_assist(df):
    fig = plt.figure(figsize=(19,10))
    U25 = df[ (df['Age'] < 25) & ( df['MP'] > 4) & ( df['Min'] > 200)]
    U25['Total Contribution'] = U25['Goals'] + U25['Assists']*U25['90s']    
    U25.sort_values(by = ['GCA'], ascending = [False],inplace = True)
    U25.rename(columns={'Comp': 'League'}, inplace=True)

    custom_palette = {}
    for x in U25['League']:
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
    
    ax = sns.scatterplot(x="Age",
                    y="GCA",
                    data=U25,
                    hue="League",
                    palette=custom_palette,
                    size = "GcaPassLive",
                    sizes=(10, 200))

    fig.set_facecolor("whitesmoke")
    ax.set_facecolor("#f7f0e5")
    ax.yaxis.grid(True, color = 'lightgrey')
    ax.set_xlim(15, 25,1)
    ax.set_xticks(np.arange(16,25))
    ax.set_yticks(np.arange(0,2.1,.2))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_ylabel('Total Contribution',fontsize = 15,weight="bold")
    ax.set_xlabel('Age',fontsize = 15,weight="bold")
    
    annotations = U25.head(7)  
    for index, row in annotations.iterrows():
        x = row["Age"]
        y = row["GCA"]
        label = row["Player"]
        if index == 1308:
            ax.text(x, y, label, fontsize=12, ha="left", va="top", color="black", weight="bold")
        else:
            ax.text(x, y, label, fontsize=12, ha="left", va="bottom", color="black", weight="bold")

    plt.title("Top Young Players with most Pass Lead to Goal 22/23", fontsize = 18, fontweight = 900)
    plt.savefig('Top-Young-Players-for-Assits-Seasons-22-23.png')
    #plt.show()
    


def U25_total_contri(df):
    fig = plt.figure(figsize=(19,10))
    U25 = df[ df['Age'] < 25]
    U25['Total Contribution'] = U25['Goals'] + U25['Assists']*U25['90s']    
    U25.sort_values(by = ['Total Contribution'], ascending = [False],inplace = True)
    U25.rename(columns={'Comp': 'League'}, inplace=True)
    #print(U25[['Player','Age','Total Contribution','Goals','Assists','MP','Min','90s']])

    custom_palette = {}
    for x in U25['League']:
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
    
    ax = sns.scatterplot(x="Age",
                    y="Total Contribution",
                    data=U25,
                    hue="League",
                    palette=custom_palette,
                    size = "Goals",
                    sizes=(10, 200))

    # RGBA color values
    rgba_color = (247 / 255, 186 / 255, 182 / 255, 1)

    # Convert to Matplotlib color format
    mpl_color = mcolors.to_rgba(rgba_color)
    fig.set_facecolor("whitesmoke")
    ax.set_facecolor("#f7f0e5")
    ax.yaxis.grid(True, color = 'lightgrey')
    ax.set_xlim(15, 25,1)
    ax.set_xticks(np.arange(16,25))
    ax.set_yticks(np.arange(0,31,2))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_ylabel('Total Contribution',fontsize = 15,weight="bold")
    ax.set_xlabel('Age',fontsize = 15,weight="bold")
    
    annotations = U25.head(7)  
    for index, row in annotations.iterrows():
        x = row["Age"]
        y = row["Total Contribution"]
        label = row["Player"]
        if index == 1858:
            ax.text(x, y, label, fontsize=12, ha="left", va="top", color="black", weight="bold")
        else:
            ax.text(x, y, label, fontsize=12, ha="left", va="bottom", color="black", weight="bold")

        #adjust_text(ts, x=x, y=y, force_points=0.1, arrowprops=dict(arrowstyle='->', color='red'))

    plt.title("Top Young Players for Total Contribution Seasons 22/23", fontsize = 18, fontweight = 900)
    plt.savefig('Top-Young-Players-for-Total-Contribution-Seasons-22-23.png')
    
def nationality_distribution_U25(df):
    fig, axs = plt.subplots(2, 2,figsize=(19,10))
    custom_palette = {}
    x = 0
    y = 0
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
    pie_color = {}
    pie_color[0] = ['grey','lightcoral','saddlebrown','darksalmon','brown','blue','orange','silver','deepskyblue','tomato']
    pie_color[1] = ['yellow','silver','green','crimson','olivedrab' ,'orange','tomato']
    pie_color[2] = ['blue', 'darkgreen', 'red']
    pie_color[3] = ['blue','orange','powderblue','green','peru','indigo','gold', 'red']
    club = [['Wolfsburg','Valencia'],['Montpellier','Leverkusen']]
    pie_color_index = 0
    
    for x in range(2):
        for y in range (2):
            U25_W = df[ (df['Age'] < 25) & (df['Squad'] == club[x][y]) & (df['MP'] > 9) ]
            U25_W_groupby = U25_W.groupby('Nation')['Nation'].count().reset_index(name="Count")
            U25_W_groupby.sort_values(by='Count', ascending=False, inplace=True) 
            axs[x,y].pie(U25_W_groupby['Count'], labels=U25_W_groupby['Nation'], 
                    autopct=autopct_format(U25_W_groupby['Count']),colors = pie_color[pie_color_index])
            axs[x,y].set_title(club[x][y],fontsize=16)
            pie_color_index += 1

    fig.set_facecolor("#f7f0e5")
    fig.suptitle('Nationality Distribution for each Club', fontsize=20)
    plt.tight_layout()
    plt.savefig('Nationality_Distribution_for_each_Club.png')


def autopct_format(values):
        def my_format(pct):
            total = 1
            total = sum(values)
            val = int(round(pct*total/100.0)) 
            return '{:.1f}%\n({v:d})'.format(pct, v=val)
        return my_format

def top_club_for_young(df):
    #U21_PlayAtLeast_1Match
    color_league_alphabet = ['red','orange', 'navy', 'purple', 'blue']
    font_size_lable = 21
    df.set_index('Rk', inplace = True)

    df_U25 = df[ (df['Age'] < 25) & (df['MP'] > 9)]    
    
    plt.figure(figsize=(19,10))
    
    df_U25 = df_U25.sort_values(by=['Comp'], ascending=True)
    df_U25.rename(columns={'Comp': 'League'}, inplace=True)
    df_U25.sort_values(by='Squad', inplace=True)
    df_U25_groupby = df_U25.groupby(['Squad','League'])['Age'].count().reset_index(name="Count")
    df_U25_groupby.sort_values(by='Count', ascending=False, inplace=True)
    df_U25_groupby = df_U25_groupby.head(30)
    
    custom_palette = {}
    for x in df_U25_groupby['League']:
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
    sns.barplot(x = 'Squad',
            y = 'Count',
            hue = 'League',
            data = df_U25_groupby,
            errorbar = None,
            palette=custom_palette,
            dodge=False,
            estimator=sum)
            
    plt.grid(axis = 'y')
    plt.yticks([1, 2, 3, 4, 5,6,7,8,9,10,11,12])
    plt.xticks(rotation=90, horizontalalignment="center", fontsize = font_size_lable - 11)   
    plt.title("Clubs with most Number Youngs Players", fontsize = font_size_lable - 4, fontweight = 900)
    plt.savefig('U25_PlayAtLeast_10Match.png')
    
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


def most_assist_league_22_23(df):
    df_temp = df[['Player', 'Comp','Assists','MP','Goals','Min','90s']].copy()
    df_temp.insert(4,"Total",df_temp['Assists'] * df_temp['90s'])
    df_temp.sort_values(by=['Total'],ascending=False, inplace=True)
    df_temp = df_temp.head(25)
    font_size_lable = 21
        
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
            y = 'Total',
            hue = 'Comp', 
            data = df_temp,
            errorbar = None,
            palette=custom_palette,
            dodge=False,
            estimator=sum
            )
    plt.xticks(rotation=30, horizontalalignment="center", fontsize = font_size_lable - 15)
    plt.title("Top Assists League 22-23", fontsize = font_size_lable - 4, fontweight = 900)
    plt.grid(axis='y')
    plt.savefig('Top_Assists_League_22-23.png')



def man_city_stat(df):
    plt.figure(figsize=(19,10))
    df_temp = df [ df['Squad'] == 'Manchester City']
    df_temp.sort_values(by="Goals", ascending = False,inplace = True)
    df_temp = df_temp.head(10)
    plt.pie(df_temp['Goals'], labels=df_temp['Player'], autopct='%.0f%%')

    plt.figure(figsize=(19,10))
    df_temp = df [ df['Squad'] == 'Manchester City']
    df_temp.insert(4,"Total",df_temp['Assists'] * df_temp['90s'])
    df_temp.sort_values(by="Total", ascending = False,inplace = True)

    df_temp = df_temp.head(10)
    plt.pie(df_temp['Total'], labels=df_temp['Player'], autopct='%.0f%%')
    plt.show()



if __name__=="__main__":
    main()
    
    """
    custom_palette = {}
    for z in U25_W_groupby['Nation']:
        if z == "GER":
            custom_palette[z] = 'black'
        elif  z == "AUT":
            custom_palette[z] = 'lightcoral'
        elif  z == "BEL":
            custom_palette[z] = 'saddlebrown'
        elif  z == "DEN":
            custom_palette[z] = 'darksalmon'
        elif  z == "EGY":
            custom_palette[z] = 'brown'
        elif  z == "FRA":
            custom_palette[z] = 'blue'
        elif  z == "NED":
            custom_palette[z] = 'orange'
        elif  z == "POL":
            custom_palette[z] = 'silver' 
        elif  z == "SWE":
            custom_palette[z] = 'deepskyblue'
        elif  z == "USA":
            custom_palette[z] = 'tomato' 
        elif  z == "ESP":
            custom_palette[z] = 'yellow'
        elif  z == "BRA":
            custom_palette[z] = 'green' 
        elif  z == "GEO":
            custom_palette[z] = 'crimson' 
        elif  z == "GUI":
            custom_palette[z] = 'olivedrad' 
        elif  z == "ENG":
            custom_palette[z] = 'red'
        elif  z == "CMR":
            custom_palette[z] = 'darkgreen'
        elif  z == "ARG":
            custom_palette[z] = 'powderblue'
        elif  z == "BFA":
            custom_palette[z] = 'palegreen'
        elif  z == "CIV":
            custom_palette[z] = 'peru'
        elif  z == "CZE":
            custom_palette[z] = 'indigo'
        else:
            custom_palette[z] = 'gold'
    """

