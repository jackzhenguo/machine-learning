
# coding: utf-8

# In[ ]:

""""
模块实现SGD学习算法，对于前向神经网络,
梯度通过后向传播计算得出
"""
import random
import numpy as np

class Network(object):

    def __init__(self, sizes):
        """
        参数，sizes : 神经网络的结构尺寸，是tuple，比如(3,2,1),
        输入层为3个神经元，
        中间层为2个神经元，
        输出层为1个神经元
        类内全局：sizes
        biases：隐含层，输出层的偏置量
        weights：各个神经元的权重参数，[[15 by 784],[10 by 15]]
        """
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]
        
    def feedforward(self, a):
        """
        a 是输入
        返回神经网络的输出： sigmoid(w*a + b)
        """
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a)+b)
        return a

    def SGD(self, training_data, epochs, mini_batch_size, eta,
            test_data=None):      
        """
        采用 mini-batch SGD 训练神经网络
        training_data : [(x,y)]，x 代表训练的输入， y 代表输出
        epochs：比如，迭代100次为一波
        mini_batch_size：批梯度下降，一次迭代，采用的样本个数，比如为10个样本
        eta : 学习率
        """
        if test_data: 
            n_test = len(list(test_data))
        n = len(list(training_data))
        for j in range(epochs):
            random.shuffle(list(training_data))
            mini_batches = [
                (list(training_data))[k:k+mini_batch_size]
                for k in range(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
            if test_data:
                print ("Epoch {0}: {1} / {2}".format(
                    j, self.evaluate(test_data), n_test))
            else:
                print ("Epoch {0} complete".format(j))

    def update_mini_batch(self, mini_batch, eta):
        """
        更新神经网络的权重（类内全局参数weights）和偏置量（类内全局参数：biases），
        使用后传播的梯度下降方法，这个方法的核心是后传播算法backprop
        mini_batch：[(x,y)]，x是输入，y是输出
        """ 
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.weights = [w-(eta/len(mini_batch))*nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb
                       for b, nb in zip(self.biases, nabla_b)]

    def backprop(self, x, y):
        """
        通过后向传播得出偏置量和权重参数的梯度方向，
        返回值 ，biases：每层的偏置量的梯度
        weights：每层神经元的权重参数
        """
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # 前向传播
        activation = x
        activations = [x] # 分层存储每层的激活节点
        zs = [] # 分层存储每层的 Z 向量
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
        # 后传播
        delta = self.cost_derivative(activations[-1], y) * sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())

        # L = 1 表示最后一层神经元， L = 2 倒数第二层神经元
        for layer in range(2, self.num_layers):
            z = zs[-layer]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-layer+1].transpose(), delta) * sp
            nabla_b[-layer] = delta
            nabla_w[-layer] = np.dot(delta, activations[-layer-1].transpose())
        return (nabla_b, nabla_w)

    def evaluate(self, test_data):
        """
        输出层中，输出值最大的神经元对应的索引为分类，比如神经元5的激活值
        最大，则认为输入的图像为5 
        """
        
        test_results = [(np.argmax(self.feedforward(x)), y)
                        for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)

    def cost_derivative(self, output_activations, y):
        """
        成本函数的导数
        """ 
        return (output_activations-y)
    
    def sigmoid(z):
        """The sigmoid 函数."""
        return 1.0/(1.0+np.exp(-z))

    def sigmoid_prime(z):
        """sigmoid 函数的导数"""
        return sigmoid(z)*(1-sigmoid(z))

