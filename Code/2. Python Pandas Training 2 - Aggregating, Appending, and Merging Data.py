# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 11:12:26 2021

@author: GuzmanMJ
"""

####################################
####################################
#####PYTHON PANDAS TRAINING TWO#####
####################################
####################################

###########
###INTRO###
###########
## Welcome to Python Pandas Training 2! This training builds on the basic data manipulation
## tools you learned in lesson 1 as we learn how to rename, sort, append, merge,
## aggregate, and reshape data in Pandas. These represent some slightly higher level data
## tools, but they should definitely be in your standard Pandas toolkit. As in
## Lesson 1, start by importing the pandas module.

import pandas as pd


##########################
###RENAMING AND SORTING###
##########################
## As we get started, let's import the insurance dataframe from lesson 1 and select
## the variables that we'll need for this training:
insurance = pd.read_excel("[FILE PATH]/Python Pandas Training/RawData/2-2016_QHP_Landscape_Individual_Market_Medical.xlsx",
                          sheet_name = "Data_AK-MT")

## Here, we select the three variables that we want to keep in the merge below -
## State Code, Plan ID, and Plan Type:
insurance = insurance[["State Code", "Plan ID (Standard Component)", "Plan Type"]]

## One thing that might be useful prior to sorting is renaming. Renaming is really
## a matter of preference in most data tools, and the same can be said for Pandas.
## Furthermore, as you may have noticed, variables are always referenced by their
## names inside of a string in Pandas. This implies that there are no specific
## requirements for Pandas variable names. Variables can begin with numbers, include
## spaces or special characters, and can be any case. That being said, you can use
## the "pd.DataFrame.rename()" method if you do want to rename variables:
insurance = insurance.rename(columns = {"State Code":"state_code", "Plan ID (Standard Component)": "plan_id", "Plan Type": "plan_type"})

## The above command renames "State Code" to "state_code", "Plan ID (Standard Component)"
## to "plan_id", and "Plan Type" to "plan_type". Note the use of the curly brackets around
## the names and colon to indicate the new name of the variable. Additionally, this 
## list of newly named variables is passed to the "columns" parameter, which is
## different from the "index" parameter if you prefer to rename columns by their indices.

## If you recently completed the Python Trainings, then you may recognize the curly brackets
## and the colons to be indicative of a Python dictionary. No need to remember this,
## but techinically, the "pd.DataFrame.rename()" method assigns new names to variables
## based on their value in the "columns" dictionary.

## Now that we have imported, selected the variables we needed, and renamed variables,
## we are now ready to sort. To sort the "insurance" dataframe, we can use the 
## "pd.DataFrame.sort_values()" method. The arguments of the "pd.DataFrame.sort_values()" 
## method are the variables by which you are sorting:
insurance = insurance.sort_values("plan_type")

## If you want to sort by multiple variables, it will be useful to use all of the
## arguments in the "pd.DataFrame.sort_values()" method:
insurance = insurance.sort_values(by = ["state_code", "plan_type"], ascending = [True, False])

## In this sort, we sorted by two variables. These correspond in order to our specification
## of "ascending", so we sorted in ascending (or alphabetical) order on state_code and
## in descending (or reverse-alphabetical) order on plan_type.


###########################
###APPENDING AND MERGING###
###########################
## Similar to the "pd.DataFrame.sort_values()" method that we just looked at, the
## "pd.DataFrame.append()" method is reasonably straightforward and can be used to
## to append DataFrames. To append a dataframe, import another dataframe, subset,
## and rename to the same column names that you set up in the "insurance" dataframe:
insurance2 = pd.read_csv("[FILE PATH]/Python Pandas Training/RawData/5-2016_QHP_Medical_Service_Pricing.csv")

## List the variables names so we know what to subset to, then keep the vars we need:
list(insurance2)
insurance2 = insurance2[["StateCode", "PlanIDStandardComponent", "PlanType"]]

## rename as above
insurance2 = insurance2.rename(columns = {"StateCode":"state_code", "PlanIDStandardComponent": "plan_id", "PlanType": "plan_type"})

## Now, use the "pd.DataFrame.append()" method to append these dataframes. Note that
## we apply the "pd.DataFrame.append()" method to the "insurance" dataframe as the base,
## and we append insurance2 to it. The argument inside "pd.DataFrame.append()" is just
## the dataframe or other object that you are appending:
insurance_appended = insurance.append(insurance2)

## Note that you can append dataframes with variables that do not match. Pandas
## will just append the variable names that do match and create blank or missing
## observations for the variables that don't match.

## Merging dataframes is syntactically similar to appending dataframes in Pandas.
## Prior to merging, let's import a dataframe of state abbreviations to their
## names to merge in:
state_codes = pd.read_csv("[FILE PATH]/Python Training/2020/RawData/states_abbrev.csv")

## If you view this dataframe in the Viewer, you'll see that it is a dataframe with
## two variables: one of state abbreviations and one of state names. We could rename
## the variables prior to merging if we wanted, but we can also merge directly in
## the following "pd.DataFrame.merge()" method:
insurance_merged = insurance_appended.merge(state_codes, left_on = "state_code", right_on = "Abbreviation:")

## Pandas uses SQL syntax to complete merges, so "join" terminology will come in handy.
## By default, Pandas runs an "inner join" in a merge which only keeps observations
## that are present both dataframes. The dataframe outside of the "merge" statement is
## the "left" dataframe and the dataset on the inside is the "right" dataframe, and
## the left_on and right_on parameters specify which variables on which to merge
## from each dataframe respectively.

## You can use the "how" parameter to adjust which SQL join Pandas will complete.
## The options are "inner", "outer", "left", and "right", and you can get more
## detail on each of these types of joins in the documentation. A word of warning:
## a join is different from a standard merge in that observations are allowed
## to be duplicated in both datasets (or a many to many merge). You don't need
## to fully understand this right now, but make sure to carefully inspect your dataframes
## before and after merges to ensure that you are getting the expected results.


#################
###AGGREGATING###
#################
## Now, let's dive in to aggregating (or collapsing) data. In a straightforward
## sense, you can use the pd.DataFrame.aggregate() method to aggregate data over
## an entire dataset. In the following example we create a count variable in the
## insurance_merged dataframe and aggregate the entire dataframe:
insurance_merged["test"] = 1
insurance_merged_sum = insurance_merged.aggregate(["sum", "mean"])

## If you look at the output insurance_merged_sum dataframe, you will notice that
## all of the string variables were concatenated in the "sum" row and the "test" variable
## was summed, creating a count of the number of observations. The string variables
## provided no output for the "mean" row, and we find that the mean of the "test"
## variable was 1.

## Whereas aggregate would always be a good choice for summary statistics, we often
## want to produce output for aggregated groups of observations. Once again, Pandas
## takes from the SQL syntax (and the "dplyr" syntax in R) to run this type of aggregation.
## you can aggregate data by group by using the "pd.DataFrame.groupby()" method.
## Let's aggregate the test variable in the insurance_merged dataframe based on the
## "US State:":
insurance_merged_agg = insurance_merged.groupby(by = "US State:", as_index = False)["test"].sum()

## Let's break this line down. Here, we applied the groupby method to insurance_merged and
## we grouped by "US State:". Then, we specified as_index = False. While not strictly
## necessary, this controls whether the new groups will serve as row names in your
## output. Following this, we selected the numeric variables that we want to see when we
## analyze our groups. Finally, we apply a SECOND method to the grouped output that is
## "pd.DataFrame.sum()" which specifies how we want to aggregate the numeric variable.

## This is easiest to read from left to right: The insurance_merged dataframe is
## being grouped, and then the groups are being aggregated by taking the sum.
## the "pd.DataFrame.groupby" does not create any output on its own, so the specification
## of the summary statistic is necessary to see the results.

## In addition to this aggregation, you can easily add additional variable to
## the grouby statement in a list:
insurance_merged_agg = insurance_merged.groupby(by = ["US State:", "plan_type"], as_index = False)["test"].sum()


###############
###RESHAPING###
###############
## One additional important tool in the Pandas arsenal are the pivot and melt
## tools to reshape data. To explore these, let's reimport the excel file that we
## imported in Lesson 1.
insurance3 = pd.read_excel("[FILE PATH]/Python Pandas Training/RawData/2-2016_QHP_Landscape_Individual_Market_Medical.xlsx",
                          sheet_name = "Data_AK-MT")

## Now, subset to just the columns we want to use in the reshape. This is not strictly
## necessary as the reshape command will automatically keep the variable you specify,
## but this helps to be clear about what data we're reshaping.
insurance3 = insurance3[["State Code", "County Name", "Plan ID (Standard Component)", "Premium Adult Individual Age 21",
                          "Premium Adult Individual Age 27", "Premium Adult Individual Age 30 ", "Premium Adult Individual Age 40 ",
                          "Premium Adult Individual Age 50 ", "Premium Adult Individual Age 60 "]]

## This following command uses the "pd.DataFrame.melt()" method to reshape the data from
## wide to long. This uses similar syntax to dplyr's "melt" command in R if you're familiar
## with that tool. The "id_vars" will be the columns in your output, and the "value_vars"
## will comprise a new column of values in the output.
insurance_long = insurance3.melt(id_vars = ["State Code", "County Name", "Plan ID (Standard Component)"], 
                                            value_vars = ["Premium Adult Individual Age 21", "Premium Adult Individual Age 27", 
                                                          "Premium Adult Individual Age 30 ", "Premium Adult Individual Age 40 ",
                                                          "Premium Adult Individual Age 50 ", "Premium Adult Individual Age 60 "])

## To take this back to wide format, we can use the "pd.DataFrame.pivot_table()" method. This is a
## generalized reshape command that will aggregate values in the case that there are duplicates in
## your dataset. In this case, we know that there are no duplicates in terms of the id_vars
## (we just reshaped, so we're definitely ok), so we don't need to worry about any aggregation
## here. In case you do have duplicated values in your dataframe though, note that the default
## aggregation function is to take the average of the numeric observations. Use the 
## "pd.DataFrame.pivot_table()" method to reshape below::
insurance_wide = insurance_long.pivot_table(index = ["State Code", "County Name", "Plan ID (Standard Component)"], columns = ["variable"], values = ["value"])

## Breaking this down, we set an index as the id_vars, specified the columns from which to take
## the new variable names, and the values with which to populate those new columns. If you
## look at the data viewer however, you may notice that we are missing the id variables
## from the original dataset. They have in fact been concatenated in the indices or rownames,
## so you need to reset the index in order to convert them back into columns. You can do this
## easily using the "pd.DataFrame.reset_index()" method:
insurance_wide = insurance_wide.reset_index()

## Additionally, there is no need to do this separately! You can reshape and apply the
## "pd.DataFrame.reset_index()" method in one line as below:
insurance_wide = insurance_long.pivot_table(index = ["State Code", "County Name", "Plan ID (Standard Component)"], 
                                                     columns = ["variable"], values = ["value"]).reset_index()

## And this brings us back to our original dataframe.






