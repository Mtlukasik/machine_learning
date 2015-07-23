import numpy as np
import matplotlib.pyplot as plt
#funkcja zwracajaca 2 parametry prostej
def gradien(x,y,alpha,m,theta0,theta1):
	
	theta0-=round((float(alpha)/m)*sum(theta0+theta1*x-y),5)
	theta1-=round((float(alpha)/m)*sum((theta0+theta1*x-y)*x),5)
	wspolczynniki=[theta0,theta1]
	return wspolczynniki
	
	
#funkcja wykonuje krotnosc powtorzen gradient_	
def petla(x,y,alpha,m,theta0,theta1,krotnosc):
	i=0
	while i<krotnosc:
		i+=1
		[theta0,theta1]=gradien(x,y,alpha,m,theta0,theta1)
	return [theta0,theta1]
#przetwarza dane podaje argumenty startowe do gradient_descent 
#bierze odpowiedz rysuje i prosta i punkty dane
def rysuj(data):
	x=data[:,0]
	y=data[:,1]
	m= len(y)
	hipoteza=petla(x,y,0.01,m,3,5,10000)
	a=np.linspace(0,max(max(x),max(y))+5)
	b=hipoteza[0] +hipoteza[1]*a
	
	plt.plot(x, y, 'ro')
	plt.plot(a,b,'b')
	plt.axis([0, max(x)+5, -5, max(y)+5])
	plt.show()

#wczytuje dane z txt i wywoluje funkcje rysuj
def main():
	data = np.loadtxt('ex1data1.txt',delimiter=',')
	rysuj(data)
main()
#po 10k -3.89 ,1.19