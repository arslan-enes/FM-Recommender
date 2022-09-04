import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Read the data
fm20 = pd.read_csv('data/fm20data.csv', low_memory=False)
fm21 = pd.read_csv('data/fm21data.csv', low_memory=False)
fm22 = pd.read_csv('data/fm22data.csv', low_memory=False)
fm_managers = pd.read_csv('data/fm22managers.csv', low_memory=False)


# Get rid of the empty characters in the column names
for df in [fm20, fm21, fm22, fm_managers]:
    df.columns = df.columns.str.strip()
    for col in df.columns:
        df[col] = df[col].str.strip() if df[col].dtype == 'object' else df[col]

# Drop managers with no club
fm_managers = fm_managers[fm_managers['Club'].str.strip() != '']

# Merge the datasets into one
fm_final = fm22.merge(fm21,
                      on='UID',
                      how='inner',
                      suffixes=('', '_21')).merge(fm20,
                                                  on='UID',
                                                  how='inner',
                                                  suffixes=('', '_20'))

# Drop the columns that are duplicated
fm_final.drop_duplicates(subset=['UID'], keep='first' ,inplace=True)

# print(fm_final[fm_final.Club == 'Fenerbahçe'])
# Create .csv file
fm_final.to_csv('data/fm_final.csv', index=False)
