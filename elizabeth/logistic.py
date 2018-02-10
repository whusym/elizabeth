# Logistic Regression (02.10.2018)
# This is not completed yet. It's still at the loading data stage.

from preprocess import *

import pyspark
from pyspark.ml.classification import LogisticRegression
from pyspark import SparkFiles

def context(**kwargs):
    conf = pyspark.SparkConf()
    conf.setAppName('elizabeth')
    conf.setAll(kwargs.items())
    ctx = pyspark.SparkContext()
    return ctx

# Start a new Spark Context
ctx = context()

# Call load_data method in preprocess and check if it's good.
data = load_data(ctx, 'X_small_train.txt', base = 'https')
print (data.take(4))
# The results should be something like:
# [(0, '00401000 2D BA 2C 37 D0 D3 5E D4 FA FF 4A 9D CD 73 6E C5'),
#   (0, '00401010 D6 B6 09 AC 76 22 29 F4 43 0D 06 CB CE 69 25 DF'),
#    ....
# ]
# That is, data is a RDD[id, line].
# id is the id for each doc (_not_ hash), and line indicates each line in the doc.



# unused code for reading
# data_path = hash_to_url('KM7grcA6yBk1J0CmaWiP', base = 'https')
# ctx.addFile(data_path)
# file_read = ctx.textFile(SparkFiles.get('KM7grcA6yBk1J0CmaWiP.bytes'))
# print (file_read.first())
