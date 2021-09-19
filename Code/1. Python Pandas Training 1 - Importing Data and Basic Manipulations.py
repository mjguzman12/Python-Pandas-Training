# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 11:16:37 2021

@author: GuzmanMJ
"""

####################################
####################################
#####PYTHON PANDAS TRAINING ONE#####
####################################
####################################

###########
###INTRO###
###########
## Welcome to the Python Pandas Training! This training provides the basics of using
## Python Pandas for data analysis. Whereas R is a programming language that was built
## with statistical analysis in mind, Python was built as a general use programming
## language. Pandas is a Python module that was designed to bring together all of
## the advantages of a general purpose programming language within a statistical
## framework.

## As Pandas is such a robust module, you technically don't need to know any Python
## in order to use it. Virtually all of your data commands will be run with a
## function from Pandas, so very little Python script is actually necessary
## to manipulate data using Python. That being said, this training is designed
## to be completed after the Python Training. Some knowledge of Python will be
## very useful as you approach these trainings, and particularly in lessons 4 
## 5, we will discuss some implementations of Python outside of Pandas to
## manipulate data.

## Notably, this training is intended to be completed using the Spyder console.
## The Spyder console is a part of the Anaconda Python Distribution which includes
## numerous tools to manipulate data. While you can technically complete this
## training and use Pandas without Spyder, the console will be very useful and
## will be essential to view any datasets.

## Getting oriented, Spyder is very similar to R Studio. This text is written 
## in the main text editor, the "Console" at the bottom right will show commands
## as they are run, and the "Variable Explorer" at the top right will show you
## dataframes, matrices, and other objects that you have loaded into memory.

## With that, let's get started!


#####################
###STARTING PANDAS###
#####################
## Pandas is a module of Python, which implies that it is a set of user written
## functions. This is analogous to a package in R or Stata, and we import it here
## so that we can use it throughout the rest of this training. Notably, it is
## typical to type "as pd" after the import statement. This is because we will
## frequently reference Pandas functions throughout this training, and it is
## more convenient to reference Pandas by a shorter name.

import pandas as pd

## If you had trouble importing the Pandas module, read the help file on how
## to install modules in Pandas in the "" path.


####################
###IMPORTING DATA###
####################
## Importing data in pandas is reasonably straightforward. To import a CSV file,
## we can use the "read_csv" function from pandas. Like R, we need to assign this
## to a name in order to keep it in memory:

bike_locations = pd.read_csv("[FILE PATH]/Python Pandas Training/RawData/Capital_Bike_Share_Locations.csv")

## Notice that above, we used the read_csv function and we referenced it by
## writing "pd" before the function. Once you run the function above, the new
## data frame "bike_locations" will appear in the "Variable Explorer" pane on
## the upper right. To view this data frame, navigate to the "Variable Explorer"
## by selecting the "Variable Explorer" ribbon under the window on the top right,
## and double click the object.

## When you view this dataframe, you will immediately notice that some of the
## columns have a different fill color that the others. Spyder automatically
## shades numeric columns in different colors, and string columns are unshaded.
## You can change your color preferences to any shade or no shade at all if you
## prefer.

## While we're here, let's quickly get oriented with the help file for "read_csv".
## Similar to R Studio, you can search for the function "pd.read_csv" in the help
## pane at the upper right (you may need to change to the "Help" ribbon at the
## bottom of the pane). This will bring up the color-coded help file in the "Help"
## Pane, and the describes the required and possible arguments for "pd.read_csv".
## Alternatively, you can also type "help(pd.read_csv)" in the console, and the
## help information will be displayed directly in the console. 

## One comment is that the Spyder interface for help files is not as intuitive as the
## R Studio equivalent. You need to search for functions using their exact names
## AND include the module extension when you search for it. If you type "read_csv"
## in the search bar, Spyder will redirect you to the general help file for the
## "re" module for regular expressions. This is the closest module match for the
## "read_csv" search. Additionally, if you search for "pd.read_csvs", Spyder will
## again redirect you to the "pd.read_csv" help file, again the closest match for your
## search. This takes some getting used to because you could easily be redirected
## to the help file for a similarly-named function, but Spyder wouldn't warn you
## because this is a "near-match". Additionally, Spyder can take a few seconds to
## look up help files, so you may need to wait an additional few seconds before
## you change your search.

## Based on the help file, we can see the additional arguments for "pd.read_csv".
## Below, we import the same dataset with more specifications this time:
bike_locations = pd.read_csv("[FILE PATH]/Python Pandas Training/RawData/Capital_Bike_Share_Locations.csv", 
                             sep = ",", header = 0)

## Here, we used the "sep" parameter to indicate the delimiter and the "header" parameter
## to indicate which row contains the column names. Note that the header is set to 0,
## and Python counting begins with 0 instead of 1.

## Now that we have csv's down, let's import an excel file. The syntax for this
## is very similar to read_csv. Here, we use "pd.read_excel"

insurance = pd.read_excel("[FILE PATH]/Python Pandas Training/RawData/2-2016_QHP_Landscape_Individual_Market_Medical.xlsx",
                          sheet_name = "Data_AK-MT")

## Once you run this, you will notice that it took quite a bit longer to import
## the Excel file. This is typical of statistical programs. Additionally, if you
## view the new "insurance" dataframe in the viewer, you will notice that it
## takes an extra second to open the viewer. This is typical of Spyder. The
## R Studio data viewer is limited to only show up to 99 variables and 1000
## observations. These limitations streamline the data viewer. Spyder has no
## such limitations, but it is quite a bit slower to open the data viewer.

## In addition to pd.read_csv and pd.read_excel, there are many other types of
## files that Pandas can read including Stata, SAS, and JSON files. To see a complete
## list, type "pd.read_" in any part of the text editor and pandas will show you
## an autocomplete list of options.


###########################
###METHODS VS. FUNCTIONS###
###########################
## Now that you are able to import several types of data, it is important to clarify
## the difference between Pandas functions and Pandas methods. Functions represents
## commands that can be run on their own with or without inputs. The "pd.read_csv" and
## "pd.read_excel" commands that you ran above are examples of functions. Methods
## on the other hand are operators for specific object classes. Without getting
## too technical, methods cannot be run on their own - they must always be applied
## to an existing object and they have no meaning without something that's already
## been created. For example, we can use the "pd.DataFrame.describe()" method to get
## a rough description of the bike_locations dataframe:
bike_locations.describe()

## You could also assign the output of this method to another variable:
bike_locations_sum = bike_locations.describe()

## Other useful methods are "pd.DataFrame.head()" which provides the first 5
## observations:
bike_locations.head()

## and "pd.DataFrame.tail()" which provides the last 5 observations:
bike_locations.tail()

## Note that these are DataFrame methods from Pandas. To see the documentation
## for these commands, search "pd.DataFrame.describe" in the Help Pane. Take care
## to type with correct capitalization for the "pd.DataFrame" help files. Pandas
## methods often have additional parameters available if you want to adjust the type
## of output you see, so check the documentation for more details.

## Pandas inherited this syntactic difference between functions and methods from
## Python. While it is an important techinical distinction, the practical point is
## that some data commands will "wrap" around the data object or arguments 
## (these are functions) and some data commands will follow the data object 
## (these are methods). We will discuss more methods later in the training.


#####################################
###CREATING AND DROPPING VARIABLES###
#####################################
## Creating variables in Pandas is analogous to creating variables in R. You
## can reference a new variable in a dataframe by enclosing the name in brackets
## and then setting it equal to a new value:
bike_locations["test"] = 1

## If you reinspect the "bike_locations" dataframe, you will now see that a new
## variable entitled "test" is at the end. Notably, you can use the exact same
## cyntax to reassign a variable already present in your dataframe. Here, we
## reassign "test" to 2:
bike_locations["test"] = 2

## Deleting variables is just as easy as creating them - you can use the "del"
## command to delete specific variables:
del bike_locations["test"]

# To keep specific variables, you can use the following syntax of naming the variables
## you want withing double brackets. This is "subsetting" your dataframe and assigning
## these columns to a new value - here "bike_locations1":
bike_locations1 = bike_locations[["OBJECTID", "ID"]]

## Now is a good time to introduce the "list" function. This has other uses as well,
## but one key use for it in Pandas is that you can easily list the variable names
## in a dataframe.
list(bike_locations)

## This just returns a string with all of the variable names from the bike_locations
## dataframe. This is particularly important in Pandas because it is the only way
## to see your variable names apart from using the data viewer. 


####################
###FILTERING DATA###
####################
## In addition to creating and dropping variables, you may want to drop observations
## based on certain criteria as well. You can accomplish this by using the
## "pd.DataFrame.loc()" method:
## following command:
bike_locations_filtered = bike_locations.loc[bike_locations["NUMBER_OF_BIKES"] >= 10]

## This command is assigning "bike_locations" to the new dataframe "bike_locations_filtered",
## and the "loc" method is operating on "bike_locations to only select rows in which the
## "NUMBER_OF_BIKES" variable is greater than or equal to 10. The "loc" method is a
## boolean operator that checks whether the condition is True for all observations.


##########################
###CLEARING YOUR MEMORY###
##########################
## One final thing before going to on Lesson 2 is to learn how to clear your memory.
## In Spyder, this is accomplished by clicking the "Eraser" symbol either on top of the
## Code Pane on the bottom right or the other "Eraser" symbol on top of the "Variable
## Explorer" Pane on the top right. When you click one of these "Erasers", Spyder will
## warn you that you are about to delete all of the objects in memory, and then will clear
## the "Variable Explorer." There is no automated way to do this. Notably however,
## unlike R, Spyder will not save your project when you close it. Therefore, you can
## also just close Spyder and automatically clear your library as well. One other
## important note is that the "Eraser" will also remove any modules you have loaded,
## including Pandas. Keep this in mind as you may need to reload Pandas after you
## clear your memory.




