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
#create plot4
par(mfrow = c(2,2))
#plot 1
plot(data$DateTime, data$Global_active_power, cex=0, xlab= " ", 
     ylab = "Global Active Power (kilowatts)")
lines(data$DateTime, data$Global_active_power)
#plot2
plot(data$DateTime, data$Voltage, cex=0, xlab = "datetime",
     ylab = "Voltage")
lines(data$DateTime, data$Voltage)
# plot3
with(data, plot(DateTime, Sub_metering_1, type = "n",
                ylab = "Energy sub metering", xlab = " "))
with(data, lines(DateTime, Sub_metering_1, col = "black"))
with(data, lines(DateTime, Sub_metering_2, col = "red"))
with(data, lines(DateTime, Sub_metering_3, col = "blue"))
legend('topright', pch = "_", col = c("black", "red","blue"), 
       legend = c("Sub_metering_1", "Sub_metering_2", "Sub_metering_3"))
#plot4
plot(data$DateTime, data$Global_reactive_power, xlab = "datetime", 
     ylab = "Global_reactive_power", type = "n")
lines(data$DateTime, data$Global_reactive_power)
dev.copy(png, file = "plot4.png", width = 480, height = 480)
dev.off()