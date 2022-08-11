import csv	#csvモジュールのインポート

with open ('log02.csv','r') as f:	#csvファイルの読み込み
	reader = csv.reader(f)		#ファイルからデータを読み込む
	line = [row for row in reader]	#csvファイルを二次元リストに格納
		 
	N = 3		#Nの値をここで決める
	count = 0		#'-'の数のカウント

	for n in range(len(line)):	#csvファイルの行の数だけループ
		if line[n][2] == '-':		#応答結果が'-'の場合
			count = count +1		#countに1足す
			if count >= N and line[n + 1][2] != '-':		#連続する'-'の数がN以上かつ、次の行の要素が'-'でないとき
				print(line[n + 1- count ][0] + "~" + line[n+1][0])	#期間の表示
		else:			#応答結果が数字の場合
			count = 0			#countの値をリセットする
