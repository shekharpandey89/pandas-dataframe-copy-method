import pandas as pd

data = {'TV_Show_name': ['The Walking Dead', 'Merlin', 'little evil',
                         'Money Heist'],
        'TV_Streaming_name': ['Netflix', 'Fx', 'Disney Plus',
                              'Amazon Prime'],
        'show_Season': [4, 10, 4, 5],
        'Main Actor': ['Rick Grimes', 'Mordred', 'Karl C. Miller',
                       'Sergio Marquina']}
df = pd.DataFrame.from_dict(data)
print('Original DataFrame')
print(df)
print('_________________________________________________________')
dfCopy = df.copy()

print('Copied DataFrame')
print(dfCopy)
print('_________________________________________________________')
print("************Manipulation done in the original df***************")
# Now, we are doing data manipulation in the original dataframe
# we are changing the column ('TV_Show_name') values to A,B,C,D
# now, we will see this will affect to the dfCopy dataframe or not
df['TV_Show_name'] = df['TV_Show_name'].replace(['The Walking Dead',
            'Merlin', 'little evil','Money Heist'],['A','B','C','D'])

#Now printing both dfCopy(deep=false) and df (original) dataframe
print('Original DataFrame')
print(df)
print('Copied DataFrame')
print(dfCopy)
