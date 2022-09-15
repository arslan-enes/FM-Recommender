NON_PLAYER_ATTRIBUTES = [' Pun ', ' Ref ', ' Com ', ' Aer ', ' Thr ', ' Han ', ' Ecc ', ' Kic ', ' Cmd ', ' 1v1 ', ' TRO ']
NON_GK_ATRIBUTES = [' L Th ', ' Lon ', ' Tck ', ' Cro ', ' Mar ', ' Cor ', ' Hea ', ' Dri ', ' Fin ']

MID = {'Advanced Playmaker (Support)': [['Fir', 'Pas', 'Tec', 'Cmp', 'Dec', 'OtB', 'Tea', 'Vis'],
                                        ['Dri', 'Ant', 'Fla', 'Agi']],
       'Advanced Playmaker (Attack)': [['Dri', 'Fir', 'Pas', 'Tec', 'Cmp', 'Dec', 'OtB', 'Tea', 'Vis'],
                                       ['Ant', 'Fla', 'Agi', 'Acc']],
       'Anchor (Defend)': [['Mar', 'Tck', 'Ant', 'Cnt', 'Dec', 'Pos'],
                           ['Cmp', 'Tea', 'Str']],
       'Attacking Midfielder (Support)': [['Fir', 'Lon', 'Pas', 'Tec', 'Ant', 'Dec', 'Fla', 'OtB'],
                                          ['Dri', 'Cmp', 'Vis', 'Agi']],
       'Attacking Midfielder (Attack)': [['Dri', 'Fir', 'Lon', 'Pas', 'Tec', 'Ant', 'Dec', 'Fla', 'OtB'],
                                         ['Fin', 'Cmp', 'Vis', 'Agi']],
       'Ball Winning Midfielder (Defend)': [['Tck', 'Agg', 'Ant', 'Tea', 'Wor', 'Sta'],
                                            ['Mar', 'Bra', 'Cnt', 'Pos', 'Agi', 'Pac', 'Str']],
       'Ball Winning Midfielder (Support)': [['Tck', 'Agg', 'Ant', 'Tea', 'Wor', 'Sta'],
                                             ['Mar', 'Pas', 'Bra', 'Cnt', 'Agi', 'Pac', 'Str']],
       'Box to Box Midfielder (Support)': [['Pas', 'Tck', 'OtB', 'Tea', 'Wor', 'Sta'],
                                           ['Dri', 'Fin', 'Fir', 'Lon', 'Tec', 'Agg', 'Ant', 'Cmp', 'Dec', 'Pos', 'Acc', 'Bal', 'Pac', 'Str']],
       'Carillero (Support)': [['Fir', 'Pas', 'Tck', 'Dec', 'Pos', 'Tea', 'Sta'],
                               ['Tec', 'Ant', 'Cmp', 'Cnt', 'OtB', 'Vis', 'Wor']],
       'Central Midfielder (Defend)': [['Tck', 'Cnt', 'Dec', 'Pos', 'Tea'],
                                       ['Fir', 'Mar', 'Pas', 'Tec', 'Agg', 'Ant', 'Cmp', 'Wor', 'Sta']],
       'Central Midfielder (Support)': [['Fir', 'Pas', 'Tck', 'Dec', 'Tea'],
                                        ['Tec', 'Ant', 'Cmp', 'Cnt', 'OtB', 'Vis', 'Wor', 'Sta']],
       'Central Midfielder (Attack)': [['Fir', 'Pas', 'Dec', 'OtB'],
                                       ['Lon', 'Tck', 'Tec', 'Ant', 'Cmp', 'Tea', 'Vis', 'Wor', 'Acc', 'Sta']],
       'Deep Lying Playmaker (Defend)': [['Fir', 'Pas', 'Tec', 'Cmp', 'Dec', 'Tea', 'Vis'],
                                         ['Tck', 'Ant', 'Pos', 'Bal']],
       'Deep Lying Playmaker (Support)': [['Fir', 'Pas', 'Tec', 'Cmp', 'Dec', 'Tea', 'Vis'],
                                          ['Ant', 'OtB', 'Pos', 'Bal']],
       'Defensive Midfielder (Defend)': [['Tck', 'Ant', 'Cnt', 'Pos', 'Tea'],
                                         ['Mar', 'Pas', 'Agg', 'Cmp', 'Dec', 'Wor', 'Sta', 'Str']],
       'Defensive Midfielder (Support)': [['Tck', 'Ant', 'Cnt', 'Pos', 'Tea'],
                                          ['Mar', 'Pas', 'Agg', 'Cmp', 'Dec', 'Wor', 'Sta', 'Str']],
       'Defensive Winger (Defend)' :[['OtB', 'Tec','Tea','Pos','Ant','Sta','Wor'],
                                          ['Agg','Tck','Cro','Mar','Cnt','Dec','Fir','Acc','Dri']],
       'Defensive Winger (Support)':[['OtB', 'Tec','Tea','Cro','Sta','Wor']],
                                          ['Agg','Tck','Cmp','Pos','Pas','Ant','Mar','Cnt','Dec','Fir','Acc','Dri']]
       'Enganche (Support)': [['Fir', 'Pas', 'Tec', 'Cmp', 'Dec', 'Vis'],
                              ['Dri', 'Ant', 'Fla', 'OtB', 'Tea', 'Agi']],
       'Half Back (Defend)': [['Mar', 'Tck', 'Ant', 'Cmp', 'Cnt', 'Dec', 'Pos', 'Tea'],
                              ['Fir', 'Pas', 'Agg', 'Bra', 'Wor', 'Jum', 'Sta', 'Str']],
       'Inside Forward (Support)': [['Dri', 'Fir', 'Pas', 'Tec', 'OtB', 'Acc', 'Agi', 'Bal'],
                                    ['Fin', 'Lon', 'Ant', 'Cmp', 'Fla', 'Vis', 'Pac']],
       'Inside Forward (Attack)': [['Dri', 'Fin', 'Fir', 'Tec', 'OtB', 'Acc', 'Agi', 'Bal'],
                                   ['Lon', 'Pas', 'Ant', 'Cmp', 'Fla', 'Pac']],
       'Inverted Winger (Support)': [['Dri', 'Pas', 'Tec', 'OtB', 'Acc'],
                                     ['Cro', 'Fir', 'Lon', 'Cmp', 'Dec', 'Vis', 'Wor', 'Agi', 'Pac', 'Sta']],
       'Inverted Winger (Attack)': [['Dri', 'Pas', 'Tec', 'OtB', 'Acc', 'Agi'],
                                    ['Cro', 'Fir', 'Lon', 'Ant', 'Cmp', 'Dec', 'Fla', 'Vis', 'Pac']],
       'Mezzala (Support)': [['Pas', 'Tec', 'Dec', 'OtB', 'Wor', 'Acc'],
                             ['Dri', 'Fir', 'Lon', 'Tck', 'Ant', 'Cmp', 'Vis', 'Bal', 'Sta']],
       'Mezzala (Attack)': [['Dri', 'Pas', 'Tec', 'Dec', 'OtB', 'Vis', 'Wor', 'Acc'],
                            ['Fin', 'Fir', 'Lon', 'Ant', 'Cmp', 'Fla', 'Bal', 'Sta']],
       'Raumdeuter (Support)': [['Fin', 'Ant', 'Cmp', 'Cnt', 'Dec', 'OtB', 'Bal'],
                                ['Fir', 'Tec', 'Wor', 'Acc', 'Sta']],
       'Regista (Support)': [['Fir', 'Pas', 'Tec', 'Cmp', 'Dec', 'Fla', 'OtB', 'Tea', 'Vis'],
                             ['Dri', 'Lon', 'Ant', 'Bal']],
       'Roaming Playmaker (Support)': [['Fir', 'Pas', 'Tec', 'Ant', 'Cmp', 'Dec', 'OtB', 'Tea', 'Vis', 'Wor', 'Acc', 'Sta'],
                                       ['Dri', 'Lon', 'Cnt', 'Pos', 'Agi', 'Bal', 'Pac']],
       'Segundo Volante (Support)': [['Mar', 'Pas', 'Tck', 'OtB', 'Pos', 'Wor', 'Pac', 'Sta'],
                                     ['Fin', 'Fir', 'Lon', 'Ant', 'Cmp', 'Cnt', 'Dec', 'Acc', 'Bal', 'Str']],
       'Segundo Volante (Attack)': [['Fin', 'Lon', 'Pas', 'Tck', 'Ant', 'OtB', 'Pos', 'Wor', 'Pac', 'Sta'],
                                    ['Fir', 'Mar', 'Cmp', 'Cnt', 'Dec', 'Acc', 'Bal', 'Str']],
       'Shadow Striker (Attack)': [['Dri', 'Fin', 'Fir', 'Ant', 'Cmp', 'OtB', 'Acc'],
                                    ['Pas', 'Tec', 'Cnt', 'Dec', 'Wor', 'Agi', 'Bal', 'Pac', 'Sta']],
       'Wide Midfielder (Defend)': [['Pas', 'Tck', 'Cnt', 'Dec', 'Pos', 'Tea', 'Wor'],
                                    ['Cro', 'Fir', 'Mar', 'Tec', 'Ant', 'Cmp', 'Sta']],
       'Wide Midfielder (Support)': [['Pas', 'Tck', 'Dec', 'Tea', 'Wor', 'Sta'],
                                     ['Cro', 'Fir', 'Tec', 'Ant', 'Cmp', 'Cnt', 'OtB', 'Pos', 'Vis']],
       'Wide Midfielder (Attack)': [['Cro', 'Fir', 'Pas', 'Dec', 'Tea', 'Wor', 'Sta'],
                                    ['Tck', 'Tec', 'Ant', 'Cmp', 'OtB', 'Vis']],
       'Wide Playmaker (Support)': [['Fir', 'Pas', 'Tec', 'Cmp', 'Dec', 'Tea', 'Vis'],
                                    ['Dri', 'OtB', 'Agi']],
       'Wide Playmaker (Attack)': [['Dri', 'Fir', 'Pas', 'Tec', 'Cmp', 'Dec', 'OtB', 'Tea', 'Vis'],
                                   ['Ant', 'Fla', 'Acc', 'Agi']],
       'Wide Target Forward (Support)': [['Hea', 'Bra', 'Tea', 'Jum', 'Str'],
                                         ['Cro', 'Fir', 'Ant', 'OtB', 'Wor', 'Bal', 'Sta']],
       'Wide Target Forward (Attack)': [['Hea', 'Bra', 'OtB', 'Jum', 'Str'],
                                        ['Cro', 'Fin', 'Fir', 'Ant', 'Tea', 'Wor', 'Bal', 'Sta']],
       'Winger (Support)': [['Cro', 'Dri', 'Tec', 'OtB', 'Acc', 'Pac'],
                            ['Fir', 'Pas', 'Wor', 'Agi', 'Sta']],
       'Winger (Attack)': [['Cro', 'Dri', 'Tec', 'OtB', 'Acc', 'Pac'],
                           ['Fir', 'Pas', 'Ant', 'Fla', 'Agi']]
       }


GK={'Sweeper Keeper (Defend)':  [[' Ref ', ' Pos ', ' Ant ', ' Cnt ', ' Kic ', ' Agi ', ' Cmd ', ' 1v1 '],
    [' Vis ', ' Cmp ', ' Pas ', ' Dec ', ' Fir ', ' Com ', ' Acc ', ' Aer ', ' Thr ', ' Han ', ' TRO ']],

    'Sweeper Keeper (Support)': [[' Cmp ', ' Ref ', ' Pos ', ' Ant ', ' Cnt ', ' Kic ', ' Agi ', ' Cmd ', ' 1v1 ', ' TRO '],
    [' Vis ', ' Pas ', ' Dec ', ' Fir ', ' Com ', ' Acc ', ' Aer ', ' Thr ', ' Han ']],

    'Sweeper Keeper (Attack)': [[' Cmp ', ' Ref ', ' Pos ', ' Ant ', ' Cnt ', ' Kic ', ' Agi ', ' Cmd ', ' 1v1 ', ' TRO '],
    [' Vis ', ' Pas ', ' Dec ', ' Fir ', ' Com ', ' Acc ', ' Aer ', ' Thr ', ' Han ', ' Ecc ']],

    'Goalkeeper (Defend)': [[' Ref ', ' Pos ', ' Cnt ', ' Com ', ' Aer ', ' Han ', ' Kic ', ' Agi ', ' Cmd '],
    [' Ant ', ' Dec ', ' Thr ', ' 1v1 ']]
    }

FW={'Complete Forward (Attack)': [[' OtB ', ' Tec ', ' Cmp ', ' Ant ', ' Hea ', ' Fir ', ' Acc ', ' Str ', ' Dri ', ' Agi ', ' Fin '],
    [' Jum ', ' Vis ', ' Lon ', ' Tea ', ' Pas ', ' Dec ', ' Pac ', ' Bal ', ' Sta ', ' Wor ']],

    'Complete Forward (Support)': [[' Vis ', ' Lon ', ' OtB ', ' Tec ', ' Cmp ', ' Pas ', ' Ant ', ' Dec ', ' Hea ', ' Fir ', ' Acc ', ' Str ', ' Dri ', ' Agi '],
    [' Jum ', ' Tea ', ' Pac ', ' Bal ', ' Sta ', ' Wor ', ' Fin ']],

    'Target Forward (Support)': [[' Jum ', ' Tea ', ' Hea ', ' Str ', ' Bal ', ' Bra '],
    [' Agg ', ' OtB ', ' Cmp ', ' Ant ', ' Dec ', ' Fir ', ' Fin ']],

    'Target Forward (Attack)': [[' Jum ', ' OtB ', ' Cmp ', ' Hea ', ' Str ', ' Bal ', ' Bra ', ' Fin '],
    [' Agg ', ' Tea ', ' Ant ', ' Dec ', ' Fir ']],

    'Pressing Forward (Defend)': [[' Agg ', ' Tea ', ' Ant ', ' Dec ', ' Acc ', ' Pac ', ' Sta ', ' Wor ', ' Bra '],
    [' Cmp ', ' Cnt ', ' Fir ', ' Str ', ' Bal ', ' Agi ']],

    'Pressing Forward (Support)': [[' Agg ', ' Tea ', ' Ant ', ' Dec ', ' Acc ', ' Pac ', ' Sta ', ' Wor ', ' Bra '],
    [' OtB ', ' Cmp ', ' Pas ', ' Cnt ', ' Fir ', ' Str ', ' Bal ', ' Agi ']],

    'Pressing Forward (Attack)': [[' Agg ', ' OtB ', ' Tea ', ' Ant ', ' Acc ', ' Pac ', ' Sta ', ' Wor ', ' Bra '],
    [' Cmp ', ' Cnt ', ' Dec ', ' Fir ', ' Str ', ' Bal ', ' Agi ', ' Fin ']],

    'Deep Lying Forward (Support)': [[' OtB ', ' Tec ', ' Tea ', ' Cmp ', ' Pas ', ' Dec ', ' Fir '],
    [' Vis ', ' Fla ', ' Ant ', ' Str ', ' Bal ', ' Fin ']],

    'Deep Lying Forward (Attack)': [[' OtB ', ' Tec ', ' Tea ', ' Cmp ', ' Pas ', ' Dec ', ' Fir '],
    [' Vis ', ' Fla ', ' Ant ', ' Str ', ' Dri ', ' Bal ', ' Fin ']],

    'Poacher (Attack)': [[' OtB ', ' Cmp ', ' Ant ', ' Fin '],
    [' Tec ', ' Dec ', ' Hea ', ' Fir ', ' Acc ']],

    'Advanced Forward (Attack)': [[' OtB ', ' Tec ', ' Cmp ', ' Fir ', ' Acc ', ' Dri ', ' Fin '],
    [' Pas ', ' Ant ', ' Dec ', ' Pac ', ' Bal ', ' Sta ', ' Agi ', ' Wor ']],

    'Trequartista (Attack)': [[' Vis ', ' OtB ', ' Tec ', ' Cmp ', ' Pas ', ' Fla ', ' Dec ', ' Fir ', ' Acc ', ' Dri '],
    [' Ant ', ' Bal ', ' Agi ', ' Fin ']],

    'False Nine (Support)': [[' Vis ', ' OtB ', ' Tec ', ' Cmp ', ' Pas ', ' Dec ', ' Fir ', ' Acc ', ' Dri ', ' Agi '],
    [' Tea ', ' Fla ', ' Ant ', ' Bal ', ' Fin ']]
}

DEF = {"Ball Playing Defender (Defender)": [[" Jum ", " Tck ", " Cmp ", " Pos ", " Pas ", " Mar ", " Hea ", " Str "],
                                           [" Agg ", " Vis ", " Tec ", " Ant ", " Cnt ", " Dec ", " Fir ", " Pac ", " Bra "]],
       "Ball Playing Defender (Stopper)": [[" Agg ", " Jum ", " Tck ", " Cmp ", " Pos ", " Pas ", " Dec ", " Hea ", " Str ", " Bra "],
                                          [" Vis ", " Tec ", " Ant ", " Mar ", " Cnt ", " Fir "]],
       "Ball Playing Defender (Cover)": [[" Tck ", " Cmp ", " Pos ", " Pas ", " Ant ", " Mar ", " Cnt ", " Dec ", " Pac "],
                                        [" Jum ", " Vis ", " Tec ", " Hea ", " Fir ", " Str ", " Bra "]],

       "No-Nonsense Centre-Back (Defend)": [[" Jum ", " Tck ", " Pos ", " Mar ", " Hea ", " Str "],
                                           [" Agg ", " Ant ", " Cnt ", " Pac ", " Bra "]],
       "No-Nonsense Centre-Back (Stopper)": [[" Agg ", " Jum ", " Tck ", " Pos ", " Hea ", " Str ", " Bra "],
                                            [" Ant ", " Mar ", " Cnt "]],
       "No-Nonsense Centre-Back (Cover)": [[" Tck ", " Pos ", " Ant ", " Mar ", " Cnt ", " Pac "],
                                          [" Jum ", " Hea ", " Str ", " Bra "]],

       "Wide Center-Back (Defend)": [[" Jum ", " Tck ", " Pos ", " Cro ", " Mar ", " Hea ", " Str ", " Sta "],
                                    [" Agg ", " Cmp ", " Ant ", " Cnt ", " Dec ", " Pac ", " Dri ", " Wor ", " Bra "]],
       "Wide Center-Back (Support)": [[' Jum ', ' Tck ', ' Pos ', ' Cro ', ' Mar ', ' Hea ', ' Pac ', ' Str ', ' Dri ', ' Sta '],
                                     [' Agg ', ' OtB ', ' Cmp ', ' Ant ', ' Cnt ', ' Dec ', ' Wor ', ' Bra ']],
       "Wide Center-Back (Attack)": [[' Jum ', ' OtB ', ' Tck ', ' Cro ', ' Mar ', ' Hea ', ' Pac ', ' Str ', ' Dri ', ' Sta '],
                                    [' Agg ', ' Cmp ', ' Pos ', ' Ant ', ' Cnt ', ' Dec ', ' Wor ', ' Bra ']],

       "Libero (Support)": [[' Vis ', ' Tck ', ' Tea ', ' Cmp ', ' Pos ', ' Pas ', ' Ant ', ' Mar ', ' Cnt ', ' Dec ', ' Fir ', ' Pac '],
                           [' Jum ', ' Tec ', ' Fla ', ' Hea ', ' Str ', ' Dri ', ' Bal ', ' Sta ', ' Agi ', ' Bra ']],
       "Libero (Attack)": [[' Vis ', ' Tck ', ' Tea ', ' Cmp ', ' Pos ', ' Pas ', ' Fla ', ' Ant ', ' Mar ', ' Cnt ', ' Dec ', ' Fir ', ' Pac ', ' Dri '],
                          [' Jum ', ' Lon ', ' Tec ', ' Hea ', ' Acc ', ' Str ', ' Bal ', ' Sta ', ' Agi ', ' Bra ']],

       "Central Defender (Defend)": [[' Jum ', ' Tck ', ' Pos ', ' Mar ', ' Hea ', ' Str '],
                                    [' Agg ', ' Cmp ', ' Ant ', ' Cnt ', ' Dec ', ' Pac ', ' Bra ']],
       "Central Defender (Stopper)": [[' Agg ', ' Jum ', ' Tck ', ' Pos ', ' Dec ', ' Hea ', ' Str ', ' Bra '],
                                     [' Cmp ', ' Ant ', ' Mar ', ' Cnt ']],
       "Central Defender (Cover)": [[' Tck ', ' Pos ', ' Ant ', ' Mar ', ' Cnt ', ' Dec ', ' Pac '],
                                   [' Jum ', ' Cmp ', ' Hea ', ' Str ', ' Bra ']],

       "Full-Back (Defend)": [[' Tck ', ' Pos ', ' Ant ', ' Mar ', ' Cnt '],
                             [' Tea ', ' Cmp ', ' Pas ', ' Cro ', ' Dec ', ' Pac ', ' Sta ']],
       "Full-Back (Support)": [[' Tck ', ' Tea ', ' Pos ', ' Ant ', ' Mar ', ' Cnt ', ' Wor '],
                              [' Tec ', ' Cmp ', ' Pas ', ' Cro ', ' Dec ', ' Pac ', ' Dri ', ' Sta ']],
       "Full-Back (Attack)": [[' Tck ', ' Tea ', ' Pos ', ' Ant ', ' Cro ', ' Pac ', ' Sta ', ' Wor '],
                             [' OtB ', ' Tec ', ' Cmp ', ' Pas ', ' Mar ', ' Cnt ', ' Dec ', ' Fir ', ' Acc ', ' Dri ',
                              ' Agi ']],
       "Full-Back (Automatic)": [[' Tck ', ' Tea ', ' Pos ', ' Ant ', ' Mar ', ' Cnt ', ' Wor '],
                                [' Tec ', ' Cmp ', ' Pas ', ' Cro ', ' Dec ', ' Pac ', ' Dri ', ' Sta ']],

       "Wing-Back (Defend)": [[' Tck ', ' Tea ', ' Pos ', ' Ant ', ' Mar ', ' Acc ', ' Sta ', ' Wor '],
                             [' OtB ', ' Tec ', ' Pas ', ' Cro ', ' Cnt ', ' Dec ', ' Fir ', ' Pac ', ' Dri ',
                              ' Agi ']],
       "Wing-Back (Support)": [[' OtB ', ' Tck ', ' Tea ', ' Cro ', ' Mar ', ' Acc ', ' Dri ', ' Sta ', ' Wor '],
                              [' Tec ', ' Pos ', ' Pas ', ' Ant ', ' Cnt ', ' Dec ', ' Fir ', ' Pac ', ' Agi ']],
       "Wing-Back (Attack)": [[' OtB ', ' Tck ', ' Tec ', ' Tea ', ' Cro ', ' Acc ', ' Pac ', ' Dri ', ' Sta ', ' Wor '],
                             [' Pos ', ' Pas ', ' Fla ', ' Ant ', ' Mar ', ' Cnt ', ' Dec ', ' Fir ', ' Agi ']],
       "Wing-Back (Automatic)": [[' OtB ', ' Tck ', ' Tea ', ' Cro ', ' Mar ', ' Acc ', ' Dri ', ' Sta ', ' Wor '],
                                [' Tec ', ' Pos ', ' Pas ', ' Ant ', ' Cnt ', ' Dec ', ' Fir ', ' Pac ', ' Agi ']],

       "No-Nonsense Full-Back (Defend)": [[' Tck ', ' Pos ', ' Ant ', ' Mar ', ' Cnt ', ' Str '],
                                         [' Agg ', ' Tea ', ' Hea ', ' Bra ']],

       "Complete Wing-Back (Support)": [[' OtB ', ' Tec ', ' Tea ', ' Pas ', ' Cro ', ' Dec ', ' Fir ', ' Acc ', ' Pac ', ' Dri ', ' Sta ', ' Wor '],
                                       [' Tck ', ' Cmp ', ' Fla ', ' Ant ', ' Bal ', ' Agi ']],
       "Complete Wing-Back (Attack)": [[' OtB ', ' Tec ', ' Tea ', ' Pas ', ' Fla ', ' Cro ', ' Dec ', ' Fir ', ' Acc ', ' Pac ', ' Dri ', ' Sta ',' Wor '],
                                      [' Tck ', ' Cmp ', ' Ant ', ' Bal ', ' Agi ']],

       "Inverted Wing-Back (Defend)": [[' Tck ', ' Tea ', ' Pos ', ' Pas ', ' Ant ', ' Mar ', ' Dec ', ' Wor '],
                                      [' OtB ', ' Tec ', ' Cnt ', ' Fir ', ' Acc ', ' Dri ', ' Sta ', ' Agi ']],
       "Inverted Wing-Back (Support)": [[' OtB ', ' Tck ', ' Tea ', ' Pas ', ' Mar ', ' Dec ', ' Sta ', ' Wor '],
                                       [' Tec ', ' Cmp ', ' Pos ', ' Ant ', ' Cnt ', ' Fir ', ' Acc ', ' Dri ',
                                        ' Agi ']],
       "Inverted Wing-Back (Attack)": [[' OtB ', ' Tck ', ' Tec ', ' Tea ', ' Pas ', ' Mar ', ' Dec ', ' Acc ', ' Dri ', ' Sta ', ' Wor '],
                                      [' Lon ', ' Cmp ', ' Pos ', ' Fla ', ' Ant ', ' Cnt ', ' Fir ', ' Pac ', ' Agi ']],
       "Inverted Wing-Back (Automatic)": [[' OtB ', ' Tck ', ' Tea ', ' Pas ', ' Mar ', ' Dec ', ' Sta ', ' Wor '],
                                         [' Tec ', ' Cmp ', ' Pos ', ' Ant ', ' Cnt ', ' Fir ', ' Acc ', ' Dri ', ' Agi ']]
       }



GK = ['Sweeper Keeper (Defend)', 'Sweeper Keeper (Support)', 'Sweeper Keeper (Attack)',
'Goalkeeper (Defend)']


DRL = ["No-Nonsense Full-Back (Defend)",
"Full-Back (Defend)", "Full-Back (Support)", "Full-Back (Attack)", "Full-Back (Automatic)",
"Wing-Back (Defend)", "Wing-Back (Support)", "Wing-Back (Attack)", "Wing-Back (Automatic)",
"Complete Wing-Back (Support)", "Complete Wing-Back (Attack)",
"Inverted Wing-Back (Defend)", "Inverted Wing-Back (Support)", "Inverted Wing-Back (Attack)", "Inverted Wing-Back (Automatic)"]

WRL = ["Wing-Back (Defend)", "Wing-Back (Support)", "Wing-Back (Attack)", "Wing-Back (Automatic)",
"Inverted Wing-Back (Defend)", "Inverted Wing-Back (Support)", "Inverted Wing-Back (Attack)", "Inverted Wing-Back (Automatic)",
"Complete Wing-Back (Support)", "Complete Wing-Back (Attack)"]


DC = ["No-Nonsense Centre-Back (Defend)", "No-Nonsense Centre-Back (Stopper)", "No-Nonsense Centre-Back (Cover)",
"Ball Playing Defender (Defender)", "Ball Playing Defender (Stopper)", "Ball Playing Defender (Cover)",
"Libero (Support)", "Libero (Attack)",
"Central Defender (Defend)", "Central Defender (Stopper)", "Central Defender (Cover)",
"Wide Center-Back (Defend)", "Wide Center-Back (Support)", "Wide Center-Back (Attack)"]

DMC = ['Anchor (Defend)',
'Ball Winning Midfielder (Defend)', 'Ball Winning Midfielder (Support)',
'Half Back (Defend)',
'Deep Lying Playmaker (Defend)', 'Deep Lying Playmaker (Support)',
'Defensive Midfielder (Defend)', 'Defensive Midfielder (Support)',
'Segundo Volante (Support)', 'Segundo Volante (Attack)',
'Roaming Playmaker (Support)',
'Regista (Support)']


MC = ['Ball Winning Midfielder (Defend)', 'Ball Winning Midfielder (Support)',
'Central Midfielder (Defend)', 'Central Midfielder (Support)', 'Central Midfielder (Attack)',
'Mezzala (Support)', 'Mezzala (Attack)',
'Deep Lying Playmaker (Defend)', 'Deep Lying Playmaker (Support)',
'Box to Box Midfielder (Support)',
'Carillero (Support)',
'Advanced Playmaker (Support)', 'Advanced Playmaker (Attack)',
'Roaming Playmaker (Support)']

AMC = ['Attacking Midfielder (Support)', 'Attacking Midfielder (Attack)',
'Shadow Striker (Attack)',
'Enganche (Support)',
'Trequartista (Attack)',
'Advanced Playmaker (Support)', 'Advanced Playmaker (Attack)',]


MRL = ['Inverted Winger (Support)', 'Inverted Winger (Attack)',
'Wide Playmaker (Support)', 'Wide Playmaker (Attack)',
'Wide Midfielder (Defend)', 'Wide Midfielder (Support)', 'Wide Midfielder (Attack)'
'Defensive Winger (Defend)', 'Defensive Winger (Support)'
'Winger (Support)', 'Winger (Attack)']

AMRL = ['Inverted Winger (Support)', 'Inverted Winger (Attack)',
'Advanced Playmaker (Support)', 'Advanced Playmaker (Attack)',
'Raumdeuter (Support)',
'Inside Forward (Support)', 'Inside Forward (Attack)',
'Winger (Support)', 'Winger (Attack)',
'Wide Target Forward (Support)', 'Wide Target Forward (Attack)',
'Trequartista (Attack)']

FC = ['Complete Forward (Attack)', "Complete Forward (Support)",
'Target Forward (Support)', 'Target Forward (Attack)',
'Pressing Forward (Defend)', 'Pressing Forward (Support)', 'Pressing Forward (Attack)'
'Deep Lying Forward (Support)', 'Deep Lying Forward (Attack)',
'Poacher (Attack)',
'Advanced Forward (Attack)',
'Trequartista (Attack)',
'False Nine (Support)']