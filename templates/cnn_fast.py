from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from PIL import Image
import imagehash , numpy 
from scipy import spatial

import os.path
import re
import sys
import tarfile

import numpy as np
from six.moves import urllib
import tensorflow as tf



def make_patches(image1 ,image2):

    im1 = Image.open(image1)
    im1 = im1.resize((200, 200), Image.ANTIALIAS)
    im1.save(image1)

    im2 = Image.open(image2)
    im2 = im2.resize((200, 200), Image.ANTIALIAS)
    im2.save(image2)

    pix1 = numpy.asarray(im1)
    pix2 = numpy.asarray(im2)

    i=0
    while(i+150<=200):
        j=0
        while(j+150<=200):
            im_temp = Image.fromarray(pix1[i:i+150][j:j+150])
            im_temp.save(image1[:-3]+"_"+str(i)+"_"+str(j)+".jpg")

            j=j+50

        i=i+50

    i=0
    while(i+150<=200):
        j=0
        while(j+150<=200):
            im_temp = Image.fromarray(pix2[i:i+150][j:j+150])
            im_temp.save(image2[:-3]+"_"+str(i)+"_"+str(j)+".jpg")

            j=j+50

        i=i+50



def similarity1(image1 , image2):
    
    image_data1 = tf.gfile.FastGFile(image1, 'rb').read()
    image_data2 = tf.gfile.FastGFile(image2 ,'rb').read()



    with open('/tmp/imagenet/classify_image_graph_def.pb', 'rb') as graph_file:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(graph_file.read())
        tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        pool_3_tensor = sess.graph.get_tensor_by_name('pool_3:0')

        feat1 = sess.run(pool_3_tensor,{'DecodeJpeg/contents:0': image_data1})  
        feat1 = np.squeeze(feat1)

        feat2 = sess.run(pool_3_tensor,{'DecodeJpeg/contents:0': image_data2})  
        feat2 = np.squeeze(feat2)

        
        return (numpy.sum(numpy.square(feat2 - feat1)))

def similarity2(image1 , image2):
    hash1 = imagehash.phash(Image.open(image1))
    hash2 = imagehash.phash(Image.open(image2))
    diff1 = abs(hash1 - hash2)

    #print (diff1)

    if(diff1<=12):
        return (1 -  (float(diff1)/64))

    return 0



#main 

def eval1(image1 , image2):

    

    make_patches(image1 , image2)

    l=0

    arr= []

    arr.append(similarity1(image1,image2))

    c = similarity2(image1,image2)

    d = min(arr)


    #a non linear ranking function 

    if(c==0):
        return (1-(float(d)/500))

    else:
        if(c>0.95):
            return(c)

        elif(d > 0.95):
            return(d)

        else:
            e = ((c + (1-(float(d)/500)))/2)

            return e













