import os
import cv2
import numpy as np

path = ''

def get_mean(path):
	file_names = os.listdir(path)
	R_mean_list = []
	G_mean_list = []
	B_mean_list = []
	for file_name in file_names:
		img = cv2.imread(os.path.join(path, file_name), 1)
		B_mean_list.append(np.mean(img[:, :, 0]))
		G_mean_list.append(np.mean(img[:, :, 1]))
		R_mean_list.append(np.mean(img[:, :, 2]))
	B_mean = np.mean(B_mean_list)
	G_mean = np.mean(G_mean_list)
	R_mean = np.mean(R_mean_list)
	return R_mean, G_mean, B_mean


def get_var(path, R_mean, G_mean, B_mean):
	file_names = os.listdir(path)
	R_std_list = []
	G_std_list = []
	B_std_list = []
	for file_name in file_names:
		img = cv2.imread(os.path.join(path, file_name), 1)
		B_std_list.append((np.mean(img[:, :, 0]) - B_mean) ** 2)
		G_std_list.append((np.mean(img[:, :, 1]) - G_mean) ** 2)
		R_std_list.append((np.mean(img[:, :, 2]) - R_mean) ** 2)
	B_std = np.sqrt(np.mean(B_std_list))
	G_std = np.sqrt(np.mean(G_std_list))
	R_std = np.sqrt(np.mean(R_std_list))
	return R_std, G_std, B_std
