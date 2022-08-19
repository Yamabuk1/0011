import PySimpleGUI as sg    

tab1_layout =  [[sg.Text('半径')]+[sg.Input(key='radius')],
                [sg.Button('计算圆的面积')]]    

tab2_layout = [[sg.Text('长')]+[sg.In(key='length')],
          [sg.Text('宽')]+[sg.Input(key='width')],
          [sg.Button('计算长方形的面积')]]   

tab3_layout = [[sg.Text('底')]+[sg.In(key='base')],
          [sg.Text('高')]+[sg.Input(key='height')],
          [sg.Button('计算三角形的面积')]]   

layout = [[sg.TabGroup([[sg.Tab('圆', tab1_layout, tooltip='tip'), sg.Tab('长方形', tab2_layout),sg.Tab('三角形', tab3_layout)]], tooltip='TIP2')],    
          [sg.Text('图形的面积为：'), sg.Text(size=(15,1), key='area')]]    

window = sg.Window('My window with tabs', layout, default_element_size=(12,1))    

while True:    
    event, values = window.read()    
    print(event,values)    
    if event == sg.WIN_CLOSED:           # always,  always give a way out!    
        break  
    if event == '计算圆的面积':
        area = 3.14159 * float(values['radius']) * float(values['radius'])
        window['area'].update('%.3f' % area)
    if event == '计算长方形的面积':
        area = float(values['length']) * float(values['width'])
        window['area'].update('%.3f' % area)
    if event == '计算三角形的面积':
        area = 0.5*float(values['base']) * float(values['height'])
        window['area'].update('%.3f' % area)

