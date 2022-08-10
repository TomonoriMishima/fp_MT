import csv	#csvモジュールのインポート

with open ('log01.csv','r') as f:	#csvファイルの読み込み
	reader = csv.reader(f)		#ファイルからデータを読み込む
	line = [row for row in reader]		#csvファイルを二次元リストに格納
	
	for n in range(len(line)):	#csvファイルの行の数だけループ
		if line[n][2] == '-':		#応答結果が'-'の場合
			print(line[n][0] + "~" + line[n+1][0])	#期間の表示
			print(line[n][1])			#アドレスの表示
