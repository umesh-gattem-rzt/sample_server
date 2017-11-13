"""Model Prediction template code will be appended"""
print('Model Inference...')
import json
import sys


def run_stage(params, message):
    # code to call predict API

    import rztdl.dl
    import numpy as np
    from rztdl.utils.file import read_csv, to_csv

    train_data, train_label = read_csv(filename='data/titanic.csv',
                                       split_ratio=[100, 0, 0],
                                       delimiter=',', label_vector=False, randomize=True)

    # Prediction
    prediction = rztdl.dl.Prediction('titanic_data')
    preds = prediction.predict(layer_name='output_layer',
                               data={'input_layer': train_data}, batches=2)
    to_csv(data={'TRUE': np.reshape(train_label, newshape=[-1, ]),
                 'LI': np.reshape(preds, newshape=[-1, ])}, save_path='/tmp/output.csv')


param = json.loads(sys.argv[1])
run_stage(params=param['parameters'], message=None)
