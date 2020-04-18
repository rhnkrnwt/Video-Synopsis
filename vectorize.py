#SGItoNPMatrix

import os
import sys
import numpy as np
import pickle as pk
from PIL import Image as IM


folder = sys.argv[1]
images = []
for file in os.listdir(folder):
	image = np.zeros((352,288,3), dtype=np.uint8)
	bnum = 0
	with open(folder+file, 'rb') as f:
		byte = int.from_bytes(f.read(1), "big")
		pnum,r,c = 0,0,0
		while r < 352:
			image[r,c,2] = byte
			byte = int.from_bytes(f.read(1), "big")
			image[r,c,1] = byte
			byte = int.from_bytes(f.read(1), "big")
			image[r,c,0] = byte
			byte = int.from_bytes(f.read(1), "big")
			pnum+=1
			c+=1
			if pnum==288:
				pnum = 0
				r += 1
				c = 0


	images.append(image)
	break

img = IM.fromarray(images[-1], 'RGB')
img.show()
	

