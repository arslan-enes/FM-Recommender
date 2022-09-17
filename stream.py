import streamlit as st
import streamlit_modal as modal
import pandas as pd
from recommender_alpha import finder
st.set_page_config(layout="wide")

@st.cache
def get_data():
    pos = pd.read_csv('data/deneme_ca2.csv')
    fm = pd.read_csv('data/fm_new_positions.csv')
    scores = pd.read_csv('data/scores_13092022.csv')
    return pos, fm, scores


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def local_js(file_name):
    with open(file_name) as f:
        st.markdown(f'<script>{f.read()}</script>', unsafe_allow_html=True)


def main():
    local_css("style.css")
    # local_js("jscript.js")
    pos, fm, scores = get_data()
    sidebar = st.sidebar.title('Player Recommender')
    input_container = sidebar.container()
    selected_age = input_container.number_input('Enter maxiumum age limit: ', min_value=15, max_value=45, value=18)
    selected_wage = input_container.slider('Enter maximum wage you can offer: ', min_value=0, max_value=int(fm.Wage.max()), step=100000)
    selected_value = input_container.slider('Enter maximum transfer fee you can offer: ', min_value=0, max_value=int(fm['Transfer Value'].max()), step=100000)
    selected_pos = input_container.selectbox('Select a position on the pitch: ', pos.columns[2:])
    selected_role = input_container.selectbox('Select a role: ', scores.columns[2:])
    get_result_button = input_container.button('Get Results')

    if get_result_button:
        results_df = finder(selected_age, selected_wage, selected_value, selected_pos, selected_role).head(5)
        col1, col2, col3, col4, col5 = st.columns(5)
        cols = [col1, col2, col3, col4, col5]
        for num, result in enumerate(results_df.iterrows()):
            with cols[num]:
                player_uid = result[1]['UID']
                player_name = result[1]['Name']
                st.markdown(f"""
                            <script src="https://code.jquery.com/jquery-3.6.1.min.js" integrity="sha256-o88AwQnZB+VDvE9tvIXrMQaPlFFSUTR+nldQm1LuPXQ=" crossorigin="anonymous"></script>
                            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
                            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.min.js" integrity="sha384-ODmDIVzN+pFdexxHEHFBQH3/9/vQ9uori45z4JjnFsRydbmQbmL5t1tQ0culUzyK" crossorigin="anonymous"></script>
                            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
                            """, unsafe_allow_html=True)
                st.markdown(f"""
                            <div class="card" style="width: 15rem;">
                            <img class="card-img-top" src="https://img.fminside.net/facesfm22/{result[1]['UID']}.png" alt="Card image cap">
                            <div class="card-body">
                            <h5 class="card-title">{player_name}</h5>
                            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                            </div>
                            </div>""", unsafe_allow_html=True)








if __name__ == '__main__':
    main()