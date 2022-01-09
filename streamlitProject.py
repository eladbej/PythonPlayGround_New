import time

import streamlit as st
import pandas as pd
import numpy as np
import random as rd
import streamlit.components.v1 as components
import altair as alt
import matplotlib.pyplot as plt



st.markdown(
    """
    <style>
    .main{
    background-color: #F5F5F5;
    }
    </style>
    """,
    unsafe_allow_html=True
)
#components.iframe(src="https://www.investing.com",width=1000,height=500,scrolling=True)
#components.iframe(src="https://www.investing.com",width=1000,height=500,scrolling=True)
@st.cache
def get_data():
    df_league=pd.read_csv("/Users/eladbej/Desktop/Projects/PythonPlayGround/england-premier-league-league-2018-to-2019-stats.csv")
    df_players = pd.read_csv("/Users/eladbej/Desktop/Projects/PythonPlayGround/england-premier-league-players-2018-to-2019-stats.csv")
    df_teams = pd.read_csv("/Users/eladbej/Desktop/Projects/PythonPlayGround/england-premier-league-teams-2018-to-2019-stats.csv")
    dfList=[df_league,df_teams,df_players]
    return dfList


header = st.container()
datasetSection = st.container()
features =st.container()
st.sidebar.title("SideBar")
st.sidebar.button("ClickMe!")

with header:
    st.title("EPL Project")

with datasetSection:
    st.header('Dataset for 2018-2019')
    flag=False
    if st.checkbox("Click Me!",help='is it helpful?'):
        st.text('Shit 💩')
        flag=True
        #st.balloons()
    else:
        st.text('Great! 😃')
        flag = False

    dataset=get_data()

    with st.form("my_form"):
        username=st.text_input("Username:")
        st.write("Inside the form")
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("slider", slider_val, "checkbox", checkbox_val)

    st.write("Outside the form")

    st.markdown('**League DataSet:**')
    st.write(dataset[0])
    #st.json(dataset[0])

    st.markdown('**Teams DataSet:**')
    st.write(dataset[-2])
    st.table(dataset[-2])
    st.markdown('**Players DataSet:**')
    st.write(dataset[-1])
    delta=1

    st.metric("My Metric",45,str(delta)+"%")
    st.subheader('Players Nationality Distribution')
    nations_dist= pd.DataFrame(dataset[-1]['nationality'].value_counts())
    nations_dist=nations_dist.sort_values(by='nationality', ascending=False)
    nations_dist=nations_dist.head(15)
    st.write(nations_dist)
    st.bar_chart(nations_dist)
    st.subheader('Players Positions Distribution')
    pos_dist = pd.DataFrame(dataset[-1]['position'].value_counts())
    pos_dist = pos_dist.head(15)
    st.write(pos_dist)
    st.bar_chart(pos_dist)
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

    sel_col, disp_col=st.columns(2)
    df_teams=get_data()[1]
    x = df_teams['league_position']
    y = df_teams['goals_conceded']
    m, b = np.polyfit(x, y, 1)

    fig=plt.figure(figsize=(12,8), dpi= 100, facecolor='w', edgecolor='k')
    plt.scatter(df_teams['league_position'], df_teams['goals_conceded'])
    plt.xticks(np.arange(min(df_teams['league_position']) - 2, max(df_teams['league_position']) + 2, 1))
    plt.yticks(np.arange(min(df_teams['goals_conceded']) - 2, max(df_teams['goals_conceded']) + 2, 5))
    plt.plot(x, m * x + b)
    plt.xlabel("מיקום בטבלה")
    plt.ylabel("Goals conceded")
    st.pyplot(fig=fig)

    #num_val=sel_col.slider('just a slider',min_value=10,max_value=1000,value=450)
    teamSelected=sel_col.selectbox('Select team:',options=dataset[1]['common_name'])
    st.text(teamSelected)
    playerList=(dataset[-1][dataset[-1]['Current Club']==teamSelected])
    playerSelected=disp_col.selectbox('Select player:',options=playerList)
    st.write(dataset[-1][dataset[-1]['full_name']==playerSelected])

