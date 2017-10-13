ss = input()
data = ss.split()
data_xishu = data[::2]
data_zhishu = data[1::2]
data_zhishu_new = []
data_xishu_new = []
for i in range(len(data_xishu)):
    data_xishu_new.append(int(data_xishu[i]) * int(data_zhishu[i]))
    data_zhishu_new.append(int(data_zhishu[i]) - 1)
# print(data_xishu_new)
# print(data_zhishu_new)
for i in range(len(data_xishu_new)):
    data[2 * i] = data_xishu_new[i]
    data[2 * i + 1] = data_zhishu_new[i]
# print(data[-1])
if (data[-1] == -1):
    data.pop()
    data.pop()
out = ""
for i in data:
    out += str(i) + " "
print(out.rstrip())
