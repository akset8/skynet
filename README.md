SKYNET
============

This project aims at measuring visual similarity based on Deep Learning and Perceptual Hashing.
-------------------------------------------------------------------------------------------------------------
About:
-------
Uses two techniques :

1.Using a InceptionNet V3 by google.To find similarity in images we need to some how extract features like SIFT , HOG , gabor filters etc in images but recent advances in deep learning have shown that deep nets are able to extract better features from the images.

I have computed a feature set just before the final softmax layer in the inception net (called the pool-3 layer).For the given two images have computed the L2 norm of the images(the eucliedian distance between the respective feature set computed.)

2.Now the above approach captures things like translation between two images, occulsion and different perspectives whereas the original problem statement said that the images could also be cropped , scaled etc for that i have used a deterministic hashing technique called
perceptual hashing which assigns a hash-value to the image.

Perceptual hashing hash the advantage the if the images are scaled and cropped within limits its hash value would be the same.The hamming distance between the hashvalues of the two images is computed and a score is assigned based on that to the pair of images.

Furthermore,The similarity score is a weighted average of both the values.

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

