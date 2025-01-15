import qwiic_serlcd
myLCD = qwiic_serlcd.QwiicSerlcd()
myLCD.clearScreen()
myLCD.print("shabo är bäst")
myLCD.print("oscarojoel har gjort GA")
myLCD.clearScreen()
myLCD.setCursor(0,1)
myLCD.print("f*k pip")



