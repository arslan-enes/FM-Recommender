import pandas as pd
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', None)


def get_data():
    pos = pd.read_csv('data/fmpos.csv')
    fm = pd.read_csv('data/fmrole (1).csv')
    scores = pd.read_csv('data/scores.csv')
    return pos, fm, scores


def finder(age, wage, value, position, role, nat):
    pos, fm, scores = get_data()
    df = fm[fm['Age'] <= age]
    df = df[df['Wage'] <= wage]
    df = df[df['Transfer Value'] <= value * 1.3]
    df = df[df['Position'] == position]
    if nat != 'All':
        df = df[df['Nat'] == nat]
    after_filter_uids = df.UID
    print(after_filter_uids)
    after_filter_scores = scores[scores['UID'].isin(after_filter_uids)]
    after_filter_position_scores = pos[pos['UID'].isin(after_filter_uids)]
    final_df = pd.DataFrame({'UID': after_filter_uids.values,
                             'Name': after_filter_scores['Name'],
                             'Position Score': after_filter_position_scores[position],
                             'Role Score': after_filter_scores[role],
                             'Final Score': (after_filter_scores[role]*0.7) + (after_filter_position_scores[position]*0.3)})
    final_df = final_df.sort_values(by='Final Score', ascending=False)
    print(final_df.head())
    return final_df


if __name__ == '__main__':
    selected_nat = int(input('Enter maxiumum age limit: '))
    max_wage = int(input('Enter maximum wage you can offer: '))
    max_value = int(input('Enter maximum transfer fee you can offer: '))
    selected_pos = input('Select a position on the pitch (GK, DM, AM...): ')
    selected_role = input('Select a role (Ball Winning Midfielder, Carillero...): ')
    finder(selected_nat, max_wage, max_value, selected_pos, selected_role)

# BRA
# 8500000
# 90000000
# AMRL
# Inverted Winger (Attack)