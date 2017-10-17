import numpy as np
from scipy import stats

filename = input("ファイル名を入力してください ")
f = open(filename)

z = []
for i in f:
    xyz = i.split()
    if xyz[2]!='-9999.99':
        xyz2 = float(xyz[2])
        z.append(xyz2)

print("最大値:",max(z))
print("最小値:",min(z))
print("平均値:",np.mean(z))
print("中央値:",np.median(z))
print("最頻値:",stats.mode(z))
