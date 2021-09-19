# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 15:20:33 2021

@author: GuzmanMJ
"""

##################################
##################################
#####PYTHON PANDAS TRAINING 5#####
##################################
##################################

import os, pandas as pd, csv, re, numpy as np
os.chdir("[FILE PATH]/Python Pandas Training")

###########
###INTRO###
###########
## Congratulations on making it this far in the Python Pandas Training! At this point, you are
## a full-fledged Python Pandas Professional, and you should feel prepared to take on any
## standard data project using Python or Pandas. At this point, you can import data, complete
## basic and complex manipulations, use numpy to edit data conditionally, use loops with ease,
## and you can create data visualizations in Python.

## This lesson is best described as "Beyond Pandas." Here, we explore two potentially useful
## data applications of Python, and we show how these could be applied to typical data work.
## The first of these tasks is an omnipresent problem in datascience: cleaning messy data.
## In the example below, we show how you could clean a CSV file prior to importing it to avoid
## a messy import. In the second example, we show how you could even create data from large
## text files. The idea here is to use Python to creatively analyze things that don't appear
## to be data at first glance. After we complete these, we import the data we created using
## Pandas.

## As you may have surmised, these tasks are not strictly speaking necessary for standard data
## work. That being said, these are examples of creative ways in which you can use data science
## to answer questions. Keeping these skills and tools in mind, you will be prepared to solve
## a broad array of problems in data and economics, and these could lead to important new results.


###############################
###CLEANING CHALLENGING DATA###
###############################
## Let's use Pandas to import some messy csv data. Start by trying to do a standard import on the
## messy milk data below:
messy_milk_data = pd.read_csv("RawData/milkutil_uk_13aug15.csv")

## Having run the command above, you will note that it didn't work. Spyder threw up an error
## due to an "invalid start byte". To fix this, we can use the following prcedure:
fin = open("RawData/milkutil_uk_13aug15.csv", "rt", encoding = "utf-16", errors = "ignore")
fout = open("IntermediateData/milk_cleaned.csv", "wt", encoding = "utf-8")
for line in fin:
    line = line.replace("  ", ",")
    line = line.replace("\t", ",")
    fout.write(line)
fin.close()
fout.close()

## If you completed the Python Trainings prior to this, then this might look a little familiar.
## Here, we open the raw file with the utf-16 encoding, and we tell Python to ignore reading
## errors. Then, we open an output file with a more standard utf-8 encoding. Finally, we loop
## through each line of the input file and replace double spaces and tabs with commas, and we
## rewrite this edited text to the output file.

## Once we complete this procedure, we can import the data normally below:
messy_milk_data = pd.read_csv("IntermediateData/milk_cleaned.csv")

## Now, we have fully imported the data, but it's still a little messy. Let's clean it up a bit
## and export the cleaned data. First, drop off the first 29 rows as these appear to be annual
## and the rest of the data is monthly.
cleaned_milk_data = messy_milk_data.tail(len(messy_milk_data) - 29)

## Next, rename the columns we want to keep
cleaned_milk_data = cleaned_milk_data.rename(columns = {"UK Availability":"uk_availibility", "Disposals and Production of Milk and Milk Products Year": "disposals_and_productions", 
                                                        "AVAILABILITY of RAW MILK UK Milk": "raw_milk_avail", " Production million litres": "production",
                                                        "AVAILABILITY of RAW MILK Imports": "raw_milk_avail_imports", 
                                                        "AVAILABILITY of RAW MILK Total Available million litres": "total_avail",})
    
## Finally, keep the columns we want
cleaned_milk_data = cleaned_milk_data[["uk_availibility", "disposals_and_productions", "raw_milk_avail", "production", "raw_milk_avail_imports", "total_avail"]]

## Voila, our milk data is cleaned from a messy csv to a cleaned dataframe!

## Notably, this is just one example of how you could clean a messy csv file using Python.
## There are in fact many different modules and approaches that have been developed for this
## exact purpose. The broader goal here is to show that you don't NEED to use a "data tool"
## to work with data. As you work more in Python, you might start to find solutions to problems
## outside of Pandas, and these work-arounds will be infintely useful when you're dealing with
## a strange problem like this one.


###################
###CREATING DATA###
###################
## Let's finish the Pandas Training with a really funky project. Here, we are going to explore a
## way to "create" data from something that we typically wouldn't think of as data. In this case,
## that will be the scripts from several Pixar movies, namely "A Bug's Life," "Finding Nemo," "Monsters
## Inc.," and "The Incredibles." 

## What kinds of information could we glean just from the scripts of these movies? In fact, we can
## use our training in regular expressions to learn all sorts of things. In this case, we are going
## to find out how often characters in this Pixar files use the words "attack," "fight," and "run."
## Once we find these words in the scripts, we are going to identify the character that said each
## word, the line in which they said it, and specify the movie in which the character said it.
## The output of this will be a dataframe with output four columns: the character that said the
## word, the word in question, the line in which the character said it, and the movie title.

## Let's kick things off by finding each line of the scripts in which the words we want are written.
## First, set up the directory that contains the files you need
files = os.listdir("RawData/Pixar Scripts")

## Now, set up a regular expression for each of the three words that we are looking for. Recall from
## the Python Trainings that ".*" implies any number of characters up to the end of the line.
attack_regex = re.compile(r".*attack.*")
fight_regex = re.compile(r".*fight.*")
run_regex = re.compile(r".*run.*")

## Now, run a loop over each of the files in the directory to find the words we're looking for.
## Begin by setting the "matches"and "titles" lists to empty lists so that you have something
## to append the results to.
matches = []
titles = []

## Next, run the loop for each file in the list of files in the directory (you set up the "files"
## list up above). In each run of the loop, you will set the "content" variable equal to the contents
## of the file of that loop (i.e., "content" will equal the entire text of one of the four movies).
for file in files:
    text = open(os.path.join("RawData/Pixar Scripts", file))
    content = text.read()
    mo = []
    mu = []
    ma = []
    ## Now that you've set up the content variable, set up an exception for when the attack_regex is
    ## not None. In this case, set the "mo" list equal to all of the results of the attack_regex, append
    ## each value from the mo list to the "matches" list. Additionally, append the value of the filename
    ## to the "titles" list each time there is a match as well.
    if attack_regex.search(content) != None:
            mo = attack_regex.findall(content)
            for i in range(len(mo)):
                matches.append(mo[i])
                titles.append(str(file)[:-4]) #this slices the file extension off the filename
    ## As with the attack_regex, do the same with the fight_regex
    if fight_regex.search(content) != None:
            mu = fight_regex.findall(content)
            for i in range(len(mu)):
                matches.append(mu[i])
                titles.append(str(file)[:-4]) #this slices the file extension off the filename
    ## As with the attack and fight regexes, do the same with the run_regex
    if run_regex.search(content) != None:
        ma = run_regex.findall(content)
        for i in range(len(ma)):
            matches.append(ma[i])
            titles.append(str(file)[:-4]) #this slices the file extension off the filename
    
## Finally, write the results to a text file. This uses the csv module to create a csv file.
## Once the csv file is open, the loop below writes each row as the value of the match list
## followed by the value of the titles list, where both lists are indexed by the same line
## number. If there are no matches, then the loop prints "No 'attack', 'fight', or 'run' matches found."
## Note that these also prints each row to the console. This is really just for show though so that you
## have a sense for what the script is actually doing.
outputFile = open("Output/Pixar Movie Search Results.csv", "w", newline = "", encoding = "utf-8")
outputWriter = csv.writer(outputFile)
outputWriter.writerow(["Line", "Movie"])
if len(matches) > 0:
    for line in range(len(matches)):
        row = [str(matches[line]).strip("\n"), str(titles[line])]
        print(row)
        outputWriter.writerow(row)
else:
    print("No 'attack', 'fight', or 'run' matches found.")
outputFile.close()

## Now that we have actually found all of our matches, we can import the results from the
## csv file into Pandas as usual
pixar_results = pd.read_csv("Output/Pixar Movie Search Results.csv")

## Cleaning up a little, drop rows that don't contain a colon. Each character name is
## followed by a colon in the movie scripts, so we can use this pattern to our advantage
## as we identify the character names in the next step.
pixar_results = pixar_results[pixar_results["Line"].str.contains(":")]

## Find the character names by taking all of the text to the left of the colon in each
## cell. This is techinically taking the first grouping of the split function result.
pixar_results["Character"] = pixar_results["Line"].str.split(":").str[0]

## Finally, identify the word that the search found to output each line. This uses the numpy
## "where" function to conditionally create the "word_matches" variable.
pixar_results["word_matches"] = np.where(pixar_results["Line"].str.contains("attack"), "attack", "")
pixar_results["word_matches"] = np.where(pixar_results["Line"].str.contains("fight"), "fight", pixar_results["word_matches"])
pixar_results["word_matches"] = np.where(pixar_results["Line"].str.contains("run"), "run", pixar_results["word_matches"])

## Order the columns for ease
cols = ["Character", "word_matches", "Line", "Movie"]
pixar_results = pixar_results[cols]

## With that, you have have created cleaned data from long text files. The text files had no
## variable names, delimiters, or any sense of data, and you "created" data from them anyway.
## You could now make a bar graph of how often these words are used in different Pixar movies,
## or you could expand the search to find other words, or you could identify specific characters
## and edit the script to return all of that character's lines. These and many other options are
## possible to analyze these movie scripts. The main takeaway here is that data is truly just
## comprised of information, and just because information doesn't appear to fit cleanly into
## a dataframe doesn't mean that you can't find a way to make it clean.

## Congratulations again on completing the Python Pandas Trainings! You did it!!!


