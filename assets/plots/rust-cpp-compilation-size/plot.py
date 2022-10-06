import numpy as np
import matplotlib.pyplot as plt
 
# took something from internet

# startup / init
rust_min = [59, 58, 56, 58, 59, 60, 63, 25, 56, 59, 60, 63, 65, 58, 58]
cpp_min = [71, 69, 73, 70, 76, 65, 66, 67, 71, 72, 68, 59, 59, 68, 61]
js_min = [0]

columns_startup = [rust_min, cpp_min, js_min]

# process
p_rust_min = [131, 133,132, 141, 133, 132, 140, 134, 130, 133, 133, 130, 133]
p_cpp_min = [967, 950, 966, 958, 956, 940, 953, 965]
p_js_min = [22, 25, 21, 21, 22, 21, 23, 21]

columns_process = [p_rust_min, p_cpp_min, p_js_min]

figure, axis = plt.subplots(1, 2)
  
axis[0].boxplot(columns_startup, labels=['rust', 'c++', 'js'])
axis[0].set_title("Startup time")
axis[0].set_ylabel("ms")

axis[1].boxplot(columns_process, labels=['rust', 'c++', 'js'])
axis[1].set_title("Process time")
axis[1].set_ylabel("ms")

plt.show()
  