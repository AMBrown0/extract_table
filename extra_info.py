import requests
from bs4 import BeautifulSoup

url = 'https://www.instituteforapprenticeships.org/apprenticeship-standards/digital-support-technician-v1-1?view=epa'
response = requests.get(url)
import re


soup = BeautifulSoup(response.content, 'html.parser')
#table = soup.find('table', {'class': 'table'})
#data = []


#tables = soup.find('table')
tables=soup.select('table')
table_no=0

table_list=[]

#columns=[]



for table in tables:
    row_list=[]
    rows = table.find_all('tr')
    for row in rows:
        column_list=[]
        # Do something with each row, such as extracting its cells
        cells = row.find_all('td')
        for cell in cells:
            #print(cell.text)
            cleansed_text=cell.text
            cleansed_text=new_string = re.sub('\n', '', cleansed_text)
            column_list.append(cleansed_text)
        row_list.append(column_list)
    table_list.append(row_list)

print("Updated Here")

# for row in table.find_all('tr'):
#     row_data = []
#     for cell in row.find_all('td'):
#         row_data.append(cell.text.strip())
#     data.append(row_data)

