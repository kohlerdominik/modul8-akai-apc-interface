currentPage = 100

#MIDI NOTE VALUES OF EACH SECTION
fader = [48, 49, 50, 51, 52]
page = [56, 57, 58, 59, 60, 61, 62, 63]
media = [50, 51, 52, 53, 42, 43, 44, 45, 34, 35, 36, 37, 26, 27, 28, 29]
layerMute = [64, 65, 66, 67, 68, 69, 70, 71]
fx = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14]

#INITIALIZE MEDIA PAGES IN GREEN
for i in page:
   modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', i, 1)

#INITIALIZE VIDEOS IN RED
for i in media:
   modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', i, 3)

#INITIALIZE SPECIAL MEDIA IN ORANGE
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 55, 5)

#INITIALIZE LAYER ON/OFF BUTTONS
modul8.setValue('ctrl_layer_hidden', True, -1)

#INITIALIZE FX BUTTONS
modul8.setValue('ctrl_layer_auto_moveOn', False, -1)
modul8.setValue('ctrl_layer_auto_scaleOn', False, -1)
modul8.setValue('ctrl_layer_auto_colorOn', False, -1)
modul8.setValue('ctrl_layer_auto_rotateOn', False, -1)
modul8.setValue('ctrl_layer_transformer_on', False, -1)
modul8.setValue('ctrl_layer_pixelFX_saturationOn', False, -1)

modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 7, 3)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 5, 5)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 4, 5)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 3, 5)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 2, 5)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 8, 5)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 9, 5)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON',10, 5)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 11, 5)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 12, 5)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 13, 5)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 39, 3)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 31, 3)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 23, 3)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 15, 3)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 40, 1)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 32, 1)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 24, 1)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 16, 1)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 41, 1)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 33, 1)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 25, 1)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 17, 1)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 48, 5)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 49, 5)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 46, 1)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 38, 1)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 30, 1)
modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 22, 1)
