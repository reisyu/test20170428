# coding: UTF-8
# ステッピングモーターマイクロステップ制御用の数列を作成する
# 20170603作成
stepN = 4
chanelN = 4

stepList = []

for i in range(chanelN):
    k0 = (i + 0) % chanelN
    k1 = (i + 1) % chanelN
    for j in range(stepN):
        tmp = []
        for k in range(chanelN):
            tmp.append(0)
        tmp[k0] = stepN - j
        tmp[k1] = j
        stepList.append(tmp)

        #print(tmp)

#print(stepList)

for i in stepList:
    print(i)
