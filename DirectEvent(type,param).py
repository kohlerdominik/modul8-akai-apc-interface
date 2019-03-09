#Light Color Values
# 0 - Off
# 1 - Green
# 2 - Flashing Green
# 3 - Red
# 4 - Flashing Red
# 5 - Orange
# 6 - Flashing Orange

#Sets current page selected
if type == 'MIDI' :
	if param['source'] == 'APC MINI - APC MINI':
		if param['channel'] == 1:
			if param['message'] == 'NOTE_ON':
				if param['param1'] > 54 and param['param1']  < 64:
					currentPage = param['param1']

#Control Mapping

#PAGE SELECT
if type == 'MIDI':
	if param['channel'] == 1:
		if param['message'] == 'NOTE_ON':
			for i in page:
				if param['param1'] == i:
						modul8.setValue('ctrl_layer_mediaSet', i-56, 0)						

#SPECIAL MEDIA PAGE SELECT
if type == 'MIDI':
	if param['channel'] == 1:
		if param['message'] == 'NOTE_ON':
				if param['param1'] == 55:
						modul8.setValue('ctrl_layer_mediaSet', 8, 0)

#LAYER ON/OFF
if type == 'MIDI':
	if param['channel'] == 1:
		if param['message'] == 'NOTE_ON':
			for i in layerMute:
				if param['param1'] == i:
					if modul8.getValue('ctrl_layer_hidden', i-63) == False:
						modul8.setValue('ctrl_layer_hidden', True, i-63)
					else:
						modul8.setValue('ctrl_layer_hidden', False, i-63)
						
#FX ON / OFF
if type == 'MIDI':
	if param['channel'] == 1:
		if param['message'] == 'NOTE_ON':
			#AUTO MOVE
			if param['param1'] == fx[0]:
				if modul8.getValue('ctrl_layer_auto_moveOn', 0) == False:
					modul8.setValue('ctrl_layer_auto_moveOn', True, 0)
				else:
					modul8.setValue('ctrl_layer_auto_moveOn', False, 0)
			#AUTO SCALE
			if param['param1'] == fx[1]:
				if modul8.getValue('ctrl_layer_auto_scaleOn', 0) == False:
					modul8.setValue('ctrl_layer_auto_scaleOn', True, 0)
				else:
					modul8.setValue('ctrl_layer_auto_scaleOn', False, 0)
			#AUTO COLOR
			if param['param1'] == fx[2]:
				if modul8.getValue('ctrl_layer_auto_colorOn', 0) == False:
					modul8.setValue('ctrl_layer_auto_colorOn', True, 0)
				else:
					modul8.setValue('ctrl_layer_auto_colorOn', False, 0)
			#AUTO ROTATE
			if param['param1'] == fx[3]:
				if modul8.getValue('ctrl_layer_auto_rotateOn', 0) == False:
					modul8.setValue('ctrl_layer_auto_rotateOn', True, 0)
				else:
					modul8.setValue('ctrl_layer_auto_rotateOn', False, 0)
			#TRANSFORMER
			if param['param1'] == fx[4]:
				if modul8.getValue('ctrl_layer_transformer_on', 0) == False:
					modul8.setValue('ctrl_layer_transformer_on', True, 0)
				else:
					modul8.setValue('ctrl_layer_transformer_on', False, 0)
			#SATURATION
			if param['param1'] == fx[7]:
				if modul8.getValue('ctrl_layer_pixelFX_saturationOn', 0) == False:
					modul8.setValue('ctrl_layer_pixelFX_saturationOn', True, 0)
				else:
					modul8.setValue('ctrl_layer_pixelFX_saturationOn', False, 0)

                            #LIGHTNESS
			if param['param1'] == fx[8]:
				if modul8.getValue('ctrl_layer_pixelFX_lightnessOn', 0) == False:
					modul8.setValue('ctrl_layer_pixelFX_lightnessOn', True, 0)
				else:
					modul8.setValue('ctrl_layer_pixelFX_lightnessOn', False, 0)

                            #CONTRAST
			if param['param1'] == fx[9]:
				if modul8.getValue('ctrl_layer_pixelFX_contrastOn', 0) == False:
					modul8.setValue('ctrl_layer_pixelFX_contrastOn', True, 0)
				else:
					modul8.setValue('ctrl_layer_pixelFX_contrastOn', False, 0)

                            #LUMA KEY
			if param['param1'] == fx[10]:
				if modul8.getValue('ctrl_layer_pixelFX_lumaOn', 0) == False:
					modul8.setValue('ctrl_layer_pixelFX_lumaOn', True, 0)
				else:
					modul8.setValue('ctrl_layer_pixelFX_lumaOn', False, 0)

                            #NOISE
			if param['param1'] == fx[11]:
				if modul8.getValue('ctrl_layer_pixelFX_noiseOn', 0) == False:
					modul8.setValue('ctrl_layer_pixelFX_noiseOn', True, 0)
				else:
					modul8.setValue('ctrl_layer_pixelFX_noiseOn', False, 0)

                            #BLUR
			if param['param1'] == fx[12]:
				if modul8.getValue('ctrl_layer_pixelFX_blurOn', 0) == False:
					modul8.setValue('ctrl_layer_pixelFX_blurOn', True, 0)
				else:
					modul8.setValue('ctrl_layer_pixelFX_blurOn', False, 0)																						
#INVERT COLOR
if type == 'MIDI':
	if param['channel'] == 1:
		if param['message'] == 'NOTE_ON':
				if param['param1'] == 15:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 15, 5)
						modul8.setValue('ctrl_master_invColorR', 1.0, 10)
						modul8.setValue('ctrl_master_invColorG', 1.0, 10)
						modul8.setValue('ctrl_master_invColorB', 1.0, 10)
		if param['message'] == 'NOTE_OFF':
				if param['param1'] == 15:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 15, 3)
						modul8.setValue('ctrl_master_invColorR', 0.0, 10)
						modul8.setValue('ctrl_master_invColorG', 0.0, 10)
						modul8.setValue('ctrl_master_invColorB', 0.0, 10)
						
#FLASH
if type == 'MIDI':
	if param['channel'] == 1:
		if param['message'] == 'NOTE_ON':
				if param['param1'] == 7:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 7, 5)
						modul8.setValue('ctrl_master_addColorR', 1.0, 10)
						modul8.setValue('ctrl_master_addColorG', 1.0, 10)
						modul8.setValue('ctrl_master_addColorB', 1.0, 10)
		if param['message'] == 'NOTE_OFF':
				if param['param1'] == 7:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 7, 3)
						modul8.setValue('ctrl_master_addColorR', 0.0, 10)
						modul8.setValue('ctrl_master_addColorG', 0.0, 10)
						modul8.setValue('ctrl_master_addColorB', 0.0, 10)
#BLUE
if type == 'MIDI':
	if param['channel'] == 1:
		if param['message'] == 'NOTE_ON':
				if param['param1'] == 23:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 23, 5)
						modul8.setValue('ctrl_master_addColorR', 0.0, 10)
						modul8.setValue('ctrl_master_addColorG', 0.0, 10)
						modul8.setValue('ctrl_master_addColorB', 1.0, 10)
		if param['message'] == 'NOTE_OFF':
				if param['param1'] == 23:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 23, 3)
						modul8.setValue('ctrl_master_addColorR', 0.0, 10)
						modul8.setValue('ctrl_master_addColorG', 0.0, 10)
						modul8.setValue('ctrl_master_addColorB', 0.0, 10)
#GREEN
if type == 'MIDI':
	if param['channel'] == 1:
		if param['message'] == 'NOTE_ON':
				if param['param1'] == 31:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 31, 5)
						modul8.setValue('ctrl_master_addColorR', 0.0, 10)
						modul8.setValue('ctrl_master_addColorG', 1.0, 10)
						modul8.setValue('ctrl_master_addColorB', 0.0, 10)
		if param['message'] == 'NOTE_OFF':
				if param['param1'] == 31:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 31, 3)
						modul8.setValue('ctrl_master_addColorR', 0.0, 10)
						modul8.setValue('ctrl_master_addColorG', 0.0, 10)
						modul8.setValue('ctrl_master_addColorB', 0.0, 10)

#RED
if type == 'MIDI':
	if param['channel'] == 1:
		if param['message'] == 'NOTE_ON':
				if param['param1'] == 39:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 39, 5)
						modul8.setValue('ctrl_master_addColorR', 1.0, 10)
						modul8.setValue('ctrl_master_addColorG', 0.0, 10)
						modul8.setValue('ctrl_master_addColorB', 0.0, 10)
		if param['message'] == 'NOTE_OFF':
				if param['param1'] == 39:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 39, 3)
						modul8.setValue('ctrl_master_addColorR', 0.0, 10)
						modul8.setValue('ctrl_master_addColorG', 0.0, 10)
						modul8.setValue('ctrl_master_addColorB', 0.0, 10)
												
#RESET1
if type == 'MIDI':
	if param['channel'] == 1:
		if param['message'] == 'NOTE_ON':
				if param['param1'] == 40:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 40, 5)
						
		if param['message'] == 'NOTE_OFF':
				if param['param1'] == 40:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 40, 1)
						
#RESET2
if type == 'MIDI':
	if param['channel'] == 1:
		if param['message'] == 'NOTE_ON':
				if param['param1'] == 32:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 32, 5)
						
		if param['message'] == 'NOTE_OFF':
				if param['param1'] == 32:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 32, 1)												
						
#RESET3
if type == 'MIDI':
	if param['channel'] == 1:
		if param['message'] == 'NOTE_ON':
				if param['param1'] == 24:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 24, 5)
						
		if param['message'] == 'NOTE_OFF':
				if param['param1'] == 24:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 24, 1)												
						
#RESET4
if type == 'MIDI':
	if param['channel'] == 1:
		if param['message'] == 'NOTE_ON':
				if param['param1'] == 16:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 16, 5)
						
		if param['message'] == 'NOTE_OFF':
				if param['param1'] == 16:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 16, 1)																		
#RESET5
if type == 'MIDI':
	if param['channel'] == 1:
		if param['message'] == 'NOTE_ON':
				if param['param1'] == 41:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 41, 5)
						
		if param['message'] == 'NOTE_OFF':
				if param['param1'] == 41:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 41, 1)


#RESET6
if type == 'MIDI':
	if param['channel'] == 1:
		if param['message'] == 'NOTE_ON':
				if param['param1'] == 33:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 33, 5)
						
		if param['message'] == 'NOTE_OFF':
				if param['param1'] == 33:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 33, 1)


#RESET7
if type == 'MIDI':
	if param['channel'] == 1:
		if param['message'] == 'NOTE_ON':
				if param['param1'] == 25:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 25, 5)
						
		if param['message'] == 'NOTE_OFF':
				if param['param1'] == 25:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 25, 1)


#RESET8
if type == 'MIDI':
	if param['channel'] == 1:
		if param['message'] == 'NOTE_ON':
				if param['param1'] == 17:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 17, 5)
						
		if param['message'] == 'NOTE_OFF':
				if param['param1'] == 17:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 17, 1)

#ON/OFF1
if type == 'MIDI':
	if param['channel'] == 1:
		if param['message'] == 'NOTE_ON':
				if param['param1'] == 48:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 48, 1)
						
		if param['message'] == 'NOTE_OFF':
				if param['param1'] == 48:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 48, 5)

#ON/OFF2
if type == 'MIDI':
	if param['channel'] == 1:
		if param['message'] == 'NOTE_ON':
				if param['param1'] == 49:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 49, 1)
						
		if param['message'] == 'NOTE_OFF':
				if param['param1'] == 49:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 49, 5)
						

#ON/OFF3
if type == 'MIDI':
	if param['channel'] == 1:
		if param['message'] == 'NOTE_ON':
				if param['param1'] == 46:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 46, 3)
						
		if param['message'] == 'NOTE_OFF':
				if param['param1'] == 46:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 46, 1)


#ON/OFF4
if type == 'MIDI':
	if param['channel'] == 1:
		if param['message'] == 'NOTE_ON':
				if param['param1'] == 38:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 38, 3)
						
		if param['message'] == 'NOTE_OFF':
				if param['param1'] == 38:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 38, 1)


#ON/OFF5
if type == 'MIDI':
	if param['channel'] == 1:
		if param['message'] == 'NOTE_ON':
				if param['param1'] == 30:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 30, 3)
						
		if param['message'] == 'NOTE_OFF':
				if param['param1'] == 30:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 30, 1)


#ON/OFF6
if type == 'MIDI':
	if param['channel'] == 1:
		if param['message'] == 'NOTE_ON':
				if param['param1'] == 22:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 22, 3)
						
		if param['message'] == 'NOTE_OFF':
				if param['param1'] == 22:
						modul8.sendMidi('APC MINI - APC MINI', 1, 'NOTE_ON', 22, 1)

#VIDEO SELECT
if type == 'MIDI':
	if param['channel'] == 1:
		if param['message'] == 'NOTE_ON':
			for idx, i in enumerate(media):
				if param['param1'] == i:
						modul8.setValue('ctrl_layer_media', idx+(currentPage-56)*16, 0)

					
# MASTER OPACITY
if type == 'MIDI' :						
	if param['channel'] == 1:
		if param['message'] == 'CONTROL_CHANGE':	
			if param['param1'] == 56:			
				modul8.setValue('ctrl_master_alpha', param['param2']/127.0, 1)
			
#LAYER OPACITY		
if type == 'MIDI' :						
	if param['channel'] == 1:
		if param['message'] == 'CONTROL_CHANGE':
			for i in fader:
				if param['param1'] == i:
					modul8.setValue('ctrl_layer_alpha', param['param2']/127.0, i - 47)

