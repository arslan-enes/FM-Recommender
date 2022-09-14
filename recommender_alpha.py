import pandas as pd
pos = pd.read_csv('data/pozisyon_puan.csv')
fm = pd.read_csv('data/fm_13092022.csv')
scores = pd.read_csv('data/scores_13092022.csv')

def finder(nat, wage, value, position, role):
    df = fm[fm['Nat'] == nat]
    # print("df.head(1) after nat choice", df.head(1))
    df = df[df['Wage'] <= wage]
    # print("df.head(1) after wage choice", df.head(1))
    df = df[df['Transfer Value'] <= value]
    # print("df.head(1) after value choice", df.head(1))
    pos_mask = df.apply(lambda x: True if position in x['Position'] else False, axis=1)
    df = df[pos_mask]
    # print("df.head(1) after pos choice", df.head(1))
    after_filter_uids = df.UID
    after_filter_scores = scores[scores['UID'].isin(after_filter_uids)]
    after_filter_position_scores = pos[pos['UID'].isin(after_filter_uids)]
    # print("after_filter_position_scores.head(1)", after_filter_position_scores.head(1))
    # print("after_filter_scores.head(1)", after_filter_scores.head(1))
    final_df = pd.DataFrame({'UID': after_filter_uids,
                             'Name': after_filter_scores['Name'],
                             'Position Score': after_filter_position_scores[position],
                             'Role Score': after_filter_scores[role],
                             'Final Score': after_filter_scores[role] + after_filter_position_scores[position]})
    final_df = final_df.sort_values(by='Final Score', ascending=False)
    print(final_df.head(5))


if __name__ == '__main__':
    selected_nat = input('Select nationality (TUR, ENG, BRA...): ')
    max_wage = int(input('Enter maximum wage you can offer: '))
    max_value = int(input('Enter maximum transfer fee you can offer: '))
    selected_pos = input('Select a position on the pitch (GK, DM, AM...): ')
    selected_role = input('Select a role (Ball Winning Midfielder, Carillero...): ')
    finder(selected_nat, max_wage, max_value, selected_pos, selected_role)


# TUR
# 2000000
# 10000000
# GK
# Sweeper Keeper (Attack)