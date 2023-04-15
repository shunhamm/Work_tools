import pandas as pd
import re

# ファイル名をユーザーに入力してもらう
csv1_file = input("Enter the filename for the first CSV file: ")
csv2_file = input("Enter the filename for the second CSV file: ")

# 引用符で囲まれたファイルパスを検出して除去する
quoted_file_pattern = re.compile(r'^\'(.*)\'$|^\"(.*)\"$')
csv1_match = re.match(quoted_file_pattern, csv1_file)
if csv1_match:
    csv1_file = csv1_match.group(1) or csv1_match.group(2)
csv2_match = re.match(quoted_file_pattern, csv2_file)
if csv2_match:
    csv2_file = csv2_match.group(1) or csv2_match.group(2)

# CSVファイルをpandasのデータフレームとして読み込む
df1 = pd.read_csv(csv1_file)
df2 = pd.read_csv(csv2_file)

# 2つ目のCSVファイルを最初のCSVに追記する
df = pd.concat([df1, df2], ignore_index=True)

# 結合されたデータフレームを新しいCSVファイルに書き出す
output_file = "output/merged_output.csv"
output_file_match = re.match(quoted_file_pattern, output_file)
if output_file_match:
    output_file = output_file_match.group(1) or output_file_match.group(2)
df.to_csv(output_file, index=False)

print("CSV files have been successfully merged.")
