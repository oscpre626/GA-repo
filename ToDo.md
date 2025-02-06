1. Skapa skript för två sensorer
- Sätt på och stäng av sensorerna för att sedan sätta på båda sensorena igen. (eh.output.one/two.on/off)
- Använd XSHUT för att stänga ner en av sensorerna först och ändra adressen på den aktiva. ()
- Sätt på och ändra adressen på den andra sensorn utan att stänga av den första sensorn (tror jag)
- Stäng av båda sensorerna för att reseta dem och sätt till sist på dem igen
- Använd time.sleep(0.1) eller liknande
- PWM, config pwm för våra motorer kombinerat med sensorernas output så vi kan svänga bra
