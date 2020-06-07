# graph-plotter-notion
A python program that plots a graph from a Notion collection using notion-py(an unofficial API).
![Demo Image](https://github.com/kvnandula04/graph-plotter-notion/blob/master/Demo%20Image.png?raw=true)

# Usage
You need to configure the following data if you want to use this program:
1) Notion Page Link. First, open the Notion page for which you would like to use the program for. Then, make the page public so that it can generate a link through which it can be accessed. Then open that page on your broswer. 
2) Token v2. Ensuring you're on the Notion page, you can Inspect -> Application -> Cookies -> Select site -> get the value for Token v2.

Once you've got the values, just replace the temp values in the program with your values and you're all set!

# Python Libraries
You need to make sure that you have the following libraries installed on Python:
1) Matplotlib
2) Notion

# Sidenotes
You must make sure that you're logged in on Notion web for this to work. 

You must allow editing for your Notion page.

There must be 2 columns(case sensitive) for this to work:
1) Title - The date in the format Day + Month (For example, '6 June').
2) Screen Time - The screen time that you'd like to plot, in minutes.

Let me know if you have any issues.
