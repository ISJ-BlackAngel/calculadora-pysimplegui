# bot_get_information_interweb.py
import os
try:
	import PySimpleGUI as sg
except:
	os.system('pip install pysimplegui')
	import PySimpleGUI as sg

font = ('courier new', 16)
layout = [
	[sg.Push(), sg.Text('Calculadora', font=font), sg.Push()],
	[sg.Push(), sg.Input(key='-input-', font=font, size=[11, 1]), sg.Button('del', key='del', font=font)],
	[sg.Push()]+[sg.Button(f'{x}', font=font, key=f'{x}') for x in [1, 2, 3]]+[sg.Push(), sg.Button('-', font=font, key='-')],
	[sg.Push()]+[sg.Button(f'{x}', font=font, key=f'{x}') for x in [4, 5, 6]]+[sg.Push(), sg.Button('/', font=font, key='/')],
	[sg.Push()]+[sg.Button(f'{x}', font=font, key=f'{x}') for x in [7, 8, 9]]+[sg.Push(), sg.Button('+', font=font, key='+')],
	[sg.Push(), sg.Button(f'0', font=font, key=f'0'), sg.Push(), sg.Button('*', font=font, key='*')],
	[sg.Push(), sg.Push(), sg.Push(), sg.Button('=', font=font, key='=')],
]
window = sg.Window('Calculadora', layout, finalize=True)
window.bind('<Return>', '=')
def tratamente(string:str):
	try:
		result_expre = eval(string)
		window['-input-'].update(result_expre)
	except:	sg.popup('Calculo não valido!!')


while(True):
	event, values = window.read(0)
	if (event == sg.WIN_CLOSED):
		break
	if (len(values['-input-']) > 0):
		if (not values['-input-'][-1] in '1234567890-=/*+') or (event == 'del'):
			window['-input-'].update(values['-input-'][:-1])
	if (event == '='):
		tratamente(values['-input-'])
	elif (event in '1234567890-/+*'):
		window['-input-'].update(values['-input-']+event)
window.close()
