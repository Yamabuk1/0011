 a=[0,0,0,1];             %定义函数变量
 b=[1,50,500,50000];
 t=0:0.01:2;

 s=tf(a,b);               %定义系统
 subplot(1,3,1), step(s,t);     %绘制阶跃响应曲线
 grid on
 title('单位阶跃响应');

 subplot(1,3,2), impulse(s,t);    %绘制冲激响应曲线
 grid on
 title('单位冲激响应');

 t=0:0.1:50;
 subplot(1,3,3), c=step(a,b,t);    %绘制斜坡响应曲线
 plot(t,c,'ro',t,t,'b-')
 grid on
 title('单位斜坡响应');
