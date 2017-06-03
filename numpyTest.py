# coding: UTF-8
# 本体を回転させずに任意の方向に移動する場合の各ホイールの回転角速度
# 20170603作成

import numpy as np
import math as ma

# 進行方向を指定
dir = 90
dirX = ma.cos(ma.radians(dir))
dirY = ma.sin(ma.radians(dir))

# 各ホイールの係数を計算
a1 = ma.cos(ma.radians(  0+90))
a2 = ma.cos(ma.radians(120+90))
a3 = ma.cos(ma.radians(240+90))

b1 = ma.sin(ma.radians(  0+90))
b2 = ma.sin(ma.radians(120+90))
b3 = ma.sin(ma.radians(240+90))

# 連立方程式を解いて各ホイールの回転角速度を決定
A = np.array([[a1, a2, a3],
              [b1, b2, b3],
              [ 1,  1,  1]])
b = np.array( [ dirX,  dirY,  0])

x = np.linalg.solve(A, b)

print(x)
print(max(abs(x)))

# 最大値が1になるように調整
x = x/max(abs(x))
print(x)

# 計算結果の確認
vx = (x[0]*a1 + x[1]*a2 + x[2]*a3)
vy = (x[0]*b1 + x[1]*b2 + x[2]*b3)
m = (x[0] + x[1] + x[2])

print(vx, vy, m)
print(ma.degrees(ma.atan(vy/vx)))