
def nor1(X):
	'''Normalize an image'''
	
def region_gorw(I):
	'''X is input gray image,use region growing algorithm'''
	Itermax=5000000
	thr=60#%������ֵ��1~255֮�������
	flag=1#%have taken the pixel?
	I=nor1(I)
	I1=boundex(I)
	