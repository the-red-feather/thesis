# Import libraries
from matplotlib import pyplot as plt
import numpy as np
import math;

size = 6

# data
# from https://en.wikipedia.org/wiki/Usage_share_of_web_browsers
browser_data = np.array([
    ["Study", 	"StatCounter", "NetMarketShare", "W3Counter", "Wikimedia"],
    ["Date",     "October 2021", "October 2021", "September 2021", "October 2021 "],
    ["Chrome"   ,67.17 	,72.96 	, 63.3 	, 58.0],
    ["Safari"   ,9.63 	,2.72	, 17.7 	, 9.3],
    ["Edge"     ,9.33 	,12.61 	, 5.4   , 7.8],
    ["Firefox"  ,7.87 	,5.54 	, 5.8   , 10.7],
    ["Opera"    ,2.89 	,1.01 	, 1.3   , 2.0],
    ["Others"   ,3.11 	,5.56 	, 6.5   , 12.2],
])

# extract what we need
header = browser_data[2:, 0]
data = browser_data[2:, 1:].astype('f')

# check it 
# print("header", header)
# print("data", data)
# print(data.dtype) 

# test dataset
# header = ['AUDI', 'BMW', 'FORD',
#         'TESLA', 'JAGUAR', 'MERCEDES'] 
# data = np.array([
#     [23, 16], 
#     [17, 23],
#     [35, 11], 
#     [29, 33],
#     [12, 27], 
#     [41, 42]
# ])
 
# normalizing data to 2 pi
norm = data / np.sum(data)*2 * np.pi
 
# obtaining ordinates of bar edges
left = np.cumsum(np.append(0, norm.flatten()[:-1])).reshape(data.shape)
 
# Creating color scale
cmap = plt.get_cmap("tab20b")
outer_colors = cmap(np.arange(6)*4)

 
# Creating plot
fig, ax = plt.subplots(figsize =(10, 7),
                       subplot_kw = dict(polar = True))
 
ax.bar(x = left[:, 0],
       width = norm.sum(axis = 1),
       bottom = 1-size,
       height = size,
       color = outer_colors,
       edgecolor ='w',
       linewidth = 1,
       align ="edge")
 
for x, w, title in zip(left[:, 0], norm.sum(axis = 1), header):
    percentage = round(w / (2 * np.pi) * 10000) / 100
    text = title + ": " + str(percentage) + "%"
    ax.text(x + 0.5 * w, 1 - size * 0.2, text, ha='center', weight='bold', color='white')

ax.set_axis_off()
 
# show plot
plt.show()