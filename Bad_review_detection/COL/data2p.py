import os
import pandas as pd


def data2frame(data_path):
    data = pd.read_csv(data_path, encoding='utf-8')
    text, label = data['TEXT'], data['label']
    # 保存为txt结构化文件
    data = pd.DataFrame({'Text': text, 'label': label})
    return data


def create_data_folder():
    data_folder = 'data'
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)


if __name__ == '__main__':
    # 创建名为 "data" 的文件夹
    create_data_folder()

    data_paths = ['./COLDataset/train.csv',
                  './COLDataset/test.csv',
                  './COLDataset/dev.csv']

    for data_path in data_paths:
        # 提取文件名，用于保存 txt 文件
        file_name = data_path.split('/')[-1].split('.')[0]

        # 生成保存的 txt 文件名
        save_path = f'data/{file_name}.txt'

        # 读取数据并保存为 txt
        df = data2frame(data_path)
        df.to_csv(save_path, sep='\t', index=False, header=False)
