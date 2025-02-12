import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
import os

# 定义CSV文件路径模板
csv_file_path_template = 'datasets\\detection_part_{}.csv'
root_dir = r"datasets"

#读取文件夹下所有文件
csv_list = os.listdir(root_dir)

for i in range(len(csv_list)):
    
    csv_file_path = csv_file_path_template.format(i + 1)
    
    # 初始化坐标列表
    x_coords = []
    y_coords = []
    z_coords = []

    # 读取CSV文件
    with open(csv_file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        
        # 读取表格中第一行
        header = next(csv_reader)
        timestamp = header['y(m)']
        
        for row in csv_reader:
            try:
                # 读取x, y, z坐标
                x = float(row['x(m)'])
                y = float(row['y(m)'])
                z = float(row['z(m)'])
                
                # 添加到坐标列表
                x_coords.append(x)
                y_coords.append(y)
                z_coords.append(z)
                
            except ValueError:
                # 跳过包含无效数据的行
                continue

    # 创建3D散点图
    fig = plt.figure(figsize=(16, 9))  # 调整图形大小为全屏
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_coords, y_coords, z_coords, c='r', marker='o')

    # 设置坐标轴标签
    ax.set_xlabel('X Coordinate (m)')
    ax.set_ylabel('Y Coordinate (m)')
    ax.set_zlabel('Z Coordinate (m)')
    
    # 在左上角显示Timestamp_Seconds
    fig.text(0.05, 0.95, f'Timestamp: {timestamp}', transform=fig.transFigure)

    print(f"文件 {csv_file_path} 的点云数据量为：{len(x_coords)}, 时间戳为：{timestamp}")

    # 显示图形
    manager = plt.get_current_fig_manager()
    manager.window.showMaximized()
    plt.show()





