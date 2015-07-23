

import numpy as np

import matplotlib.pyplot as plt

	

def normal_equ(x,y):
	#maciez na poczet X
	a=np.ones((len(x),1))
	a=np.matrix(a)
	x=np.matrix(x).transpose()
	X=np.hstack((a,x))
	tr=X.transpose()
	y=np.matrix(y).transpose()
	return np.linalg.inv(tr*X)*tr*y
def rysuj(data):
	x=data[:,0]
	y=data[:,1]
	hipoteza=normal_equ(x,y)
	print hipoteza
	a=np.linspace(0,30)
	b=int(hipoteza[0]) +int(hipoteza[1])*a
	
	plt.plot(x, y, 'ro')
	plt.plot(a,b,'b')
	plt.axis([0, 30, -5, 30])
	plt.show()

def main():
	data = np.loadtxt('ex1data1.txt',delimiter=',')
	rysuj(data)
main()