SKYNET
============

This project aims at measuring visual similarity based on Deep Learning and Perceptual Hashing.
-------------------------------------------------------------------------------------------------------------

Features of InceptionNet at POOL3 layer are taken for two images and L2 norm is computed.Also used is Hamming Distance between the perceptual Hashes of two images.The net output is a weighted average of the two.

To run:

1.Install all the dependencies listed in requirements.txt

2.Install the preatrained model

3.run app.py

4.Application running at 0.0.0.0:80

There are two versions cnn.py and cnn_fast.py, by default cnn_fast is used.In cnn version patch wise comparisons are also done hence making it much more time consuming but gives better results.To use that version replace cnn_fast.eval1 call in app.py by cnn.eval1


PS:might need sudo priviledges

References: 
------------------

DeCAF: A deep convolutional activation feature for generic visual recognition

Phash functions : perceptual hashing in images 

