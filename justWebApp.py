import streamlit as st
import pandas as pd


#@st.cache
def get_data():
    df_league=pd.read_csv("england-premier-league-league-2018-to-2019-stats.csv")
    df_teams = pd.read_csv("england-premier-league-teams-2018-to-2019-stats.csv")
    df_players = pd.read_csv("england-premier-league-players-2018-to-2019-stats.csv")
    dfList=[df_league,df_teams,df_players]
    return dfList


header = st.container()
datasetSection = st.container()
features =st.container()

with header:
    st.title("EPL Project")

with datasetSection:
    st.header('Dataset for 2018-2019')
    st.text('I found this data on dataworld website')


    dataset=get_data()
    st.write(dataset)
    #st.subheader('Nations Distribution:')
    #nations_dist= pd.DataFrame(dataset['Nationality'].value_counts())
    #st.bar_chart(nations_dist)
    #st.subheader('Goals Distribution:')
    #gamePlayed_dist=dataset[['Player','Goals']]
    #st.bar_chart(gamePlayed_dist)
    #st.subheader('Assists Distribution:')
    #gamePlayed_dist = pd.DataFrame(dataset['Assists'].sort_values(by='Assists',ascending=False))
    #st.bar_chart(gamePlayed_dist)

with features:
    st.header('Some features')
    st.markdown('* **First** words words')
    st.markdown('* **Second** words words')



