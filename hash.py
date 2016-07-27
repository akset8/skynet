#hashing done start with conv_net 

from PIL import Image
import imagehash
import math


def similarity(image1 , image2):
	hash1 = imagehash.phash(Image.open(image1))
	hash2 = imagehash.phash(Image.open(image2))
	diff1 = abs(hash1 - hash2)

	if(diff1<=12):
		print (1 -  (float(diff1)/64))



similarity('/Users/akshaysethi/Desktop/images/bel1.jpg','/Users/akshaysethi/Desktop/images/bel2.jpg')












