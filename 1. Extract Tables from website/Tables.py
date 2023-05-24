import pandas as pd    # to install pandas --> pip install pandas 

champions_tables = pd.read_html('https://en.wikipedia.org/wiki/UEFA_Champions_League')

print('the type of tables is list :', type(champions_tables))

print('the type of element of the list :', type(champions_tables[1]))

# there is 27 tables in https://en.wikipedia.org/wiki/UEFA_Champions_League :
print('size of champions_tables list :', len(champions_tables))
