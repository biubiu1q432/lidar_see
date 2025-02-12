import csv

# 定义CSV文件路径
csv_file_path = 'detection.csv'

# 初始化变量
file_count = 1
header = None
rows = []

# 读取CSV文件并按Timestamp_Seconds字段切割
with open(csv_file_path, mode='r', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if header is None:
            header = row
            continue
        
        if 'Timestamp_Seconds' in row:
            # 保存当前部分到新文件
            output_file_path = f'detection_part_{file_count}.csv'
            with open(output_file_path, mode='w', newline='') as output_file:
                csv_writer = csv.writer(output_file)
                csv_writer.writerow(header)
                csv_writer.writerows(rows)
            
            # 重置变量
            file_count += 1
            rows = []
        
        rows.append(row)

# 保存最后一部分到新文件
if rows:
    output_file_path = f'detection_part_{file_count}.csv'
    with open(output_file_path, mode='w', newline='') as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerow(header)
        csv_writer.writerows(rows)