import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import altair as alt


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
    df_league=pd.read_csv("/Users/eladbej/PycharmProjects/pythonProject1/england-premier-league-league-2018-to-2019-stats.csv")
    df_players = pd.read_csv("/Users/eladbej/PycharmProjects/pythonProject1/england-premier-league-players-2018-to-2019-stats.csv")
    df_teams = pd.read_csv("/Users/eladbej/PycharmProjects/pythonProject1/england-premier-league-teams-2018-to-2019-stats.csv")
    dfList=[df_league,df_teams,df_players]
    return dfList


header = st.container()
datasetSection = st.container()
features =st.container()

with header:
    st.title("EPL Project")

with datasetSection:
    st.header('Dataset for 2018-2019')

    if st.checkbox("Click Me!",help='is it helpful?'):
        st.text('Shit 💩')
    else:
        st.text('Great! 😃')
    dataset=get_data()

    st.markdown('**League DataSet:**')
    st.write(dataset[0])

    st.markdown('**Teams DataSet:**')
    st.write(dataset[-2])
    st.markdown('**Players DataSet:**')
    st.write(dataset[-1])
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

    #num_val=sel_col.slider('just a slider',min_value=10,max_value=1000,value=450)
    teamSelected=sel_col.selectbox('Select team:',options=dataset[1]['common_name'])
    st.text(teamSelected)
    playerList=(dataset[-1][dataset[-1]['Current Club']==teamSelected])
    playerSelected=disp_col.selectbox('Select player:',options=playerList)
    st.write(dataset[-1][dataset[-1]['full_name']==playerSelected])

