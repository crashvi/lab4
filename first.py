#AM вношу изменеения в первую строчку кода
from numpy import *
from matplotlib.pyplot import *
from pylab import *
t = arange(-2 * pi, 2 * pi, 0.06)

u=15			#амплетуда исходного сигнала
w=7				#частота исходного сигнала
fi=pi/2			#фаза исходного сигнала
s=str(fi)

u0=45			#амплетуда несущего сигнала
w0=21			#частота несущего сигнала
fi0=pi/5		#фаза несущего сигнала
s0=str(fi0)

m=1				#коэфицент модуляции от 0 до 1
kam=m*u0/u		#коэфицент амплетудной модуляции

bt = u*sin(w*t+fi)								#исходный сигнал

ft = u0*cos(w0*t+fi0)							#несущий сигнал	

uam = (u0+kam*bt)*cos(w0*t+fi0)					#итоговый сигнал

rcParams['figure.figsize'] = 17, 3
rcParams.update({'figure.autolayout': True})
rcParams['lines.linewidth'] = 1
subplot(1, 3, 1)
plot(t, bt, '-', label=r'$usin(wt+fi)$')
legend(loc='upper right')
title('исходный сигнал '+'u='+str(u)+' w='+str(w)+' fi='+s[0:4])
subplot(1, 3, 2)
plot(t, ft, '-', label=r'$u0cos(w0t+fi0)$')
legend(loc='upper right')
title('несущий сигнал '+'u0='+str(u0)+' w0='+str(w0)+' fi0='+s0[0:4])
subplot(1, 3, 3)
plot(t,uam, '-', label=r'$uam=(u0+kamb(t))cos(w0t+fi0)$')
legend(loc='upper right')
title('Итоговый сигнал'+' kam='+str(kam)[0:4])
savefig('AM-1-2.png')
show()
