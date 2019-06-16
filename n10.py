# # num = sum(1 for line in file) # count number of lines

# file = open("n.txt", "a+")
# name = "Huong"
# year = "1998"
# file.writelines(name + " " + year + " " + "26\n")
# file.close

# x= "045"
# x = int(x)
# print(x)

# l1 = ["A", "B", "C"]
# l2 = ["A"]

# l1 = l1.remove("A")
# print(l1)

data = ['TRAN.NGOC.THAI 0356874982 20 M 45000\n', 'NGUYEN.NGOC.NGAN 0945125365 18 M 37520\n', 'HUYNH.THI.NGOC.NHI 01684532145 29 F 36610\n', 'HUYNH.NGOC.THINH 0983456246 35 M 32010\n', 'BUI.NHU.NGOC 0704562365 30 F 29670\n', 'NGUYEN.NHU.NGOC 0869624756 29 F 28800\n', 'NGUYEN.VAN.NGOC 0905655236 25 M 25400\n', 'VO.VAN.NGOC 01123452454 26 M 19450\n', 'TRAN.VAN.NGOC 0984567352 30 M 12200\n', 'VO.THU.NGOC 0425624123 25 F 9870\n', 'NGUYEN.TRAN.NGOC 0988475216 24 F 4250\n', 'TRAN.HUNG.DUNG 0123456789 25 M 58000\n', 'x 0987654321 0 x 7950\n']
file = open("m.txt", "r+")
file.writelines(["%s" %item for item in data])
file.close