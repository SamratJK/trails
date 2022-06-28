# from root.n_gram import remove_punctuation
# from  root.parser_table import ratio_and_distance

# print(remove_punctuation("Alaskas's"))
# print(ratio_and_distance("Alaska","Alaskas's"))

import pandas as pd
d = {'col1': [1, 2], 'col2': [3, 4]}
a = pd.DataFrame(data=d)
e = {'col1': [7, 28], 'col2': [13, 14],'col3': [5,6]}
b = pd.DataFrame(data=e)
print(pd.index(a))
# print(pd.concat([pd.merge(a, b, how="right"),pd.merge(a,b, how="left")],axis=0))  