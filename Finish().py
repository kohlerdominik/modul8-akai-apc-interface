#TURN OFF LEDS
for i in range (0, 98):
   modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', i, 0)
