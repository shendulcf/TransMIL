import pandas as pd

for i in range(5):
    # 从CSV文件加载原始数据
    original_df = pd.read_csv(f'dataset_csv/cptac_lung_100/splits_{i}.csv')

    # 从包含标签信息的CSV文件加载标签数据
    label_df = pd.read_csv('cptac_lung_subtyping.csv')

    # 合并标签信息到原始数据框中的各列
    original_df['train_label'] = original_df['train'].map(label_df.set_index('slide_id')['label'])
    original_df['val_label'] = original_df['val'].map(label_df.set_index('slide_id')['label'])
    original_df['test_label'] = original_df['test'].map(label_df.set_index('slide_id')['label'])

    #label mapping
    original_df.replace({'train_label': {'LUAD': 0, 'LUSC': 1}, 'val_label': {'LUAD': 0, 'LUSC': 1}, 'test_label': {'LUAD': 0, 'LUSC': 1}}, inplace=True)
    # 重新排列列的顺序
    original_df = original_df[['train', 'train_label', 'val', 'val_label', 'test', 'test_label']]
    # 保存到新的CSV文件
    original_df.to_csv(f'dataset_csv/cptac_lung_100/fold{i}.csv', index=False)
