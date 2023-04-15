import csv

file_path = input("ファイルパスをドラッグして入力してください: ")

with open(file_path, 'r') as f:

    reader = csv.reader(f)    
    # ヘッダーをスキップ
    header = next(reader)
    
    # 銘柄ごとの取得金額の総額と平均取得単価を計算するための辞書を初期化
    holding_dict = {}
    
    # 各取引の情報を読み込み、銘柄ごとに取得金額を計算
    for row in reader:
        if row[6] != '':  # 銘柄名が記載されている行のみ処理する
            symbol = row[6]  # 銘柄名
            amount = float(row[2])  # 取得数量
            rate = float(row[12])  # 約定レート
            
            # 銘柄が辞書に存在する場合は取得金額を加算し、そうでない場合は辞書に新たに登録する
            if symbol in holding_dict:
                holding_dict[symbol]['total_amount'] += amount * rate
                holding_dict[symbol]['total_quantity'] += amount
            else:
                holding_dict[symbol] = {'total_amount': amount * rate, 'total_quantity': amount}
    
    # 結果をCSVファイルに書き込む
    with open('holding_summary.csv', 'w', newline='') as f_out:
        writer = csv.writer(f_out)
        
        # ヘッダー行を書き込む
        writer.writerow(['銘柄名', '取得金額の総額', '平均取得単価'])
        
        for symbol, values in holding_dict.items():
            total_amount = round(values['total_amount'], 2)
            total_quantity = round(values['total_quantity'], 8)
            average_rate = round(total_amount / total_quantity, 2) if total_quantity != 0 else 0.0
            writer.writerow([symbol, total_amount, average_rate])

print("処理が完了しました。")
