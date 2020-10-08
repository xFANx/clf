import os
data_path = './common.txt' # 通用数据
data_sp_path = './special.txt' # 特别的数据，注意按比例划分到三个数据集中
data_ssp_path = './sspecial.txt'
train_path = './train.txt'
valid_path = './test.txt'
test_path = './valid.txt'


f_in = open(data_path, 'r')
f_sp_in = open(data_sp_path, 'r')
f_ssp_in = open(data_ssp_path, 'r')
f_train_out = open(train_path, 'w')
f_valid_out = open(valid_path, 'w')
f_test_out = open(test_path, 'w')


imgs = {}
imgs_sp = {}
imgs_ssp = {}

for line in f_in:
	# print(line)
	path, label = line.split()
	imgs[path] = label

for line in f_sp_in:
	path, label = line.split()
	imgs_sp[path] = label

for line in f_ssp_in:
	path, label = line.split()
	imgs_sp[path] = label

for i in imgs_sp:
	if i in imgs:
		del imgs[i]

for i in imgs_ssp:
	if i in imgs:
		del imgs[i]

length_imgs = len(imgs)
length_sp = len(imgs_sp)
length_ssp = len(imgs_ssp)
print(length_imgs)
print(length_sp)
print(length_ssp)



split_proportion_list = [6, 2, 2]
split_position_img_list = []
split_position_sp_list = []

split_position_img_list.append(length_imgs * split_proportion_list[0] // 10)
split_position_img_list.append(length_imgs * split_proportion_list[1] // 10 + split_position_img_list[0])
# split_position_img_list[2] = length_imgs

split_position_sp_list.append(length_sp * split_proportion_list[0] // 10)
split_position_sp_list.append(length_sp * split_proportion_list[1] // 10 + split_position_sp_list[0])
# split_position_sp_list[2] = length_sp


if __name__ == '__main__':
	
	train = []
	valid = []
	test = []
	for idx, line in enumerate(imgs):
		_str = line + ' ' + imgs[line] + '\n'
		if (idx < split_position_img_list[0]):
			train.append(_str)
			# f_train_out.write(_str)
		elif (idx < split_position_img_list[1]):
			valid.append(_str)
			# f_valid_out.write(_str)
		else:
			test.append(_str)
			# f_test_out.write(_str)
	
	for idx, line in enumerate(imgs_sp):
		_str = line + ' ' + imgs_sp[line] + '\n'
		if (idx < split_position_sp_list[0]):
			train.append(_str)
			# f_train_out.write(_str)
		elif (idx < split_position_sp_list[1]):
			valid.append(_str)
			# f_valid_out.write(_str)			
		else:
			test.append(_str)
			# f_test_out.write(_str)

	for idx, line in enumerate(imgs_ssp):
		_str = line + ' ' + imgs_ssp[line] + '\n'
		test.append(_str)
		
		 
	train.sort()
	valid.sort()
	test.sort()

	for _ in train:
		f_train_out.write(_)
	for _ in valid:
		f_valid_out.write(_)
	for _ in test:
		f_test_out.write(_)
	f_in.close()
	f_sp_in.close()
	f_train_out.close()
	f_valid_out.close()
	f_test_out.close()
	print('hello world')