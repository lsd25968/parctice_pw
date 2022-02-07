true_pw = 'a123456'
times = 2

while time > -1:
	pw = input('請輸入密碼: ')
	if pw == true_pw:
		print('登入成功')
	
	else:
		print('密碼錯誤, 你還有',times ,'次輸入機會')
		times = times - 1