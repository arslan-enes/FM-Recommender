import streamlit as st
import pandas as pd
from recommender_alpha import finder
import base64
from graphs import compareplayer, compareplayer_line
import json
from key_features import role_for_pos
st.set_page_config(layout="wide", initial_sidebar_state="expanded")


@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True)
    return


#set_png_as_page_bg('498776.jpg')

if 'analyze' not in st.session_state:
    st.session_state['anayze'] = False


@st.cache
def get_data():
    pos = pd.read_csv('data/fmpos.csv')
    fm = pd.read_csv('data/fmrole (1).csv')
    scores = pd.read_csv('data/scores1.csv').merge(pd.read_csv('data/scores2.csv'), how='outer')
    return pos, fm, scores


def pos_json():
    with open('data/positions.json') as f:
        data = json.load(f)
    return data

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
    input_container = st.sidebar.container()
    tab1, tab2, tab3 = st.tabs(["Recommender", "Analysis", "About"])
    selected_age = input_container.number_input('Enter maxiumum age limit: ', min_value=15, max_value=45, value=18)
    selected_value = input_container.selectbox('Select maximum transfer fee you can offer: ', ['€100,000', '€500,000', '€1,000,000', '€5,000,000',
                                                                                               '€10,000,000', '€50,000,000', '€100,000,000'])
    selected_value = int(selected_value.replace(',', '').replace('€', ''))
    selected_wage = input_container.selectbox('Select maximum wage you can offer: ', ['€1,000', '€5,000', '€10,000', '€50,000', '€100,000', '€500,000',
                                                                                      '€1,000,000', '€5,000,000', '€10,000,000', '€50,000,000'])
    selected_wage = int(selected_wage.replace(',', '').replace('€', ''))
    selected_pos = input_container.selectbox('Select a position on the pitch: ', pos.columns[2:])
    selected_role = input_container.selectbox('Select a role: ', role_for_pos[selected_pos])
    selected_nat = input_container.selectbox('Select a Nationality: ', ["All"] + list(fm.Nat.unique()))
    get_result_button = input_container.button('Get Results')

    if get_result_button:
        results_df = finder(selected_age, selected_wage, selected_value, selected_pos, selected_role, selected_nat, fm, pos, scores).head(5)
        col1, col2, col3, col4, col5 = tab1.columns(5)
        cols = [col1, col2, col3, col4, col5]
        pos_atts = pos_json()
        role_atts_dict = {}
        role_atts_dict.update(pos_atts['GK'])
        role_atts_dict.update(pos_atts['DEF'])
        role_atts_dict.update(pos_atts['MID'])
        role_atts_dict.update(pos_atts['FW'])
        for num, result in enumerate(results_df.iterrows()):
            with cols[num]:
                player_uid = result[1]['UID']
                img_path = f"https://img.fminside.net/facesfm22/{player_uid}.png"
                if player_uid == 777777777:
                    img_path = 'https://media-exp1.licdn.com/dms/image/C4D03AQEAn5cOIWFO7Q/profile-displayphoto-shrink_800_800/0/1661549952564?e=1669248000&v=beta&t=9dRgksv0W9_EjtUrPOP87cMWCvRfqtbQB-BuNSEe_aE'
                player_name = result[1]['Name']
                player_all = fm[fm.UID == player_uid]
                print(img_path)
                cols[num].markdown(f"""
                            <script src="https://code.jquery.com/jquery-3.6.1.min.js" integrity="sha256-o88AwQnZB+VDvE9tvIXrMQaPlFFSUTR+nldQm1LuPXQ=" crossorigin="anonymous"></script>
                            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
                            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.min.js" integrity="sha384-ODmDIVzN+pFdexxHEHFBQH3/9/vQ9uori45z4JjnFsRydbmQbmL5t1tQ0culUzyK" crossorigin="anonymous"></script>
                            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
                            """, unsafe_allow_html=True)

                cols[num].markdown(f"""
                            <div class="wsk-cp-product" id="card{num}">
                            <div class="wsk-cp-img">
                            <img src="{img_path}" alt="Product" class="img-responsive" />
                            </div>
                            <div class="wsk-cp-text">
                            <div class="title-product">
                            <h3>{player_name}</h3>
                            </div>
                            <div class="description-prod">
                            <table class="table" id='ttable'>
  <tbody>
    <tr>
      <th >Club</th>
      <td colspan='3'>{player_all['Club'].values[0]}</td>
    </tr>
    <tr>
      <th>Value </th>
      <td colspan='3'>{"${:,}".format(int(player_all['Transfer Value'].values[0]))}</td>
    </tr>
    <tr>
      <th>Wage</th>
      <td colspan='3'>{"${:,} (p/y)".format(int(player_all['Wage'].values[0]))}</td>
    </tr>
    <tr>
      <th>Age</th>
      <td>{player_all['Age'].values[0]}</td>
      <th>Nat</th>
      <td>{player_all['Nat'].values[0]}</td>
    </tr>
    <tr>
      <th>Height (cm)</th>
      <td>{player_all['Height'].values[0].split()[0]}</td>
      <th>Weight (kg)</th>
      <td>{player_all['Weight'].values[0].split()[0]}</td>
    </tr>
    <tr>
      <th>Foot</th>
      <td>{player_all['Preferred Foot'].values[0]}</td>
      <th>Score</th>
      <td>{round(result[1]['Final Score'],2)}</td>
    </tr>
  </tbody>
</table>
                            </div>
                            """, unsafe_allow_html=True)
        col1, col2 = tab2.columns(2)
        col1.plotly_chart(compareplayer(fm, results_df.UID.values, role_atts_dict[selected_role]['key']), use_container_width=True)
        col2.plotly_chart(compareplayer_line(fm, results_df.UID.values, role_atts_dict[selected_role]['key']), use_container_width=True)
@st.cache
def analysis():
    st.title('Analysis')
    st.write('This is the analysis page')




if __name__ == '__main__':
    main()