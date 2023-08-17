#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt


# In[12]:


# Sample data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]  # x-coordinates
y = [0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 3, 1, 1]  # y-coordinates

# Create scatter plot
plt.scatter(x, y)

# Set labels and title
plt.xlabel('Number of Fringe Candidates')
plt.ylabel('Swap Distance')
plt.title('')

# Show the plot
plt.show()

plt.savefig('/Users/emariedelanuez/Desktop/fringe_candidates.png')  # Replace 'path/to/save/plot.png' with the desired file path and name


# In[ ]:




