import os
import glob
import numpy as np

# bin_path = '/media/autolab/2T/FLC/16_lidar_test/test_pcd'
bin_path = './velo_result/data'

if not os.path.exists(bin_path):
    print("ERROR: Velodyne path does not exists.")
    exit(-1)

bins = glob.glob(bin_path + '/*.bin')
bins.sort()
bin_files = {i: bins[i] for i in range(len(bins))}

for i in bin_files.keys():
    points = np.fromfile(bin_files[i], dtype=np.float32).reshape(-1, 4)
    pass

