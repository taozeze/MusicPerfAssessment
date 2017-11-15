import os
import sys
from collections import defaultdict
import dill
import numpy as np
from DataUtils import DataUtils


# Initialize input params, specify the band, intrument, segment information
BAND = 'middle'
SEGMENT = 2
YEAR = ['2013', '2014', '2015']

# define paths to FBA dataset and FBA annotations
PATH_FBA_ANNO = '/home/apati/FBA2013/'

# create data holder
perf_assessment_data = []
# instantiate the data utils object for different instruments and create the data
INSTRUMENT = 'Alto Saxophone'
utils = DataUtils(PATH_FBA_ANNO, BAND, INSTRUMENT)
for year in YEAR:
    perf_assessment_data += utils.create_data(year, SEGMENT)

INSTRUMENT = 'Bb Clarinet'
utils = DataUtils(PATH_FBA_ANNO, BAND, INSTRUMENT)
for year in YEAR:
    perf_assessment_data += utils.create_data(year, SEGMENT)

INSTRUMENT = 'Flute'
utils = DataUtils(PATH_FBA_ANNO, BAND, INSTRUMENT)
for year in YEAR:
    perf_assessment_data += utils.create_data(year, SEGMENT)

print(len(perf_assessment_data))

file_name = BAND + '_' + str(SEGMENT) + '_data'
if sys.version_info[0] < 3:
    with open('../dat/' + file_name + '.dill', 'wb') as f:
        dill.dump(perf_assessment_data, f)
else:
    with open('../dat/' + file_name + '_3.dill', 'wb') as f:
        dill.dump(perf_assessment_data, f)