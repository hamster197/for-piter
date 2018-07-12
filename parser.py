import requests, bs4
s=requests.get('https://www.python.org')
b=bs4.BeautifulSoup(s.text, "html.parser")
nazv_name_list = b.find(class_='medium-widget event-widget last')
nazv_name_list_items = nazv_name_list.find_all('a')
date_items = nazv_name_list.find_all('time')
year_items = nazv_name_list.find_all('span')

i=0
for nazv_name in nazv_name_list_items[1:]:
    i=i+1
    if i==1:
        s1=nazv_name.contents[0]
    if i==2:
        s2=nazv_name.contents[0]
    if i==3:
        s3=nazv_name.contents[0]
    if i==4:
        s4=nazv_name.contents[0]
    if i==5:
        s5=nazv_name.contents[0]
i=0
for year in year_items[1:]:
    i = i + 1
    if i == 1:
        s1 = s1 + '; Starts:' + year.contents[0]
    if i == 2:
        s2 = s2 + '; Starts:' + year.contents[0]
    if i == 3:
        s3 = s3 + '; Starts:' + year.contents[0]
    if i == 4:
        s4 = s4 + '; Starts:' + year.contents[0]
    if i == 5:
        s5 = s5 + '; Starts:' + year.contents[0]
i=0
for date in date_items:
    i = i + 1
    if i == 1:
        s1 = s1 + date.contents[1]
    if i == 2:
        s2 = s2 + date.contents[1]
    if i == 3:
        s3 = s3 + date.contents[1]
    if i == 4:
        s4 = s4 + date.contents[1]
    if i == 5:
        s5 = s5 + date.contents[1]

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)