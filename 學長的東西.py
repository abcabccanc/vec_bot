import os
import pandas as pd
folder_path = r'C:\Users\adam0\OneDrive\桌面\新增資料夾'  # 資料夾路徑
#columes 命名
all_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) ]
print(all_files)
df_list = []
for i in all_files:
    filename=os.path.basename(i)[-6:-4]
    a=pd.read_excel(i, sheet_name=1)
    a.columns=['序號', '時間', filename+'溫度°C', filename+'濕度%RH']
    print(a.columns)
#合成資料
    df_list.append(a)
print(df_list)
combined = pd.concat(df_list,axis=1)

#刪除重複columns
combined=combined.loc[:, combined.columns.duplicated()]
print(combined)
combined.to_excel('1.xlsx', index=False)

