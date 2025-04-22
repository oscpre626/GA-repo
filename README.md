# Guide för vår produkt #
# Inlogg till Raspberry Pi connect. Användarnamn: oscpre626@edu.linkoping.se, Lösenord: oscarojoel #
# Inlogg till Raspberry Pi datorn. Användarnamn: ojGA, Lösenord: ojGA #

!Viktigt! Uppdatera INTE datorn om en sådan knapp/ notis kommer upp. Vi behöver inte ta några onödiga risker nu eller hur? 
Powerbanken är inte riktigt stark nog för att stödja all uppkopplad elektronik så displayen som sitter ovanpå powerbanken får inte vara ikopplad medans man kör "Final-sensor-motor.py" då allt vanligtvis sätts igång. Om ni vill testa den kan ni köra "jonathaGOAT-edit.py" skriptet

1. Hur man kopplar alla enheter och sladdar till bilen
   - Sätt i rätt sladd i rätt uttag på ovansidan av Raspberry Pi:n
   - *Man ska inte sätta dit någon sladd på det blåa området
   - De fyra sladdar som sitter i klämmor är för motorerna och ska kopplas till motoruttagen. Den gula och orangea hör ihop medan den gröna och röda hör ihop. Den gröna respektive gula sladden ska sitta på någon av de negativa motoruttagen medan den orangea och röda sitter på en av de positiva motoruttagen. Om man sätter den gröna på -1 ska den röda sitta på +1, då sitter gul på -2 och orange på +2. Den enskilda orangea sladden är till för en av sensorerna och ska sitta på output 1. Den enda svarta sladden ska sättas i GND-uttaget.
    ![20250410_105910](https://github.com/user-attachments/assets/df341f07-15d1-43e2-9441-a37327e2898a)
   - De svarta, röda, blå och gula sladdarna som är tvinnade är till för sensorerna. Den röda tvinnade sladden ska sättas i 3v3-uttaget. Den gula tvinnade sladden ska sättas i SCL-uttaget och den blåa tvinnade sladden ska sättas i SDA-uttaget. Den svarta sladden sitter på GND som sagt.
    ![20250410_110707](https://github.com/user-attachments/assets/73df1723-b003-4471-88ea-a1b13c92c470)
   - Den orangea JBL kabeln är datorns strömkabel och sätts in under ettan. Den sätts in i USB-uttaget längst från power-knappen då det andra uttaget inte fungerar som output. Under tvåan på explorer HAT Pro finns datorns bildskärmsanslutning, som tar emot micro USB-C kablar. Sätt först in micro USB-C HDMI adaptern och koppla sedan en HDMI sladd via adaptern till en skärm. Tangentbord och mus kopplas till USB-uttagen vid sidan av datorn. Om man vill kan man koppla en LAN-kabel till datorn, men om man vill köra bilen trådlöst behöver man tilldela sin mobildata till bilen.
    ![20250410_111558](https://github.com/user-attachments/assets/b051b32f-b079-4c30-bb56-ea05fffd9450)

2. Uppkoppling med trådlös anslutning
     - När man väl sätter i strömkabeln i datorn kommer den startas automatiskt och man blir då inloggad. För att fixa trådlös anslutning till bilen måste man fixa några få saker. Först behöver man ansluta bilen till eran mobildata för att orestrikterat (skolans nätverk är rätt reglerat) kunna skräm projicera bilens skärm.
       ![image](https://github.com/user-attachments/assets/bcc52b7b-7062-4918-b740-e8bf6817c4c3)
     - Sedan behöver man ha Raspberry Pi Connect på. Bilden nedan visar hur det ser ut när Raspberry Pi Connect är igång. Om Raspberry Pi:n kräver inlogg av något slag bör vi sagt det till er, men om vi inte gjort det är det bara att fråga. (Repot är ju public).. När ni väl aktiverat Raspberry Pi Connect får ni skifta fokus till den dator ni vill ha skärm projiceringen på. Gå in på denna länk: https://www.raspberrypi.com/software/connect/ och klicka "Sign in". Ni får logga in med Oscars email och lösenordet bör vi ha sagt till er. När ni loggat in på kontot bör ni se en enhet som heter "ojGA". På högra sidan av samma ruta som innehåller "ojGA" bör det finnas en knapp som säger "Connect via". Klicka på den knappen och välj "Screen sharing", det kan dröja lite innan man får sin projicerad bild. Om ni inte ser "Connect via" knappen beror det ofta på att webbsidan är väldigt seg med att känna av när man aktiverat Raspberry Pi Connect, ge den 3-5 minuter så bör den dyka upp.
      ![image](https://github.com/user-attachments/assets/1e6dfb8f-454c-4cf6-954e-e771d9712a6e)

3. Andra saker som är värt att ta upp
     - För att hitta våra skript behöver man gå in i datorns filsystem. Klicka på mapp-ikonen för att öppna filsystemet, ni bör börja i hemkatalogen "ojGA". Sedan går ni in i "GA-repo" och voila, där har ni massa (främst helt värdelösa) skript. De enda viktiga skripten finns i mappen "Bra-filer"
      ![image](https://github.com/user-attachments/assets/76e2f88f-7382-454d-85ca-671e8ebc67d9)
     - För att stänga av datorn följer ni bilden nedan. Om ni råkar bli utloggade bör vi ha sagt inlogget, fråga annars.
      ![image](https://github.com/user-attachments/assets/7ec17b6c-6963-44c2-af4b-4be136cbac85)
