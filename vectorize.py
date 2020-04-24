#SGItoNPMatrix

import os
import sys
import numpy as np
import pickle as pk
from tqdm import tqdm
from math import floor
from PIL import Image as IM

W, H = 352, 288
loffolder = ['data/video_1/', 'data/video_2/','data/video_3/', 'data/video_4/']

for folder in loffolder:
	print("Parsing", folder)
	images = []
	for file in tqdm(sorted(os.listdir(folder))):
		with open(folder+file, 'rb') as f:
			byte = f.read()
		bl,gr,re = [],[],[]
		image = np.zeros((H,W,3))
		for i, b in enumerate(byte):
			if i<W*H:
				re.append(b)
			elif i>=W*H and i<W*H*2:
				gr.append(b)
			else:
				bl.append(b)
			pass
		image[:,:,0] = np.array(re).reshape((H,W))
		image[:,:,1] = np.array(gr).reshape((H,W))
		image[:,:,2] = np.array(bl).reshape((H,W))
		image = image.astype(np.uint8)
		images.append(image)
	

	#out = open(folder[:-1]+'_parsed.pkl', 'wb')
	#pk.dump(images, out)
	#out.close()

print("Done!")


	

