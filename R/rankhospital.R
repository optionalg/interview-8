rankhospital <- function(state, outcome, num = "best") {
  ## Read outcome data
  outcome.data <- read.csv("outcome-of-care-measures.csv", colClasses = "character", na.strings = "Not Avalible")
  ## Check that state and outcome are valid
  if (is.element(state, outcome.data$State)){
    outcome.state.subset <- outcome.data[(outcome.data$State == state),]  
  } else {
    stop("invalid state")
  }
  if (outcome == "heart attack"){
    outcome <- 11
  } else {
    if (outcome == "heart failure"){
      outcome <- 17
    } else {
      if (outcome == "pneumonia"){
        outcome <- 23
      } else {
        stop("invalid outcome")
      }
    }
  }
  outcome.state.subset <- outcome.data[(outcome.data$State == state),]
  outcome.state.ordered.subset <- outcome.state.subset[order(as.numeric(outcome.state.subset[,outcome]), as.character(outcome.state.subset$State)),]
  outcome.state.ordered.subset.na.rm <- outcome.state.ordered.subset[complete.cases(outcome.state.ordered.subset[,outcome]),]
  count <- nrow(outcome.state.ordered.subset.na.rm)  
  if (num == "best"){
    num = 1
  } else{
    if (num == "worst"){
      num = count
    } else{
      num = num
    }
  }
  ## Return hospital name in that state with lowest 30-day death
  ## rate

  rank <- outcome.state.ordered.subset.na.rm[num,]
  name = 2
  hospital.names <- rank[,name]
  hospital.names <- hospital.names[order(hospital.names)]
  hospital.names[1]
}