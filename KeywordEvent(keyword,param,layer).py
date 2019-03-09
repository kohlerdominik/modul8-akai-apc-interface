#Light Color Values
# 0 - Off
# 1 - Green
# 2 - Flashing Green
# 3 - Red
# 4 - Flashing Red
# 5 - Orange
# 6 - Flashing Orange


#ON/OFF LAYER BUTTONS
if keyword == 'ctrl_layer_hidden':
	for i in layerMute:
		if layer == i-63:
			if param == True:
				modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', i, 0)
			else:
				modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', i, 4)
 
#VIDEO BUTTONS (broken)
if keyword == 'ctrl_layer_media':
	for idx, i in enumerate(media):
		if param == idx+(currentPage-56)*16:
			modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', i, 1)
		else:
			modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', i, 3)
			
#TWO WAY PAGE LEDS
if keyword == 'ctrl_layer_mediaSet':
	currentPage = param + 56
	for i in page:
		if i == currentPage:
			modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', i, 4)
		else:
			modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', i, 1)
	
#TWO WAY SPECIAL MEDIA BUTTON
if keyword == 'ctrl_layer_mediaSet':
	if param == 8:
		modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 55, 6)
	else:
		modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 55, 5)
		
#TWO WAY FX BUTTONS
if keyword == 'ctrl_layer_auto_moveOn':
	if param == True:
		modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', fx[0], 4)
	else:
		modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', fx[0], 5)
		
if keyword == 'ctrl_layer_auto_scaleOn':
	if param == True:
		modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', fx[1], 4)
	else:
		modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', fx[1], 5)

if keyword == 'ctrl_layer_auto_colorOn':
	if param == True:
		modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', fx[2], 4)
	else:
		modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', fx[2], 5)
		
if keyword == 'ctrl_layer_auto_rotateOn':
	if param == True:
		modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', fx[3], 4)
	else:
		modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', fx[3], 5)
		
if keyword == 'ctrl_layer_transformer_on':
	if param == True:
		modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', fx[4], 4)
	else:
		modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', fx[4], 5)

if keyword == 'ctrl_layer_pixelFX_saturationOn':
	if param == True:
		modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', fx[7], 4)
	else:
		modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', fx[7], 5)

if keyword == 'ctrl_layer_pixelFX_lightnessOn':
	if param == True:
		modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', fx[8], 4)
	else:
		modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', fx[8], 5)

if keyword == 'ctrl_layer_pixelFX_contrastOn':
	if param == True:
		modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', fx[9], 4)
	else:
		modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', fx[9], 5)

if keyword == 'ctrl_layer_pixelFX_lumaOn':
	if param == True:
		modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', fx[10], 4)
	else:
		modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', fx[10], 5)
		
if keyword == 'ctrl_layer_pixelFX_noiseOn':
	if param == True:
		modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', fx[11], 4)
	else:
		modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', fx[11], 5)
		
if keyword == 'ctrl_layer_pixelFX_blurOn':
	if param == True:
		modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', fx[12], 4)
	else:
		modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', fx[12], 5)												
