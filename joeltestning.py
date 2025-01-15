import qwiic_serlcd
import explorerhat as eh

myLCD = qwiic_serlcd.QwiicSerlcd()
myLCD.clearScreen()
myLCD.print('Hejsan svejsan!')
myLCD.setCursor(0,1)
myLCD.print('Joel och Oscar')


