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
