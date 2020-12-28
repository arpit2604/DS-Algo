def longestPeak(array):
	peak_len = 0
	peak_len_backup = 0
	peak_len_backup_old = 0
	peak_det = False

	if len(array)<3:
		return peak_len
	for i in range(len(array)-1):
		if array[i] < array[i+1]:
			peak_len+=1
		elif array[i] == array[i+1] and peak_det == False :
			#peak_len_backup = peak_len
			peak_len = 0
		elif array[i] > array[i+1] and peak_len > 0:
			peak_len+=1
			peak_det = True
		if array[i] < array[i+1] and peak_len > 0 and peak_det == True:
			peak_len_backup = peak_len
			if peak_len_backup > peak_len_backup_old:
				peak_len_backup_old = peak_len_backup
			peak_len_backup = peak_len
			peak_len=0
			peak_len+=1
			peak_det = False
		print(peak_len)
	if peak_det == False:
		peak_len = 0
	if peak_len_backup_old>=peak_len:
		return peak_len_backup_old
	else:
		return peak_len+1
		#else:
		#	return peak_len_backup
	
