# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 09:05:46 2021

@author: GuzmanMJ
"""

######################################
######################################
#####PYTHON PANDAS TRAINING THREE#####
######################################
######################################

###########
###INTRO###
###########
## Welcome to Pandas Training 3! At this point, you have a lot of the basics down. From
## importing, to creating and dropping variables, to sorting, merging, appending,
## and even reshaping, you've got it all. Now let's dive in to some slightly more
## more challenging concepts. This training focuses on conditional variable generation,
## loops, and regular expressions in Pandas.


############
###HEADER###
############
## While we're here, let's take a look at a standard header for your Pandas script:

import os, pandas as pd
os.chdir("[FILE PATH]/Python Pandas Training")

## Let's break down these three lines. The first line imports the modules that you
## are going to use in this script. "os" is a standard Python module that stands
## for "operating system". This is useful for many data reading and writing purposes,
## but we will mainly use it to change the directory, which we'll discuss momentarily.
## You are allowed to import multiple modules in one line separated by commas, so
## we import the pandas library in this line as well. Following this, we change
## the working directory using the "chdir" function within the "os" module.


#####################################
###CONDITIONAL VARIABLE GENERATION###
#####################################
## Now, let's import the bike_locations data so that we can practice conditional variable
## generation within it. Note that we just include "RawData" in the beginning of the
## path because we already set our working directory above:
bike_locations = pd.read_csv("RawData/Capital_Bike_Share_Locations.csv")

## To generate variables conditionally, we typically use the "where" function in the
## numpy module. Short for "numeric python", the "numpy" module provides many useful
## tools for manipulating matrices and higher dimensional dataframes. Depending
## on your exact project, you may or may not need numpy, but it is so standard that
## it is typically included in most pandas scripts. Note that the standard abbreviation
## for the "numpy" module is "np":
import numpy as np

## as we discussed above, we will use the "where" function from numpy to conditionally
## create a variable. The following line sets a new variable entitled "test" to 1 if
## the "NUMBER_OF_BIKES" variable is greater than 10 and 0 if the "NUMBER_OF_BIKES"
## variables is less than or equal to 10:
bike_locations["test"] = np.where(bike_locations["NUMBER_OF_BIKES"] > 10, 1, 0)

## This is pretty typical syntax of an if-else statement. The first argument is the
## condition, the second argument is the value to return if the condition evaluates to
## True, and the third argument is the value to return if the condition evaluates to
## False.

## Note that like other data tools, you cannot have a variable that contains both strings
## and numerics. That being said, Pandas doesn't care very much if you try. The following
## command is exactly the same, but the "test2" variable is now set to the string "one"
## if the "NUMBER_OF_BIKES" variable is greater than 10. If you run this, Pandas will
## coerce the 0 in the third argument to a string without telling you. You can check
## this in the data viewer to confirm that the new variable "test2" does exist and
## is comprised of the "one" and "0".
bike_locations["test2"] = np.where(bike_locations["NUMBER_OF_BIKES"] > 10, "one", 0)


###########
###LOOPS###
###########
## At long last, we have arrived at some tasks in which Pandas has a distinct advantage over
## R. First and foremost among these is loops. Loops are extremely easy in Python and Pandas.
## For example, say you want to convert the "INSTALLED" and "LOCKED" variables in bike_locations
## to lowercase. In the parlance of Pandas, "INSTALLED" and "LOCKED" are actually "series"
## within the bike_locations data frame. Therefore, you could apply the "pd.Series.str.lower()"
## method to these variables to make them lowercase one at at time:
bike_locations["INSTALLED"] = bike_locations["INSTALLED"].str.lower()
bike_locations["LOCKED"] = bike_locations["LOCKED"].str.lower()

## Gosh, now say you messed up and need to convert these variables back to uppercase!
## Rather than retype these two commands, you could convert these to uppercase in the
## following loop:

for column in ["INSTALLED", "LOCKED"]:
    bike_locations[column] = bike_locations[column].str.upper()
    
## If you have any experience in Stata, this might look a little familiar. In setting
## up a loop, we set up a variable by which we call the objects in the loop (here we used
## "column"), and then we can call that variable in the command within the loop.
    
## There are a few things to note here. First, the list of things over which we iterated
## is a list of strings enclosed by brackets. This is immediately followed by a colon
## to indicate the beginning of the loop. Now, one thing that you may have noticed is that
## there is no further colon, closed parentheses, or bracket to end the loop. This is
## inherited from Python - there is no closing symbol. Python respects the INDENTATION
## of the loop. Therefore, the following command to create a new variable is NOT part of
## the loop above:
bike_locations["new variable"] = "This variable creation is not part of the loop above."

## However, in the following loop to conditionally create variables, each line is part of the
## loop, even though they have different spacing between them. Here, we are going to create a
## variable entitled "num_of_bikes_string", and we are going to set it equal to a value depending
## on the value of the "NUMBER_OF_BIKES" variable. Now, since there is actually a range of numbers
## of bikes, we could feasibly do this in a loop where each line accounts for one potential value.

## Start by creating the "num_of_bikes_string" variable that we just described
bike_locations["num_of_bikes_string"] = ""


## run the loop for each value between 0 and 20, exclusive. This is similar to a "forvalues" loop in
## Stata if you're familiar with that syntax. Each line in this loop tests whether the "NUMBER_OF_BIKES"
## variable equals the value of the loop (I chose "i" for this value), and then it sets the
## "num_of_bikes_string" variable equal to a string value depending on which line evaluates to true:
for i in range(0, 20):
    bike_locations["num_of_bikes_string"] = np.where((bike_locations["NUMBER_OF_BIKES"] == i) & (i == 0), "zero", bike_locations["num_of_bikes_string"])
    bike_locations["num_of_bikes_string"] = np.where((bike_locations["NUMBER_OF_BIKES"] == i) & (i == 1), "one", bike_locations["num_of_bikes_string"])
    bike_locations["num_of_bikes_string"] = np.where((bike_locations["NUMBER_OF_BIKES"] == i) & (i == 2), "two", bike_locations["num_of_bikes_string"])
    bike_locations["num_of_bikes_string"] = np.where((bike_locations["NUMBER_OF_BIKES"] == i) & (i == 3), "three", bike_locations["num_of_bikes_string"])
    bike_locations["num_of_bikes_string"] = np.where((bike_locations["NUMBER_OF_BIKES"] == i) & (i == 4), "four", bike_locations["num_of_bikes_string"])
    bike_locations["num_of_bikes_string"] = np.where((bike_locations["NUMBER_OF_BIKES"] == i) & (i == 5), "five", bike_locations["num_of_bikes_string"])
    bike_locations["num_of_bikes_string"] = np.where((bike_locations["NUMBER_OF_BIKES"] == i) & (i == 6), "six", bike_locations["num_of_bikes_string"])
    bike_locations["num_of_bikes_string"] = np.where((bike_locations["NUMBER_OF_BIKES"] == i) & (i == 7), "seven", bike_locations["num_of_bikes_string"])
    bike_locations["num_of_bikes_string"] = np.where((bike_locations["NUMBER_OF_BIKES"] == i) & (i == 8), "eight", bike_locations["num_of_bikes_string"])
    bike_locations["num_of_bikes_string"] = np.where((bike_locations["NUMBER_OF_BIKES"] == i) & (i == 9), "nine", bike_locations["num_of_bikes_string"])
    bike_locations["num_of_bikes_string"] = np.where((bike_locations["NUMBER_OF_BIKES"] == i) & (i == 10), "ten", bike_locations["num_of_bikes_string"])
    
    bike_locations["num_of_bikes_string"] = np.where((bike_locations["NUMBER_OF_BIKES"] == i) & (i == 11), "eleven", bike_locations["num_of_bikes_string"])
    bike_locations["num_of_bikes_string"] = np.where((bike_locations["NUMBER_OF_BIKES"] == i) & (i == 12), "twelve", bike_locations["num_of_bikes_string"])
    bike_locations["num_of_bikes_string"] = np.where((bike_locations["NUMBER_OF_BIKES"] == i) & (i == 13), "thirteen", bike_locations["num_of_bikes_string"])
    bike_locations["num_of_bikes_string"] = np.where((bike_locations["NUMBER_OF_BIKES"] == i) & (i == 14), "fourteen", bike_locations["num_of_bikes_string"])
    bike_locations["num_of_bikes_string"] = np.where((bike_locations["NUMBER_OF_BIKES"] == i) & (i == 15), "fifteen", bike_locations["num_of_bikes_string"])
    
    
    bike_locations["num_of_bikes_string"] = np.where((bike_locations["NUMBER_OF_BIKES"] == i) & (i == 16), "sixteen", bike_locations["num_of_bikes_string"])
    bike_locations["num_of_bikes_string"] = np.where((bike_locations["NUMBER_OF_BIKES"] == i) & (i == 17), "seventeen", bike_locations["num_of_bikes_string"])
    bike_locations["num_of_bikes_string"] = np.where((bike_locations["NUMBER_OF_BIKES"] == i) & (i == 18), "eighteen", bike_locations["num_of_bikes_string"])
    bike_locations["num_of_bikes_string"] = np.where((bike_locations["NUMBER_OF_BIKES"] == i) & (i == 19), "nineteen", bike_locations["num_of_bikes_string"])
    
    
    
    
    
    bike_locations["num_of_bikes_string"] = np.where((bike_locations["NUMBER_OF_BIKES"] == i) & (i == 20), "twenty", bike_locations["num_of_bikes_string"])


## To further emphasize the point above, take note of the strange extra spacing in this loop. This is to
## illustrate that Python respects indentation in loops. Everything following the "for" command that
## follows the indentation of the loop will be treated as part of the loop, regardless of how much space
## is put between commands. Spyder will also automatically indent new lines until you write a new
## command that is outside of the loop's indentation.

## Two other useful loop tricks in Pandas is how to loop over all variable in a dataframe, and how to
## loop over multiple dataframes. The former can be accomplished by looping over the dataframe itself:
for column in bike_locations:
    print(bike_locations[column])

## The loop above interprets "bike_locations" in the "for" command as the list of all variables in the
## "bike_locations" dataframe. This will therefore print a list of each of the variables in the console.
## This would be particularly useful if your dataframe is composed entirely of strings or entirely of numerics.

## To loop over multiple dataframes, we can do the following. First, we need to import a second dataframe:
insurance = pd.read_excel("[FILE PATH]/Python Pandas Training/RawData/2-2016_QHP_Landscape_Individual_Market_Medical.xlsx",
                          sheet_name = "Data_AK-MT")

## Now, create a "sourcefile" variable in both dataframes. We will convert this sourcefile variable to uppercase
## in the next step.
insurance["sourcefile"] = "Insurance Data"
bike_locations["sourcefile"] = "DC Bike Locations"

## Now, run a loop over the two dataframes. If you had many dataframes, you could put these into a list first
## and then run the loop over all of the list.
for df in insurance, bike_locations:
     df["sourcefile"] = df["sourcefile"].str.upper()    

## This converts the "sourcefile" variable in both dataframes to uppercase, and you can confirm this by
## opening each of these dataframes separately.

## Above, we noted that Python has a distinct advantage over R in terms of loops. This is because Python
## interprets the loop macro variables in a much more intuitive manner to R. You can loop over virtually
## anything in Python, from variables, to dataframes, to values. Loops in Python are powerful, flexible,
## and with a little practice, very intuitive, and you should take full advantage of this when possible.


#########################
###REGULAR EXPRESSIONS###
#########################
## If you have any experience with other data tools, than you may already realize that
## regular expressions represent some of the most powerful tools in the data scientist's
## arsenal. A well designed regular expression can allow you to identify and edit observations
## with surgical precision, and regular expressions are much faster than the myriad of
## true/false statements that you would need to type out otherwise. This training won't
## go into extreme depth on regular expressions as an entire training can (and should)
## be devoted solely to them. Here, we will just go into basic usage of regular expressions
## in Python. This is similar to what you may have seen in the Python Trainings if you
## already completed those, but here, we emphasize regular expressions in data more than
## we did before.
     
## To keep observations that match a regular expression, we can index a dataframe using
## the "str.contains()" method. In the command below, we keep observations that contain
## "NW" in the "ADDRESS" field:
bike_locations_nw = bike_locations[bike_locations["ADDRESS"].str.contains("NW")]

## Note that if you were to just set a new variable equal to the value of the index as we
## do below, then you would just get a list of TRUE/FALSE to indicate if the value of each
## observations matches the regular expression:
nw_regex = bike_locations["ADDRESS"].str.contains("NW")

## Like other programming languages, Pandas uses the asterisk to indicate the repetition of
## any number of characters. Notably however, in Pandas, the asterisk will only match
## the expression immediately to its left. Therefore, if you want to match any number of
## any character, you would need to use the following regular expression with a period
## followed by an asterisk. This returns the entire original bike_locations dataframe.
bike_locations = bike_locations[bike_locations["ADDRESS"].str.contains(".*")]

## Another useful regular expression tool is the "replace" method. We can use this to replace
## text in a dataframe column with other text. In the example below, we replace all "NW"
## strings in the "ADDRESS" column to "SW". Note that we specify "regex = True" so that Pandas
## will interpret the strings as regular expressions, but if you were to change this to False or
## omit this argument, then Pandas would replace text on a literal basis:
bike_locations_nw["ADDRESS"] = bike_locations["ADDRESS"].replace(to_replace ="NW", value = "SW", regex = True) 

## As you may have surmised, there are many other regular expression syntactic cues such
## as "$", "^", and "+" that each have their own uses in regular expressions. These are
## beyond the scope of this training, but they are extremely powerful and you can make
## use of them using the contains and replace methods.









