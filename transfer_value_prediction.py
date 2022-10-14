import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV, cross_validate, cross_val_score
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

pd.set_option('display.float_format', lambda x: '%.5f' % x)

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = pd.read_csv('son_model_df.csv')

drop_cols = ['Name',	'Nat',	'Based',	'Club', 'Yth Apps', 'Preferred Foot',	'Right Foot',	'Left Foot',	'Height',	'Weight', 'Wage', 'Role','GK', 'DRL',	'DC',	'WBRL', 'DM', 'MRL', 'MC',	'AMRL',	'AMC']

att_22 = ['Agg', 'Jum', 'Pun', 'Nat .1', 'Vis', 'L Th', 'Lon', 'OtB', 'Tck', 'Tec', 'Tea', 'Cmp', 'Fre', 'Ref', 'Pos', 'Pen', 'Pas',
          'Fla', 'Ant', 'Cro', 'Mar', 'Ldr', 'Cor', 'Cnt', 'Det', 'Dec', 'Hea', 'Fir', 'Com', 'Acc', 'Pac', 'Aer', 'Str', 'Thr', 'Han',
          'Ecc', 'Dri', 'Bal', 'Kic', 'Sta', 'Agi', 'Wor', 'Bra', 'Cmd', 'Fin', '1v1', 'TRO']

att_21 = [col + '_21' for col in att_22]
att_20 = [col + '_20' for col in att_22]

non_player = ['Pun', 'Ref', 'Com', 'Aer', 'Thr', 'Han', 'Ecc', 'Kic', 'Cmd', '1v1', 'TRO']
non_gk = ['L Th', 'Lon', 'Tck', 'Cro', 'Mar', 'Cor', 'Hea', 'Dri', 'Fin']


def data_preparer(df, position, non_player, non_gk, drop_col=[], label='Transfer Value', is_gk=False):
        if is_gk:
                df_model = df.drop(non_gk + drop_col, axis=1)
        else:
                df_model = df.drop(non_player + drop_col, axis=1)

        df_model = df_model[df_model['Position'].isin(position)]
        train_df = df_model[~df_model[label].isna()]
        test_df = df_model[df_model[label].isna()]

        X_train = train_df.drop([label, 'UID', 'Position'], axis=1)
        y_train = train_df[label]

        X_test = test_df.drop([label, 'UID', 'Position'], axis=1)

        train_id = train_df['UID']
        test_id = test_df['UID']

        return X_train, y_train, X_test, train_id, test_id

X_train, y_train, X_test, train_id, test_id = data_preparer(new_df, ['SC'], non_player, non_gk, label='Transfer Value', is_gk=False)


def model_bestparams(X, y, plot=False, random=17):
    rmse_list = []
    mae_list = []
    best_params = {}

    # Hyperparameter Sets

    xgboost_params = {'learning_rate': [0.1, 0.01, 0.001],
                      'max_depth': [5, 8, 12, 15],
                      'n_estimators': [100, 300, 500],
                      'colsample_bytree': [0.5, 0.7, 1]}

    hyperparameter_sets = {'XGBoost': xgboost_params}

    model_list = {'XGBoost': XGBRegressor(random_state=random, objective='reg:squarederror')}

    # GridSearch Process
    for idx, model in model_list.items():
        print(f'------------------{idx}------------------')
        best_model_grid = GridSearchCV(model, hyperparameter_sets[idx], cv=5, n_jobs=-1, verbose=True).fit(X, y)
        cv_results = cross_validate(model.set_params(**best_model_grid.best_params_), X, y, cv=5,
                                    scoring=['neg_mean_absolute_error', 'neg_mean_squared_error'])
        best_params[idx] = best_model_grid.best_params_
        for score in ['test_neg_mean_absolute_error', 'test_neg_mean_squared_error']:
            if score == 'test_neg_mean_absolute_error':
                value = np.round(np.mean(-cv_results[score]), 4)
                print(f"{score.replace('test_', '')}: {value}")
                mae_list.append(value)
            else:
                value = np.round(np.mean(np.sqrt(-cv_results[score])), 4)
                print(f"{score.replace('test_', '')}: {value}")
                rmse_list.append(value)
        print(f'-----------------------------------------')

    if plot:
        plt.figure(figsize=(14, 10))
        plt.subplot(2, 1, 1)
        sns.barplot(x=mae_list, y=list(model_list.keys()))
        plt.title('Mean Absolute Error')
        plt.subplot(2, 1, 2)
        sns.barplot(x=rmse_list, y=list(model_list.keys()))
        plt.title('Root Mean Squared')
        plt.show(block=True)

    return best_params

best_params = model_bestparams(X_train, y_train)

print(best_params)