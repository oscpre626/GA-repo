Python 3.11.2 (main, Sep 14 2024, 03:00:30) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> import qwiic serlcd
SyntaxError: incomplete input
>>> import qwiic-serlcd
SyntaxError: invalid syntax
>>> import-qwiic-serlcd
SyntaxError: invalid syntax
>>> import qwiic_serlcd
>>> myLCD = qwiic_serlcd.QwiicSerlcs()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    myLCD = qwiic_serlcd.QwiicSerlcs()
AttributeError: module 'qwiic_serlcd' has no attribute 'QwiicSerlcs'. Did you mean: 'QwiicSerlcd'?
>>> myLCD = qwiic_serlcd.QwiicSerlcd()
>>> myLCD.clearScreen
<bound method QwiicSerlcd.clearScreen of <qwiic_serlcd.QwiicSerlcd object at 0x7fab514950>>
>>> myLCD.clearScreen()
>>> myLCD.print("shabo är bäst")
True
>>> myLCD.print("oscarojoel har gjort GA")
True
>>> myLCD.clearScreen()
>>> myLCD.setCursor(o,1)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    myLCD.setCursor(o,1)
NameError: name 'o' is not defined
>>> myLCD.setCursor(0,1)
>>> myLCD.print("f*k pip")

True



