from notion.client import NotionClient
from datetime import datetime
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import numpy
import pandas as pd

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
client = NotionClient(token_v2="b231e6b8416d2a469483fce7191de467a703d9f1d136"
                      "ab55d51ce65ad8c3de028ae6ad84991875b974f8f6177d7c1bbe77b"
                      "58e11da5766a33b7ba0d2390e08dbd2342cb9ad371dfde8ce9"
                      "35a654c")

# Replace this URL with the URL of the page you want to edit
page = client.get_collection_view("https://www.notion.so/c4934352d1504ddca"
                                  "a8ddb6e7e287af7?v=f550c1b77988440fa8c33148a268386d")

all_rows = list(page.build_query().execute())
all_rows_data = [row.get_all_properties() for row in all_rows]
date_list = []
data = []

# Add the data of the dates and the respective screen time into 2 separate lists.
for item in all_rows_data:
    date_time = item.get('title') + ' 2020'
    screen_time = item.get('screen_time')
    datetime_object = datetime.strptime(date_time, '%d %B %Y')
    #print(datetime_object, screen_time)
    date_list.append(datetime_object)
    data.append(screen_time)

#Sort datetime list
sorted_list = sorted(date_list)

# Plot a graph using Matplotlib
ax = plt.gca() #get axes

formatter = mdates.DateFormatter("%d %B %Y") #format as a date
ax.xaxis.set_major_formatter(formatter)

locator = mdates.DayLocator() #set locator
ax.xaxis.set_major_locator(locator)

fig = plt.figure(figsize=(15, 5)) # Plot graph
ax = fig.add_subplot(111)
ax.plot(sorted_list, data)
plt.show()

# Print any data for reference
##print(date_list)
##print(data)


#-----Notes----
##    t = datetime_object.timetuple()
##    for i in t:
##        date_list.append(i)
