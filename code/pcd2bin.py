import os
import glob
import numpy as np

bin_path = '/media/TIEV/Datasets/16_lidar_test/test_bin'
pcd_path = '/media/TIEV/Datasets/16_lidar_test/test_pcd'

def load_pcd_data(file_path):
	pts = []
	f = open(file_path, 'r')
	data = f.readlines()
 
	f.close()
	line = data[9]
	# print line
	line = line.strip('\n')
	i = line.split(' ')
	pts_num = eval(i[-1])
	for line in data[12:]:
		line = line.strip('\n')
		xyz = line.split(' ')
		x, y, z = [eval(i) for i in xyz[:3]]
		pts.append([x, y, z, 1.0])
 
	assert len(pts) == pts_num
	res = np.zeros((pts_num, len(pts[0])), dtype=np.float32)
	for i in range(pts_num):
		res[i] = pts[i]
	# x = np.zeros([np.array(t) for t in pts])
	return res

if not os.path.exists(bin_path):
    os.makedirs(bin_path)

if not os.path.exists(pcd_path):
    print("ERROR: Velodyne path does not exists.")
    exit(-1)

pcds = glob.glob(pcd_path + '/*.pcd')
pcds.sort()
pcd_files = {i: pcds[i] for i in range(len(pcds))}

for i in pcd_files.keys():
    print("Processing " + bin_path + '/' + str(i).rjust(6, '0') + '.bin')
    res = load_pcd_data(pcd_files[i])
    res.tofile(bin_path + '/' + str(i).rjust(6, '0') + ".bin")
    pass

pass
