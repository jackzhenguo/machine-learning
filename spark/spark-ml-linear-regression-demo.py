#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 18:06:21 2019

@author: penzhu
"""

from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.ml.regression import LinearRegression
import numpy as np
import pandas as pd


features=[i/100. for i in range(-100,100)]
labels=[2*features[i]+np.random.normal() for i in range(len(features))]
features=np.atleast_2d(np.array(features)).reshape([-1,1])
labels=np.atleast_2d(np.array(labels)).reshape([-1,1])

matrix=np.hstack([features,labels])


fes=pd.DataFrame(data=matrix,columns=["features","labels"])


sc= SparkContext( 'local', 'lineregression')

sqlContext = SQLContext(sc)
 

df = sqlContext.createDataFrame(fes)

df.select(["features","labels"]).toPandas()



from pyspark.ml.feature import VectorAssembler
vectorAssembler = VectorAssembler(inputCols = ['features'], outputCol = 'feature')
vhouse_df = vectorAssembler.transform(df)
vhouse_df = vhouse_df.select(['feature', 'labels'])
vhouse_df.show(3)




lr = LinearRegression(featuresCol = 'feature', labelCol='labels', maxIter=100, regParam=0.3, elasticNetParam=0.8)
lr_model = lr.fit(vhouse_df.randomSplit([0.9,0.1])[0])
print("Coefficients: " + str(lr_model.coefficients))
print("Intercept: " + str(lr_model.intercept))

a=float(str(lr_model.coefficients[0]))
b=float(str(lr_model.intercept))
import matplotlib.pyplot as plt

plt.scatter(matrix[:,0], matrix[:,1])

plt.plot(matrix[:,0],a*matrix[:,0]+b,color='red')


