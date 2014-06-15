best <- function(state, outcome) {
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
  name = 2
  ## Return hospital name in that state with lowest 30-day death
  ## rate
  minium <- min(as.numeric(outcome.state.subset[,outcome]), na.rm= TRUE)
  outcome.state.min.subset <- outcome.state.subset[which(as.numeric(outcome.state.subset[,outcome]) == minium),]
  hospital.names <- outcome.state.min.subset[,name]
  hospital.names <- hospital.names[order(hospital.names)]
  hospital.names[1]
}
