 a=[0,0,0,1];             %���庯������
 b=[1,50,500,50000];
 t=0:0.01:2;

 s=tf(a,b);               %����ϵͳ
 subplot(1,3,1), step(s,t);     %���ƽ�Ծ��Ӧ����
 grid on
 title('��λ��Ծ��Ӧ');

 subplot(1,3,2), impulse(s,t);    %���Ƴ弤��Ӧ����
 grid on
 title('��λ�弤��Ӧ');

 t=0:0.1:50;
 subplot(1,3,3), c=step(a,b,t);    %����б����Ӧ����
 plot(t,c,'ro',t,t,'b-')
 grid on
 title('��λб����Ӧ');
