import pandas as pd
import matplotlib.pyplot as plt

def main():

    
    #path_folder =
    file_name = "2021-2022_Football_Player_Stats.csv"
    df_origin = pd.read_csv(file_name, sep = ";", encoding='latin-1')
    df = df_origin
    #U21_PlayAtLeast_1Match(df)
    Unique_nationality(df)

    
   
def U21_PlayAtLeast_1Match(df):
    #U21_PlayAtLeast_1Match
    color_league_alphabet = ['red','orange', 'navy', 'purple', 'blue']
    font_size_lable = 21
    df.set_index('Rk', inplace = True)

    df_U21 = df[ (df['Age'] < 22) & (df['MP'] > 1)]    
    
    plt.figure(figsize=(19,10))
    
    df_U21 = df_U21.sort_values(by=['Comp'], ascending=True)
    df_U21.rename(columns={'Comp': 'League'}, inplace=True)
    plot1 = df_U21.groupby(['League']).size().plot.bar(color = color_league_alphabet)

    #annotate bars
    plot1.bar_label(plot1.containers[0], fontsize = font_size_lable)
    plt.xticks(rotation=30, horizontalalignment="center", fontsize = font_size_lable - 10)
    plt.title("U21 Players Play At Least 1 Match", fontsize = font_size_lable - 4, fontweight = 900)
    plt.savefig('U21_PlayAtLeast_1Match.png')

def Unique_nationality(df):
    #Unique Nat
    leagues_5 = ['Bundesliga', "La Liga", "Ligue 1", "Premier League", "Serie A"]
    plt.figure(figsize=(19,10))
    temp = df[df['Nation'].str.startswith('A', na=False)]

    #print(df.head(10))
    #temp = df[ (df['Nation'] == "NA")]      
    #print(temp)
    #print(df['Nation'])
    #print(temp.head(200))
    #plot2 = df.groupby(df['Nation'].str.match('^[a]')).size().plot.barh()
    #plt.tight_layout()
    #plt.legend()
    #plt.savefig('Nationality_distribution.png')
    #plt.show()
 


if __name__=="__main__":
    main()
    
