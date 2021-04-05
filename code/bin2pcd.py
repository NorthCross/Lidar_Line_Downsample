import os
import glob
import numpy as np

bin_path = './velo_result/data'
pcd_path = '/media/autolab/2T/FLC/velo16_pcd/data'


if not os.path.exists(pcd_path):
    os.makedirs(pcd_path)

if not os.path.exists(bin_path):
    print("ERROR: Velodyne path does not exists.")
    exit(-1)

bins = glob.glob(bin_path + '/*.bin')
bins.sort()
bin_files = {i: bins[i] for i in range(len(bins))}

for i in bin_files.keys():
    print("Processing " + pcd_path + '/' + str(i).rjust(6, '0') + '.pcd')
    points = np.fromfile(bin_files[i], dtype=np.float32).reshape(-1, 4)
    pcd_file = open(pcd_path + '/' + str(i).rjust(6, '0') + '.pcd', 'w', -1)
    pcd_file.write("VERSION 0.7\n" + "FIELDS x y z\n" +
                   "SIZE 4 4 4\n" + "TYPE F F F\n" + "COUNT 1 1 1\n" + "WIDTH " + str(points.shape[0]) +
                   "\nHEIGHT 1\n" + "VIEWPOINT 0 0 0 1 0 0 0\n" + "POINTS " + str(points.shape[0]) + "\nDATA ascii\n\n")
    for point in points:
        pcd_file.write(str(point[0]) + ' ' +
                       str(point[1]) + ' ' + str(point[2]) + '\n')
        pass
    pcd_file.close()
pass
