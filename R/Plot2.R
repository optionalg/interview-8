#read in dataset
setwd("C:\\Users\\Nathan\\Documents\\R\\Projects\\Coursera Johns Hopkins University Data Science\\Exploratory Data Analysis\\")
unzip("exdata-data-household_power_consumption.zip")
data <- read.table("household_power_consumption.txt", header = TRUE, sep = ";", na.string = "?")
#process date
data$DateTime <- paste(as.character(data$Date), as.character(data$Time), sep = " ")
data$DateTime <- strptime(data$DateTime,"%d/%m/%Y %H:%M:%S")
data$Date <- as.Date(data$Date, "%d/%m/%Y")
#subset data
data <- subset(data, Date == "2007-02-01" | Date == "2007-02-02")
#create plot2
plot(data$DateTime, data$Global_active_power, cex=0.0, xlab= " ", 
     ylab = "Global Active Power (kilowatts)")
lines(data$DateTime, data$Global_active_power)
mtext("Plot 2", outer=TRUE, adj = 0)
dev.copy(png, file = "plot2.png", width = 480, height = 480)
dev.off()