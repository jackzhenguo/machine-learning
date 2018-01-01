
# coding: utf-8

from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import matplotlib.pyplot as plt

class mnistData():
    def __init__(self):  
        self.__trainimg= None  
        self.__trainlabel=None
        self.__testimg=None
        self.__testlabel=None
        
    def __getData(self,filepath):
        print ("Download and Extract MNIST dataset")
        mnist = input_data.read_data_sets(filepath, one_hot=True)
        print (" tpye of 'mnist' is %s" % (type(mnist)))
        print (" number of trian data is %d" % (mnist.train.num_examples))
        print (" number of test data is %d" % (mnist.test.num_examples))

        print ("What does the data of MNIST look like?")
        self.__trainimg   = mnist.train.images
        self.__trainlabel = mnist.train.labels
        self.__testimg    = mnist.test.images
        self.__testlabel  = mnist.test.labels
        print (" type of 'trainimg' is %s"    % (type(self.__trainimg)))
        print (" type of 'trainlabel' is %s"  % (type(self.__trainlabel)))
        print (" type of 'testimg' is %s"     % (type(self.__testimg)))
        print (" type of 'testlabel' is %s"   % (type(self.__testlabel)))
        print (" shape of 'trainimg' is %s"   % (self.__trainimg.shape,))
        print (" shape of 'trainlabel' is %s" % (self.__trainlabel.shape,))
        print (" shape of 'testimg' is %s"    % (self.__testimg.shape,))
        print (" shape of 'testlabel' is %s"  % (self.__testlabel.shape,))


    def loadData(self,filepath='./mnist-dataset'):
        '''
        return:
            training_data: tuple([50000,784] , [50000,10])
            test_data : tuple([10000,784], [10000,10])
        '''
        self.__getData(filepath)
        tr_d = (self.__trainimg,self.__trainlabel)
        te_d = (self.__testimg,self.__testlabel)
        training_inputs = [np.reshape(x, (784, 1)) for x in tr_d[0]]
        training_results = [self.__vectorizedResult(y) for y in tr_d[1].astype(int)]
        training_data = zip(training_inputs, training_results)
        test_inputs = [np.reshape(x, (784, 1)) for x in te_d[0]]
        test_data = zip(test_inputs, te_d[1])
        return (training_data, test_data)

    def __vectorizedResult(self,j):
        """
        return:
            10维向量，jth:1,其他位置都为0
        """
        e = np.zeros((10, 1))
        e[j] = 1.0
        return e
    

    def showImg(self,nsample=3):
        '''
        description: randomly show nsample images from dataset
        '''
        nsample = 3
        randind = np.random.randint(self.__trainimg.shape[0], size=nsample)
        for i in randind:
            curr_img   = np.reshape(self.__trainimg[i, :], (28, 28)) # 28 by 28 matrix 
            curr_label = np.argmax(self.__trainlabel[i, :] ) # Label
            plt.matshow(curr_img, cmap=plt.get_cmap('gray'))
            plt.show()
