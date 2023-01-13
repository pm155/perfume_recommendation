import streamlit as sl
import pickle
import pandas as pd
sl.set_page_config(
    page_title="Find your Fragrance app",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# It can be difficult for a fragrance novice person like most of us to find a perfect scent for any occasion or simply based on your mood. Here, you can select your favourite perfume that you heard of or you currently use, there are 5 recommendations for similar fragrances for you! Get your perfect scent!"
    }
)
perfume_dict = pickle.load(open('perfume_recommend.pkl','rb'))
sim = pickle.load(open('similarity.pkl','rb'))
perfume = pd.DataFrame(perfume_dict)
sl.title("Want your favourite fragrance?        -poojamaheria")


def recommend(per):
    index = perfume[perfume['Fragrance'] == per].index[0]
    distances = sorted(list(enumerate(sim[index])),reverse=True,key = lambda x: x[1])[1:6]
    recommended_perfume_names=[]
    recommended_perfume_poster=[]
    for i in distances:
        # result.append(perfume.iloc[i[0]].Name)
        # recommended_movie_poster.append(fetch_poster(movie_id))
        per_id = perfume.iloc[i[0]].id
        recommended_perfume_poster.append(fetch_poster(per_id))
        recommended_perfume_names.append(perfume.iloc[i[0]].Fragrance)
    return recommended_perfume_names,recommended_perfume_poster

def fetch_poster(perid):
    return perfume['Image URL'][perid]

perfume_list = perfume['Fragrance'].values
selected_perfume = sl.selectbox(
    "Type or select a perfume from the dropdown",
    perfume_list
)

# if sl.button('Similar Fragrances'):
#     result1 = recommend(option)
#     #sl.image(perfume[perfume['Image URL'][0], width=200)
#     for i in result1:
#         sl.write(i)
# def recommended_perfume_poster(perid):
#     sl.image(perfume['Image URL'][perid], width=200)


# sl.image(perfume['Image URL'][0], width = 200)
if sl.button('Show Recommendation'):
    recommended_perfume_names, recommended_perfume_poster = recommend(selected_perfume)
    col1, col2, col3, col4, col5 = sl.columns(5)
    with col1:
        sl.text(recommended_perfume_names[0])
        sl.image(recommended_perfume_poster[0])
    with col2:
        sl.text(recommended_perfume_names[1])
        sl.image(recommended_perfume_poster[1])

    with col3:
        sl.text(recommended_perfume_names[2])
        sl.image(recommended_perfume_poster[2])
    with col4:
        sl.text(recommended_perfume_names[3])
        sl.image(recommended_perfume_poster[3])
    with col5:
        sl.text(recommended_perfume_names[4])
        sl.image(recommended_perfume_poster[4])
