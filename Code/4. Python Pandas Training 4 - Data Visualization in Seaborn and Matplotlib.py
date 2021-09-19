# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:02:50 2021

@author: GuzmanMJ
"""

##################################
##################################
#####PYTHON PANDAS TRAINING 4#####
##################################
##################################

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
os.chdir("[FILE PATH]/Python Pandas Training")

###########
###INTRO###
###########
## Welcome to Python Pandas Training 4! At this point, you have all of the data manipulation
## skills down. From importing to cleaning data to efficiently looping through dataframes,
## all of the major skills you'll need are in place. In this lesson, we'll dive into a
## much more interesting topic: data visualization in Python. Like everything in Python,
## there are advantages and disadvantages to using it as opposed to another data tool.
## Stata wins virtually all data visualization concepts in terms of how easy it is to
## create a visual, but crafting work-arounds for options that are not builtin can be
## very challenging. Similarly, ggplot in R offers incredible visualization possibilities,
## but once again it can be finicky and there are some things that ggplot won't allow.

## In Python, we are going to explore Seaborn. Seaborn is on par with ggplot for graphing
## capabilities, and it might be more flexible in somoe situations as well. After we dive
## in to some of the possibilities with Seaborn, we are also going to dig into matplotlib.
## As the name implies, "matplotlib" is a Python module built similarly to MATLAB, and it
## allows for three dimensional graphing in Python. Three dimensional plotting is rarely
## called for in data visualization work, but it is occasionally a handy tool in the
## data scientist's toolbox if only to give youself more intuition about how three variables
## are interacting.


##############
###SEABORNE###
##############
## import the data we will use in the "titanic" dataset. This contains some basic info on
## passengers on the Titanic.
titanic = pd.read_csv("RawData/titanic.csv")

## drop extraneous variables
del titanic["PassengerId"]
del titanic["Name"]
del titanic["Ticket"]

## Now, let's plot the age of Titanic passengers against the fare they paid. To do this, we are
## going to use the "relplot" command, which is short for a "relational plot." You can use this
## command to create scatter plots and line graphs which generally "relate" two variables.

## The syntax for this is actually quite similar to ggplot in R if you are familiar with that tool.
## In a nutshell, you need to first specify the base data, then the x variable, and then the y variable.
## These are the only three pieces of information that you need to start:
sns.relplot(data = titanic, x = "Age", y = "Fare")

## Note that the "kind" parameter is set equal to "scatter" by default, so this command does the
## exact same thing as the one above:
sns.relplot(data = titanic, x = "Age", y = "Fare", kind = "scatter")

## This is a basic example of a graph, but what if you want to change the title or add other
## characteristics to your graph? Similar to ggplot, Seaborn uses a layering functionality
## to make changes to graph objects. In ggplot, you would typically add objects together using
## a "+". In Seaborn however, you would edit attributes by modifying the graph object. Let's look
## at an example of this as we change the title of this plot.

## First, we need to set the plot equal to a graph object. Here, this is just "scatter_plot"
scatter_plot = sns.relplot(data = titanic, x = "Age", y = "Fare", kind = "scatter")

## Now, we edit an attribute of this graph object using the "fig.suptitle" method, applied
## to the "scatter_plot" object.
scatter_plot.fig.suptitle("Titanic Passengers Age by Fare")

## The command above immediately shows the edited version of the graph.

## Now, let's vary the fill colors of the scatter plot points by whether passengers survived or not.
## This is controlled by the "hue" parameter, and you will notice that a legend is automatically generated
## in this plot. Note that we once again adjust the title, and we add a third line to adjust the location
## of the title in this version of the graph:
scatter_plot2 = sns.relplot(data = titanic, x = "Age", y = "Fare", kind = "scatter", hue = "Survived")
scatter_plot2.fig.suptitle("Titanic Passengers Age by Fare")
scatter_plot2.fig.subplots_adjust(top = 0.9)

## Finally, Now, let's change the title of the legend here. The first three lines follow the exact same
## pattern as the previous example to change the graph title.
scatter_plot3 = sns.relplot(data = titanic, x = "Age", y = "Fare", kind = "scatter", hue = "Survived")
scatter_plot3.fig.suptitle("Titanic Passengers Age by Fare")
scatter_plot3.fig.subplots_adjust(top = 0.9)

## These next two lines set the "legend" variable to the value of the legend within scatter_plot3. Then,
## we adjust the attributes of the "legend" variable" using the set_text method.
legend = scatter_plot3._legend
legend.texts[0].set_text("Passenger Survived")

## Now that we've made a scatterplot, let's make a histogram to count the number of passengers in each
## age group that survived. To do this, we'll first create the category, and then we'll aggregate by category
## taking the sum of the "Survived" column
titanic_aggregated = titanic
titanic_aggregated["Category"] = ""
titanic_aggregated["Category"] = np.where(titanic_aggregated["Age"].between(0, 10), "0-10", titanic_aggregated["Category"])
titanic_aggregated["Category"] = np.where(titanic_aggregated["Age"].between(10, 20), "10-20", titanic_aggregated["Category"])
titanic_aggregated["Category"] = np.where(titanic_aggregated["Age"].between(20, 30), "20-30", titanic_aggregated["Category"])
titanic_aggregated["Category"] = np.where(titanic_aggregated["Age"].between(30, 40), "30-40", titanic_aggregated["Category"])
titanic_aggregated["Category"] = np.where(titanic_aggregated["Age"].between(40, 50), "40-50", titanic_aggregated["Category"])
titanic_aggregated["Category"] = np.where(titanic_aggregated["Age"].between(50, 60), "50-60", titanic_aggregated["Category"])
titanic_aggregated["Category"] = np.where(titanic_aggregated["Age"].between(60, 70), "60-70", titanic_aggregated["Category"])
titanic_aggregated["Category"] = np.where(titanic_aggregated["Age"].between(70, 80), "70-80", titanic_aggregated["Category"])
titanic_aggregated["Category"] = np.where(titanic_aggregated["Age"].between(80, 90), "80-90", titanic_aggregated["Category"])
titanic_aggregated["Category"] = np.where(titanic_aggregated["Age"].between(90, 100), "90-100", titanic_aggregated["Category"])
titanic_aggregated["Category"] = np.where(titanic_aggregated["Category"] == "", "Other", titanic_aggregated["Category"])

## drop observations that are null in the "Age" variable
titanic_aggregated = titanic_aggregated.loc[pd.notnull(titanic_aggregated["Age"])]

## aggregate by Category taking the sum of the "Survived" column.
titanic_aggregated = titanic_aggregated.groupby(by = "Category", as_index = False)["Survived"].sum()

## Now, create the bar plot. This syntax is very similar to the scatter plot that we created above.
## we set out data, x, and y variables, and here, we also set our confidence intervale to None. The
## reason for this is that Seaborn includes confidence intervals in bar plots by default, and in
## this particular case, we don't want to see those intervals (we're plotting the values as they
## are anyway without any additional calculation). Additionally, we will change the title of this
## bar plot in much the same way as we did before. Note that here, we use the "set_title" method
## which was not available for the relplot object above, but is available for the barplot object
## here.
bar_plot = sns.barplot(data = titanic_aggregated, x = "Category", y = "Survived", ci = None)
bar_plot.set_title("Ages of Survivors of the Titanic")

## This example demonstrates that like many things in Python (and some things in R), there are often
## multiple ways to program something syntactically. We couldn't use the "set_title" syntax with the
## relplot command, but we could use it with the barplot command. You will find that there is in fact
## a universe of seaborn syntax that goes with each of these types of commands, and you can use each
## to improve your Python graphing abilities.

## This completes the overview of how to use Seaborn. At the time of writing, the Antitrust Division only has access
## to version 9.0 of Seaborn, although new versions are available. This basic syntax for Seaborn shouldn't
## change much, and you should be able to use this syntax to get started visualizing data in Python. Like
## all things, there is no subsitute for experience when it comes solving problems, and practice with Seaborn
## will inevitably help you to find out what's new and what syntax is available to craft an outstanding graphic.


################
###MATPLOTLIB###
################
## Now, let's dive into making three dimensional graphs in matplotlib. As mentioned above, this is one area in which
## Pandas has a distinct advantage over R. Three-dimensional plotting is complicated and not very clear in
## ggplot, and Python has integrated it pretty naturally. 

## To start, let's just open a three dimensional plotting space. There are two ways to view matplotlib plots. You can
## either view them "inline" in the console or in an interactive viewer. Most often, you will want to see the interactive
## viewer. To confirm this setting, copy the following command into the console so that the interactive viewer will open
## by default when you create a 3-d plot.
#%matplotlib qt5

## Now, let's open the basic plotting space. The commands below set up a figure with no attributes, and the "ax" command
## that follows sets the projection to 3 dimensions. Finally, we use the "plt.show()" command to view the basic graph:
three_d_fig = plt.figure()
ax = plt.axes(projection = "3d")

## When the graph above opens, you will notice the three dimensional format of the graph area. Additionally, you will
## be able to interactively move the surface so that you can view the plot from different angles.

## Now, let's make a three dimensional line graph with scattered points. To do this, we start by setting up our
## 3-dimensional axes as we did above:
ax = plt.axes(projection = "3d")

## Next, we set up the data for a three-dimensional line. As you may have expected, this requires x, y, and z data
## so that our graph can vary on all three dimensions. Here, we will simply create the z-axis data to be 1000 evenly
## spaced numbers between 0 and 15. Then, we will create the x and y axis data by taking the sine and cosine of these
## values:
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)

## Next, we will create the 3D plot with a gray line. In the command below, we use the "plot3D" method to modify the "ax"
## object, and we add the xline, yline, and zline datasets to this method to plot the line.
ax.plot3D(xline, yline, zline, "gray")

# Now that we've set up an intersting spiral or "slinky" line, let's randomly plot some points around the line as well.
## Once again, we start with the z-axis data by generating a random sample of 100 numbers over the uniform distribution
## from 0 to 1. This is then multiplied by 15 to match our line data above. Following this, we create the x and y
## datasets that are the sine and cosine of the z data plus a random term. This random term adds an interesting element
## to the scattered points so that the points aren't exactly on the line.
zdata = 15*np.random.random(100)
xdata = np.sin(zdata) + 0.1*np.random.randn(100)
ydata = np.cos(zdata) + 0.1*np.random.randn(100)

## Now, use the xdata, the ydata, and the zdata to plot the 3-dimensional scatter plot. Note that the "c" parameter
## governs the color of the graph, so setting c equal to the zdata varies the color according to the value of z
## for each point. Additionally, we have chosen the "Blues" color map here:
ax.scatter3D(xdata, ydata, zdata, c = zdata, cmap = "Blues")

## From here, the world of 3-dimensional plotting gets very big very fast. Among the most popular 3-dimensional
## plotting options are geometric surfaces, three-dimensional bar graphs, and three-dimensional heat maps. Each of
## these are possibly in matplotlib, and you can develop some very interesting visuals in this framework.

## Now that we've created these, a word of caution. Three dimensional graphics are never intuitive. Again, THREE
## DIMENSIONAL GRAPHICS ARE NEVER INTUITIVE. While it can be tempting to add an extra dimension to a graphic to
## show one more type of data, this temptation should be a signal to you as the analyst that you need to find a
## different, more creative way to display the information. The reason that three dimensional graphs are not intuitive is
## that it is difficult for people to see the third dimension drawn on paper. For this reason, you might want
## to make three-dimensional graphics to inform your own understanding of three variables' behaviors, but in terms
## of communicating ideas, other means are almost always going to be recommended over these 3-dimensional methods.
