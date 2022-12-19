import cv2
import os

#initialisation of the variable
path ="./" # path to use beacause the py file is in the same folder of the other folder
folder = [] #list of all the folder to change the picture format

for root, dirs, files in os.walk(path): #get all the files and the directory of the path
	for aa in dirs: #go throught all the folder next have
		folder.append(os.path.join(root,aa)) #append all the folder name in the folder tab


#create all the resize photos for all the folders
for i in range(len(folder)):	
	"""
		bloc to resize all the image with a resolution of 1242*2688
	"""
	os.mkdir(folder[i] + '/12422688')
	for j in range(1, 8):
		src = cv2.imread(folder[i] + '/' + str(j) + '.png', cv2.IMREAD_UNCHANGED)
		print(folder[i] + '/' + str(j) + '.png')
		dsize = (1242, 2688)
		output = cv2.resize(src, dsize)
		cv2.imwrite(folder[i] + '/12422688/' + str(j) + '.png',output)
	"""
		bloc to resize all the image with a resolution of 1242*2208
	"""
	os.mkdir(folder[i] + '/12422208')
	for j in range(1, 8):
		src = cv2.imread(folder[i] + '/' + str(j) + '.png', cv2.IMREAD_UNCHANGED)
		print(folder[i] + '/' + str(j) + '.png')
		dsize = (1242, 2208)
		output = cv2.resize(src, dsize)
		cv2.imwrite(folder[i] + '/12422208/' + str(j) + '.png',output)
	"""
		bloc to resize all the image with a resolution of 2048*2732 for apple 12.9inch apple tablette and big phone
	"""
	os.mkdir(folder[i] + '/20482732')
	for j in range(1, 8):
		src = cv2.imread(folder[i] + '/' + str(j) + '.png', cv2.IMREAD_UNCHANGED)
		print(folder[i] + '/' + str(j) + '.png')
		dsize = (2732, 2048)
		output = cv2.resize(src, dsize)
		cv2.imwrite(folder[i] + '/20482732/' + str(j) + '.png',output)