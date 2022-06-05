import pandas as pd 

csv_dir = r'C:\Users\15284\Desktop\TransMIL-main\dataset_csv\camelyon16\fold0.csv'
csv_dir2 =  r'C:\Users\15284\Desktop\TransMIL-main\dataset_csv\tcga_coad\fold0.csv'

csv = pd.read_csv(csv_dir,index_col=1)
print(csv)
csv2 = pd.read_csv(csv_dir2)
print(csv2)