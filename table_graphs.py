def foot_condition(v):
    if v == 1:
        return "Very Weak"
    elif v == 2:
        return "Weak"
    elif v == 3:
        return 'Reasonable'
    elif v == 4:
        return 'Fairly Strong'
    elif v == 5:
        return 'Strong'
    else:
        return 'Very Strong'


def set_color(styler):
    styler.format(foot_condition)
    styler.background_gradient(axis=None, vmin=1, vmax=6, cmap="YlGnBu")
    return styler


def foot_table(df, uid_list):
  data = df[df['UID'].isin(uid_list)]
  data['Left Foot'] = data['Left Foot'].replace(['Very Weak','Weak', 'Reasonable', 'Fairly Strong', 'Strong', 'Very Strong'],[1, 2, 3, 4, 5, 6])
  data['Right Foot'] = data['Right Foot'].replace(['Very Weak','Weak', 'Reasonable', 'Fairly Strong', 'Strong', 'Very Strong'],[1, 2, 3, 4, 5, 6])
  foot = data[['Name', 'Left Foot', 'Right Foot']].set_index('Name').style.pipe(set_color)
  return foot


def highlight_cells(x):
    return 'background-color: ' + x.map(
        {'No': 'green', 'Yes': 'red'}
    ).fillna('gray')


def injury_table(df, uid_list):
  data = df[df['UID'].isin(uid_list)]
  data['Rc Injury'] = data['Rc Injury'].apply(lambda x: 'No' if x == 0 else 'Yes')
  injury_data = data[['Name', 'Rc Injury']].set_index('Name')
  return injury_data.style.apply(highlight_cells)
