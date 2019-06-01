import pandas as pd
country = pd.read_csv('A:\\Lemonade.csv',index_col=0)
country.to_html('A:\\edu.html')
country.to_excel('A:\\edu1.xlsx')
df=pd.DataFrame(country)









