import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import json
import base64
from recommender_alpha import finder, manager_check
from graphs import compareplayer, compareplayer_line, short_list_table
from key_features import role_for_pos
from table_graphs import *
st.set_page_config(layout="wide", initial_sidebar_state="expanded")


def blank_space(col, number_of_spaces):
    for i in range(number_of_spaces):
        col.markdown('')


def inject_javascript():
    components.html("""
        <script>
        document.onreadystatechange = () => {

        if (document.readyState === 'complete') {
        const doc = window.parent.document;
        doc.querySelector('.css-1qrvfrg').addEventListener('click', function() {
            doc.querySelectorAll('.css-9s5bis')[1].click(); // same behavior as doc.querySelector('[role="combobox"]').click()
        });
  }
};
        
        </script>
        """, height=0, width=0)


if 'start_page' not in st.session_state:
    st.session_state['start_page'] = True

if 'shortlist' not in st.session_state:
    st.session_state['shortlist'] = pd.DataFrame(columns=['Name', 'Club', 'Age', 'Foot', 'Injury State',
                                                          'Position', 'Role', 'Value', 'Wage', 'Score'])
if 'results' not in st.session_state:
    st.session_state['results'] = False

@st.cache
def get_data():
    pos = pd.read_csv('data/fmpos.csv')
    fm = pd.read_csv('data/fmrole (1).csv')
    scores = pd.read_csv('data/scores1.csv').merge(pd.read_csv('data/scores2.csv'), how='outer')
    managers = pd.read_csv('data/fm22manager3.csv')
    return pos, fm, scores, managers


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

print(f"session_state['shortlist'] = {st.session_state['shortlist']}")

def add_to_shortlist(df, col):
    st.session_state['results'] = True
    st.session_state['shortlist'] = st.session_state['shortlist'].merge(df, how='outer')
    st.session_state['shortlist'] = st.session_state['shortlist'].drop_duplicates()
    col.success('Added to shortlist')
    return


def main():
    local_css("style.css")


    pos, fm, scores, managers = get_data()
    input_container = st.sidebar.container()
    tab1, tab2, tab3, tab4 = st.tabs(["Recommender", "Analysis", "Shortlist", "About"])
    selected_age = input_container.number_input('Enter maxiumum age limit: ', min_value=15, max_value=45, value=27)
    selected_value = input_container.selectbox('Select maximum transfer fee you can offer: ', ['€0', '€100,000', '€500,000', '€1,000,000', '€5,000,000',
                                                                                               '€10,000,000', '€25,000,000', '€50,000,000', '€100,000,000', 'No Limit'])
    if selected_value != 'No Limit':
        selected_value = int(selected_value.replace(',', '').replace('€', ''))

    selected_wage = input_container.selectbox('Select maximum wage you can offer: ', ['€1,000', '€5,000', '€10,000', '€50,000', '€100,000', '€500,000',
                                                                                      '€1,000,000', '€2,500,000', '€5,000,000', '€10,000,000', '€50,000,000', 'No Limit'])
    if selected_wage != 'No Limit':
        selected_wage = int(selected_wage.replace(',', '').replace('€', ''))

    position_help_string = """
    Select a position on the pitch.
    GK = Goalkeeper,
    DRL = Defense Right Left,
    WBRL = Wing Back Right Left,
    DC = Defense Center,
    DM = Defensive Midfield,
    MC = Midfield Center,
    MRL = Midfield Right Left,
    AMC = Attacking Midfield Center,
    AMRL = Attacking Midfield Right Left,
    SC = Striker Center
    """
    selected_pos = input_container.selectbox('Select a position: ', pos.columns[2:], help=position_help_string)

    role_help_string = """Role and duty options for the selected position. 
    Each role has a different set of attributes that are important for the role.
    It sets the player's role on the pitch and the duties he will be expected to perform."""
    selected_role = input_container.selectbox('Select a role: ', role_for_pos[selected_pos], help=role_help_string)
    selected_nat = input_container.selectbox('Select a Nationality: ', ["All"] + list(fm.Nat.unique()))

    manager_help_string = "By choosing a manager, you can compare the tactical style of the player's current club with" \
                          " the tactics of the selected manager. Cards will go green if the two styles are match."
    selected_manager = input_container.selectbox('Select a Manager: ', ["No Preference"] + list(managers.Name.unique()),
                                                 help=manager_help_string)
    get_result_button = input_container.button('Get Results')

    if get_result_button:
        st.session_state['results'] = True

    if st.session_state['results']:
        st.session_state['start_page'] = False
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
                manager_stars = manager_check(player_all['Club'].values[0], selected_manager, managers)
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
      <td colspan='3'>{"€{:,}".format(int(player_all['Transfer Value'].values[0]))}</td>
    </tr>
    <tr>
      <th>Wage</th>
      <td colspan='3'>{"€{:,} (p/y)".format(int(player_all['Wage'].values[0]))}</td>
    </tr>
    <tr>
      <th>Age</th>
      <td>{player_all['Age'].values[0]}</td>
      <th>Nat</th>
      <td>{player_all['Nat'].values[0]}</td>
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

                short_list_dataframe = pd.DataFrame({'Name': player_all['Name'].values[0],
                                                     'Club': player_all['Club'].values[0],
                                                     'Age': player_all['Age'].values[0],
                                                     'Foot': player_all['Preferred Foot'].values[0],
                                                     'Injury State': player_all['Rc Injury'].values[0],
                                                     'Position': player_all['Position'].values[0],
                                                     'Role': selected_role,
                                                     'Value': "€{:,}".format(int(player_all['Transfer Value'].values[0])),
                                                     'Wage': "€{:,} (p/y)".format(int(player_all['Wage'].values[0])),
                                                     'Score': round(result[1]['Final Score'], 2)}, index=[0])

                cols[num].button('Add to Shortlist',
                                 key=f'add{num}',
                                 on_click=add_to_shortlist,
                                 args=(short_list_dataframe, cols[num]))
                if manager_stars:
                    st.markdown(f"""<style>
                #card{num}
                """
                                """
                                {
                                background-color: #D3FFCA;
                                background-size: cover;
                                }
                                </style>""", unsafe_allow_html=True)
                st.session_state['results'] = False

        col1, col2 = tab2.columns(2)
        if results_df.shape[0] == 5:
            col1.plotly_chart(compareplayer(fm, results_df.UID.values, role_atts_dict[selected_role]['key']), use_container_width=True)
            col2.plotly_chart(compareplayer_line(fm, results_df.UID.values, role_atts_dict[selected_role]['key']), use_container_width=True)
            foot = foot_table(fm, results_df.UID.values)
            tab2.dataframe(foot)
            tab2.dataframe(injury_table(fm, results_df.UID.values))
        else:
            tab2.write('Not enough players to compare')

    tab3.plotly_chart(short_list_table(st.session_state['shortlist']), use_container_width=True)


    if st.session_state['start_page']:
        start_cont = tab1.container()
        start_cont.title('Welcome to the Football Manager Player Recommender ⚽')
        start_cont.subheader('Find, analyse and compare players to help you build your dream team!')
        col0, col2, col1 = start_cont.columns([1,2,1])
        blank_space(col0, 1)
        col0.write('1. Enter your preferences 👈 ')
        col0.write('2. View results 🕵️‍♂')
        col0.write('3. Compare players 📊')
        col0.write('4. Add players to your shortlist 📝')
        col0.write('5. And go on !')
        col1.metric(label='Players',value=fm.shape[0])
        col1.metric(label='Managers',value=managers.shape[0])
        col1.metric(label='Attributes', value=(fm.shape[1]))
        col1.metric(label='Roles',value=(len(pos_json()['GK'])+ len(pos_json()['DEF'])+ len(pos_json()['MID'])+ len(pos_json()['FW'])))
        col2.dataframe(fm.sort_values('Transfer Value',ascending=False).iloc[1:10,][['Name','Club','Transfer Value']])




if __name__ == '__main__':
    main()
    inject_javascript()
