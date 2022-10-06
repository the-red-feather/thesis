import numpy as np
import matplotlib.pyplot as plt
 
# took something from internet

# set width of bar
barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))
 
# set height of bar
RUST = [20.140, 114.263]
ECE = [68.424, 257.994]
count = len(RUST)

# Set position of bar on X axis
br1 = np.arange(count)
br2 = [x + barWidth for x in br1]
 
# Make the plot
plt.bar(br1, RUST, color ='r', width = barWidth,
        edgecolor ='grey', label ='Rust')
plt.bar(br2, ECE, color ='g', width = barWidth,
        edgecolor ='grey', label ='C++')
 
# Adding Xticks
plt.title("size of compilation artefacts")
plt.ylabel('kb', fontweight ='bold', fontsize = 15)
plt.xticks([r + (barWidth / 2) for r in range(count)],
        ['minimum example', 'startin / cgal tin'])
 
plt.legend()
plt.show()