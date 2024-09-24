import os
import matplotlib
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
import logging

# GLOBAL CONSTANTS

PATH_TO_FIGURES = "../figs/"
FIGSIZE=(11, 7)
LEGEND_FONTSIZE = 26
LABEL_FONTSIZE = 40
hatches = ['xx', '\\\\', '//', '--', '++', '||', 'o', 'O', '.', '*']
width = 0.35  # the width of the bars
line_width = 3.5
colors = ['#7F449B', '#009D72', '#E5A023']
font = {'family': 'Arial',
        'weight' : 'normal',
        'size'   : 40}
matplotlib.rcParams['pdf.fonttype']=42
matplotlib.rcParams['ps.fonttype']=42
bar_common_args = {"linewidth": line_width, "zorder": 3, "facecolor": "white"}
bar1_args = {"edgecolor": colors[0], "hatch": hatches[0]}
bar2_args = {"edgecolor": colors[1], "hatch": hatches[1]}

# envsetup

plt.rc('font', **font)
plt.rcParams.update({'legend.handlelength': 1.3, 'legend.borderpad': 0.25, "legend.labelspacing": 0.25, "legend.handletextpad": 0.5})
plt.rcParams['hatch.linewidth'] = line_width
pd.set_option("display.max_colwidth", 5000)
pd.set_option("display.max_columns", 10000)
pd.set_option("display.max_rows", 100)
os.makedirs(PATH_TO_FIGURES, exist_ok=True)
warnings.filterwarnings('ignore')

# refresh the fonts just installed
matplotlib.font_manager._load_fontmanager(try_read_cache=False)

folder_path = 'data/memory_size/'
sub_folders = ['GAE/', 'QK/', 'Pixel/']


data = []

for folder in sub_folders:
    path = folder_path + folder
    file_names = os.listdir(path)
    print(len(file_names))
    tmp = []
    for file_name in file_names:
        file_path = os.path.join(path, file_name)
        # 打开并读取文件内容
        with open(file_path, 'r') as file:
            content = file.read()
            if len(content) == 0:
                numbers = []
            else:
                numbers = [float(num) for num in content.split(',')]
            tmp += numbers
    print(len(tmp))
    data.append(tmp)
    # print(tmp[0:100])
f, ax = plt.subplots(figsize=(9.6, 7))
plt.ylim((0, 1.2))
plt.yticks(ticks=[0, 0.2, 0.4, 0.6 ,0.8, 1], labels = ['0', '0.2', '0.4', '0.6' ,'0.8', '1'])
plt.xlim((0, 25))

print(len(data[1]))
count2, bins_count2 = np.histogram(data[1], bins=5000)
pdf2 = count2 / sum(count2)
cdf2 = np.cumsum(pdf2)
cdf2 = np.insert(cdf2, 0, 0)  # 确保从0开始
plt.plot(bins_count2, cdf2, color=colors[1], zorder=1, clip_on=True, linewidth=4)
# post_per[0] = 201.1
count, bins_count = np.histogram(data[0], bins=5000)

# finding the PDF of the histogram using count values
pdf = count / sum(count)

# using numpy np.cumsum to calculate the CDF
cdf = np.cumsum(pdf)
cdf = np.insert(cdf, 0, 0);

plt.xlabel('Memory Size (MiB)', fontsize = LABEL_FONTSIZE)
plt.ylabel('CDF', fontsize = LABEL_FONTSIZE)
ax.set_xticks([0, 5, 10, 15, 20, 25], ['0','5','10','15','20','25'])

# plot the actual lines
plt.plot(bins_count, cdf, color=colors[2], zorder=1, clip_on=True, linewidth=4, linestyle='dashed')


count3, bins_count3 = np.histogram(data[2], bins=5000)
pdf3 = count3 / sum(count3)
cdf3 = np.cumsum(pdf3)
cdf3 = np.insert(cdf3, 0, 0)
plt.plot(bins_count3, cdf3, color=colors[0], zorder=1, clip_on=True, linewidth=4, linestyle=(0,(1,1)))


bbox = dict(boxstyle="square,pad=0.3", facecolor='none', edgecolor='black')
def get_bbox_text(freq_diff):
    bbox_text = f"Max = {round(np.max(freq_diff),2)}%\nMean = {round(np.mean(freq_diff),2)}%\nMedian = {round(np.median(freq_diff),2)}%\nMin = {round(np.min(freq_diff),2)}%"
    return bbox_text

plt.annotate(
    text="Max = {:.2f}\nMean = {:.2f}".format(round(np.max(data[0]),2), round(np.mean(data[0]),2)),
    xy=(bins_count[2200], cdf[2200]),
    xytext=(15, 0.4),
    textcoords="data",
    fontsize=28,
    bbox=bbox
)
plt.annotate(
    text='',
    xy=(bins_count[2460], cdf[2460]),
    xytext=(16.5, 0.57),
    textcoords="data",
    fontsize=28,
    arrowprops=dict(arrowstyle="<-", connectionstyle="arc3", color=colors[2],linewidth=4,),
)

# 对第二条线添加bbox
plt.annotate(
    text="Max = {:.2f}\nMean = {:.2f}".format(round(np.max(data[1]),2), round(np.mean(data[1]),2)),
    xy=(bins_count2[600], cdf2[600]),
    xytext=(2, 0.1),
    textcoords="data",
    fontsize=28,
    arrowprops=dict(arrowstyle="<-", connectionstyle="arc3", color=colors[1],linewidth=4),
    bbox=bbox
)

# 对第3条线添加bbox
plt.annotate(
    text="Max = {:.2f}\nMean = {:.2f}".format(round(np.max(data[2]),2), round(np.mean(data[2]),2)),
    xy=(bins_count3[1700], cdf3[1700]),
    xytext=(11, 0.1),
    textcoords="data",
    fontsize=28,
    arrowprops=dict(arrowstyle="<-", connectionstyle="arc3", color=colors[0],linewidth=4),
    bbox=bbox
)


for label in ax.get_yticklabels():
    if label.get_text() == '0':
        label.set_visible(False)
        break

line_w, = ax.plot([0], label='GAE', linewidth=4, linestyle='dashed', color=colors[2])
line_b, = ax.plot([0], label='QEMU-KVM', linewidth=4, color=colors[1])
line_r, = ax.plot([0], label='Pixel 6a', linewidth=4, color=colors[0], linestyle=(0,(1,1)))
l2 = ax.legend(handles = [line_r, line_w, line_b], loc = 'upper left', handlelength=1.5, bbox_to_anchor=(-0.005, 1.005), fontsize=LEGEND_FONTSIZE, edgecolor = 'black', fancybox = False, ncol=1)

plt.show()

f.savefig(PATH_TO_FIGURES + "datasize_cdf.pdf", format = "pdf", bbox_inches = 'tight')