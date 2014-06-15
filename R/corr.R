corr <- function(directory, threshold = 0) {
  ## 'directory' is a character vector of length 1 indicating
  ## the location of the CSV files
  
  ## 'threshold' is a numeric vector of length 1 indicating the
  ## number of completely observed observations (on all
  ## variables) required to compute the correlation between
  ## nitrate and sulfate; the default is 0
  
  ## Return a numeric vector of correlations
  source("complete.R")
  counts <- complete("specdata", id = 1:332)
  corralation <- numeric()
  subset.nobs <-subset(counts, nobs > threshold)
  for (i2 in subset.nobs$id){
    i2 <- formatC(i2, width = 3, format = "d", flag = "0")
    data2 <- read.csv(paste(directory,"/",i2,".csv", sep = ""))
    data2 <- data2[complete.cases(data2),]
    corraltion.data <- cor(data2$sulfate, data2$nitrate)
    corralation <- c(corralation, corraltion.data)
  }
corralation
}

