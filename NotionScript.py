from notion.client import NotionClient
from datetime import datetime
from matplotlib import pyplot as plt
import matplotlib.dates as mdates

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
client = NotionClient(token_v2="Replace this with token v2")

# Replace this URL with the URL of the page you want to edit
page = client.get_collection_view("Replace this with your Notion page link")

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

#Sort datetime list and match the lists with their respective data
date_list, data = zip(*sorted(zip(date_list, data)))

# Plot a graph using Matplotlib
ax = plt.gca() #get axes

formatter = mdates.DateFormatter("%d %B %Y") #format as a date
ax.xaxis.set_major_formatter(formatter)

locator = mdates.DayLocator() #set locator
ax.xaxis.set_major_locator(locator)

fig = plt.figure(figsize=(15, 5)) # Plot graph
ax = fig.add_subplot(111)
ax.plot(date_list, data)
plt.show()
