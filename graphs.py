import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime
import numpy as np

def compareplayer(df, uid_list, pos_list):

    names = []
    fig = go.Figure()
    for uid in uid_list:
        player = df[df.UID == uid]
        fig.add_trace(go.Scatterpolar(
            r=player[pos_list].values[0],
            theta=pos_list,
            fill='toself',
            name=player['Name'].values[0]
        ))
        names.append(player['Name'].values[0])

    fig.update_layout(
        autosize=False,
        width=1000,
        height=650,
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 20]
            )),
        showlegend=True,
        title=f"{names[0]} vs {names[1]} vs {names[2]} vs {names[3]} vs {names[4]}"
    )

    return fig


def compareplayer_line(df, uid_list, pos_list):

    f_1 = df[df["UID"] == uid_list[0]]
    f_2 = df[df["UID"] == uid_list[1]]
    f_3 = df[df["UID"] == uid_list[2]]
    f_4 = df[df["UID"] == uid_list[3]]
    f_5 = df[df["UID"] == uid_list[4]]

    fig = make_subplots(rows=5, cols=1, shared_xaxes=False)
    for i, f in enumerate([f_1, f_2, f_3, f_4, f_5], start=1):
      fig.add_trace(go.Scatter(x=[datetime.datetime(year=2020, month=10, day=30).strftime('%Y'),
                                  datetime.datetime(year=2021, month=10, day=30).strftime('%Y'),
                                  datetime.datetime(year=2022, month=10, day=30).strftime('%Y')],
                               y=[np.mean(f[[col + '_20' for col in pos_list]].values) * 5
, np.mean(f[[col + '_21' for col in pos_list]].values)* 5
, np.mean(f[pos_list].values)*5
],
                          mode='lines',
                          name=f.Name.values[0]),
                          row=i, col=1)
    fig.update_layout(
        autosize=False,
        width=800,
        height=500,
        xaxis = dict(
            tickmode='array',
            tickvals=[2020, 2021, 2022],
        )
    )

    return fig