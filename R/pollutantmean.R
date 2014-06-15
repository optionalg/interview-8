pollutantmean <- function(directory, pollutant, id = 1:332) {
  ## 'directory' is a character vector of length 1 indicating
  ## the location of the CSV files
  
  ## 'pollutant' is a character vector of length 1 indicating
  ## the name of the pollutant for which we will calculate the
  ## mean; either "sulfate" or "nitrate".
  
  ## 'id' is an integer vector indicating the monitor ID numbers
  ## to be used
  
  ## Return the mean of the pollutant across all monitors list
  ## in the 'id' vector (ignoring NA values)
  pollutants <- list()
  for (i in id) {
    i <- formatC(i, width = 3, format = "d", flag = "0")
    data <- read.csv(paste(directory,"/",i,".csv", sep = ""))
    column.location <- which(colnames(data)== pollutant)
    data.subset <- na.omit(data[,column.location])
    pollutants <- c(pollutants,data.subset)
  }
  round(mean(as.numeric(pollutants), na.rm = FALSE), digits = 3)
}