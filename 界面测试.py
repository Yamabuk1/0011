import PySimpleGUI as sg

sg.theme('Reddit')

university = 1

layout = [[sg.Text('                                 请选择大学：',size = (40,2),border_width=3)],
          [sg.Button(key = 1 ,image_source=r'C:\Users\86183\Desktop\清华大学.png',image_subsample=3 ),sg.Button(key = 2 ,image_source=r'C:\Users\86183\Desktop\北京大学.png',image_subsample=3)],
          [sg.Button(key = 3 ,image_source=r'C:\Users\86183\Desktop\浙江大学.png',image_subsample=3 ),sg.Button(key = 4 ,image_source=r'C:\Users\86183\Desktop\复旦大学.png',image_subsample=3)],
          [sg.Text(size=(15,1),  key='-OUTPUT-')]]
          

win1 = sg.Window('选择窗口', layout)
win2_active=False
while True:
    ev1, vals1 = win1.read(timeout=100)
    if ev1 == sg.WIN_CLOSED:
        break
    
    if ev1 == 1 :   university =1
    if ev1 == 2 :   university =2
    if ev1 == 3 :   university =3
    if ev1 == 4 :   university =4

    if (ev1 == 1 or ev1 == 2 or ev1 == 3 or ev1 == 4 )  and not win2_active:
        win2_active = True
        win1.Hide()
        layout2 = [[sg.Text('Window 2')],      
                   [sg.Multiline( key = 'TXT' , size=(80,40))],
                   [sg.Button('返回')]]
        
        win2 = sg.Window('Window 2', layout2 , finalize = True )
        win2['TXT'].print(university,end='', text_color='red', background_color='yellow')
        win2['TXT'].print('\n'+'测试', end='')

        while True:
            ev2, vals2 = win2.read()
            if ev2 == sg.WIN_CLOSED or ev2 == '返回':
                win2.close()
                win2_active = False
                win1.UnHide()
                break