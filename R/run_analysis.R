#run_analysis.R homework Data Clearning
setwd("C:/Users/Nathan/Documents/R/Projects/Coursera Johns Hopkins University Data Science/Getting and Cleaning Data/getdata-projectfiles-UCI HAR Dataset/UCI HAR Dataset/")
#
rm(list=ls())
con = url("https://d396qusza40orc.cloudfront.net/getdata%2Fprojectfiles%2FUCI%20HAR%20Dataset.zip")
# read subject column in to vector
subject_test <- read.table("./test/subject_test.txt")
subject_train <- read.table("./train/subject_train.txt")
subject <- rbind(subject_test,subject_train)
colnames(subject) <- c("subject")
subject$subject <- as.factor(subject$subject)  #to make analysis easier
#
# read activity codes into vector
activity_y_test <- read.table("./test/y_test.txt")
activity_y_train <- read.table("./train/y_train.txt")
activity <- rbind(activity_y_test, activity_y_train)
colnames(activity) <- c("activity")
# activity_labels --names walking etc.. make activity a factor  
dummy <- scan("./activity_labels.txt", what = "character", sep=" ")
s1 <- seq(2, length(dummy), by= 2)
activity_labels <- dummy[s1]
activity$activity <-factor(activity$activity, labels = activity_labels)  # problem
#
# read in feature data X to data frames
X_test <- read.table("./test/X_test.txt")
X_train <- read.table("./train/X_train.txt")
X_both <- rbind(X_test, X_train)
#
# feature names
dummy <- scan("./features.txt", what = "character", sep = " ")
s1 <- seq(2,length(dummy), by= 2)
features <- dummy[s1]
# add labels for features columns data
names(X_both) <- features
#

# column bind subject code, activity code and feature data 
temp_data <- cbind(subject, activity)
temp_data <- cbind(temp_data, X_both)
##str(tity_data)
# select column variables with mean |and standard dev
# use grep to find m/Mean and STD, std (l*) [Mm][Ee][Aa][Nn] | [Ss][Dd][Ee]
keepmeans <- grep("[Mm][Ee][Aa][Nn]", names(temp_data))  # select means
keepSTDs <- grep("[Ss][Tt][Dd]", names(temp_data))  # select std's
keepVars <- append(keepmeans, keepSTDs, after = length(keepmeans))
onetwo <- c(1,2)  # subject and actvity
keepVars <- append(onetwo, keepVars, after = length(onetwo))
keepVars <- sort(keepVars)  # list of variable column numbers to keep with mean or std
# also keep column one ,, subject code and activity 
# selecte mean and std feature variables from temp_tity_data to make tity_data
tidy_data <- temp_data[,keepVars]
#  finished first part
# 
# install needed and extra libraries
library(plyr)
library(reshape)
library(reshape2)
mtidy_data <- melt(tidy_data)  # meld the data frame with the two factor variables -subject and activity as IDs
#
meansbysubjectactivity <-cast(mtidy_data, ... ~ variable, mean) #means for each subject's activities
# write the tidy data to a file
write.csv(meansbysubjectactivity, file= "tidy_data.txt", row.names=FALSE)
#data <- read.csv("tidy_data.txt")    #use this to read the data back
#View(data)  # use this to quickly View the data