import numpy as np
import math
from scipy import misc
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def boundshr(I):
	(m,n)=I.shape
	return I[1:m-1,1:n-1].copy()

def showImg(img):
	plt.imshow(img,cmap=cm.gray)
	plt.show()   
    
def boundex(X):
	pass
def nor1(X):
	'''Normalize an image'''
	#if X.dtype == np.dtype('uint8'):
		#return X
	if X.max()<= pow(10,-6):
		print("All points are black,fail.")
		return None
	Y=np.double(X) / float(X.max()) * 255.0
	return Y
	
def region_gorw(I,position):
	'''
	Region Growing Algorithm
	I : input image
	position: selected seed position
	'''
	assert len(I.shape) == 2
	Itermax=5000000
	threshold=60#%������ֵ��1~255֮�������
	flag=1#%have taken the pixel?
	I=nor1(I)
	I1 = np.zeros(I.shape)
	#showImg(I1)
	xp,yp = 0,0
	if flag:
				#Change the pos because we use diff coordinate system
		xp = round(position[1])
		yp = round(position[0])
		flag = 0
		
	seedrec=[xp,yp]
	seed = I[xp,yp]
	seedsum=seed
	seednum=1
	go=np.array([[-1,0],[0,-1],[1,0],[0,1]])#%directer
	#region growing
	# |0  not scaned yet
	# |1  scaned and accepted
	# |2  grown seed
	# global seed I1 I seedsum seednum xp1 yp1 seedrec
	Iter=0
	while seedrec:
		if Iter>Itermax:
			break
		xp=seedrec[0]
		yp=seedrec[1]
		del seedrec[0]
		del seedrec[0]
		I1[xp,yp]=2
		for i in range(4):
			xp1=xp+go[i,0]
			yp1=yp+go[i,1]
			if I1[xp1,yp1]==0:
				b=I[xp1,yp1]
				t = abs(seed-b)
				if t<=threshold:
					I1[xp1,yp1]=1
					seedsum=float(seedsum+I[xp1,yp1])
					seednum=seednum+1
					seedrec.append(xp1)
					seedrec.append(yp1)
		seed = float(seedsum / seednum)
		Iter += 1
		
	I1=boundshr(I1)
	I=boundshr(I)
	I1=nor1(I1)
	#xm,ym,nm=0,0,0
	#for i in range(m):
		#for j in range(n):
			#if I1[i,j]>0:
				#xm+=i
				#ym+=j
				#nm+=1
	II = np.round((I1/255.0)*I)
	II.astype('uint8')
	return II
	#showImg(II)
	

if __name__ == "__main__":
	SELECTEDPOINT= (139,149)
	img = misc.imread('3.bmp')
	if not len(img.shape) == 2:
		img= img[:,:,0] if img.shape[2] > 1 else img
	region_gorw(img,SELECTEDPOINT)
		
	