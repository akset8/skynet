This project aims at measuring visual similarity based on Deep Learning and Perceptual Hashing.

Features of InceptionNet at POOL3 layer are taken for two images and L2 norm is computed.Also used is Hamming Distance between the perceptual Hashes of two images.The net output is a weighted average of the two.

To run:

1.Install all the dependencies listed in requirements.txt

2.Install the preatrained model

3.run app.py

4.Application running at 0.0.0.0:80

PS:might need sudo priviledges

References: 

DeCAF: A deep convolutional activation feature for generic visual recognition

Phash functions : perceptual hashing in images 

