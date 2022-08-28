import PySimpleGUI as sg                #用来编写界面的库
import webbrowser                       # 用来打开网站的库
from URL_title import return_dict       #这是从爬虫返回网址和标题的函数

university = 0                          #确定选哪个大学

sg.theme('Reddit')                      #界面的颜色

layout = [[sg.Text('                                 请选择大学：',size = (40,2),border_width=3)],                  #一行文本
          [sg.Button(key = 0 ,image_source=r'C:\Users\86183\Desktop\清华大学.png',image_subsample=3 ),sg.Button(key = 1 ,image_source=r'C:\Users\86183\Desktop\北京大学.png',image_subsample=3)],
          [sg.Button(key = 2 ,image_source=r'C:\Users\86183\Desktop\浙江大学.png',image_subsample=3 ),sg.Button(key = 3 ,image_source=r'C:\Users\86183\Desktop\复旦大学.png',image_subsample=3)],
          #四张校徽（按钮）
          [sg.Text(size=(15,1))]]                              #空行
          #第一个窗口的内容
win1 = sg.Window('选择窗口', layout)                            #定义第一个窗口
win2_active=False                                              #标志第二个窗口是否出现
while True:
    ev1, vals1 = win1.read(timeout=100)                        #读取按钮等事件
    if ev1 == sg.WIN_CLOSED:            
        break
    #点击叉号时关闭
    if ev1 == 0 :   university =0
    if ev1 == 1 :   university =1
    if ev1 == 2 :   university =2
    if ev1 == 3 :   university =3
    #标志学校    
    if (ev1 == 0 or ev1 == 1 or ev1 == 2 or ev1 == 3 )  and not win2_active:
        win2_active = True
        win1.Hide()
        layout2 = [[sg.Listbox(key='List',values=list(return_dict(university)), size=(60, 30),enable_events=True,select_mode='single')],
                   [sg.Button('返回')]]
        #第二个窗口的内容
        win2 = sg.Window('信息窗口', layout2 , finalize = True )
        #定义第二个窗口

        while True:
            ev2, vals2 = win2.read()
            if ev2 == sg.WIN_CLOSED or ev2 == '返回':
                win2.close()
                win2_active = False
                win1.UnHide()
                break
            #关闭第二个窗口时，打开第一个窗口
            if ev2 == 'List':
                webbrowser.open(return_dict(university)[str(win2['List'].get())[2:-2]])
            #点击第二个窗口时打开相应的网站
