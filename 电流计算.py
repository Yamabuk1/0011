from typing import Text
import PySimpleGUI as sg

def R_parallel(a=1,b=1):
    """电阻的并联"""
    return (a*b)/(a+b)
def R_sum(a=1,b=1,c=1,d=1):
    """总电阻"""
    return R_parallel(R_parallel(a,b)+c,d)
def I_sum(V=0,R1=1,R2=1,R3=1,R4=1,image = 1):
    """总电流"""
    if image == 1 :
        return V/R_sum(R1,R3,R2,R4)
    else :
        return V/R_sum(R2,R4,R1,R3) 
img = 1

sg.theme('LightBlue3')

layout = [[sg.Text('请点击图片，选择电路结构:',size=(40,1))],
          [sg.Button(image_source=r'C:\Users\86183\Desktop\img1.png',button_text ='1'),sg.Button(image_source=r'C:\Users\86183\Desktop\img2.png',button_text ='2')],
          [sg.T('电压V(伏特):'),sg.In(key='V',s=6)],
          [sg.T('电阻R1(欧姆):'),sg.In(key='R1',s=5),sg.T(size=(5,1)),sg.T('电阻R2(欧姆):'),sg.In(key='R2',s=5)],
          [sg.T('电阻R3(欧姆):'),sg.In(key='R3',s=5),sg.T(size=(5,1)),sg.T('电阻R4(欧姆):'),sg.In(key='R4',s=5)],
          [sg.Button('计算')],
          [sg.Text('干路的电流(安培)为：'), sg.Text(size=(15,1), key='I')]]

window = sg.Window('电流计算', layout)

while True: 
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == '1' :
        img = 1
    if event == '2' :
        img = 2
    if event == '计算' :
        window['I'].update('%.3f' % I_sum(float(values['V']),float(values['R1']),float(values['R2']),float(values['R3']),float(values['R4']),img))

window.close()