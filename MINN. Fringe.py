#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from rcv_distances.dist_analysis.distance import DistanceSim, kendall_tau
from rcv_distances.dist_analysis.rcv_elections import rcvElections
import matplotlib.pyplot as plt


# In[2]:


mn_ballots= pd.read_csv('/Users/emariedelanuez/Downloads/minneopolis_data_stv_copy_clean.csv')


# In[3]:


#only select the columns that matter
mn_ballots = mn_ballots[mn_ballots.columns[2:5]]
#Convert columns to list of lists: one list is one voter
mn_ballot_lst = mn_ballots.values.tolist()
#Generate list of unique candidates
mn_cands = mn_ballots[mn_ballots.columns[0]].unique()
print(mn_cands)


# In[4]:


##run rcv election on unfringed ballots
#gives rankings based on amount of first place votes
mn_rcv = rcvElections(mn_ballot_lst, list(mn_cands), 1)
mn_irv = mn_rcv.rcv_run()
# gets rid of overvote, undervote, and write-ins
mn_irv_clean = []
for cand in mn_irv:
    if cand not in ['overvote', 'undervote', 'UWI']:
        mn_irv_clean.append(cand)
mn_irv_clean


# In[5]:


mn_ballots_alt = pd.read_csv('/Users/emariedelanuez/Downloads/minneopolis_data_stv_copy_clean.csv')


# In[6]:


#only select the columns that matter
mn_ballots_alt = mn_ballots_alt[mn_ballots_alt.columns[2:5]]
#gets rid of fringe voters 
mn_ballots_alt = mn_ballots_alt.replace('JOHN CHARLES WILSON', 'FRINGE')
mn_ballots_alt = mn_ballots_alt.replace('CYD GORMAN', 'FRINGE')
mn_ballots_alt = mn_ballots_alt.replace('BOB "AGAIN" CARNEY JR', 'FRINGE')
mn_ballots_alt = mn_ballots_alt.replace('JAMES "JIMMY" L. STROUD', 'FRINGE')
mn_ballots_alt = mn_ballots_alt.replace('RAHN V. WORKCUFF', 'FRINGE')
mn_ballots_alt = mn_ballots_alt.replace('EDMUND BERNARD BRUYERE', 'FRINGE')
mn_ballots_alt = mn_ballots_alt.replace('JOHN LESLIE HARTWIG', 'FRINGE')
mn_ballots_alt = mn_ballots_alt.replace('BILL KAHN', 'FRINGE')
mn_ballots_alt = mn_ballots_alt.replace('MERRILL ANDERSON', 'FRINGE')
mn_ballots_alt = mn_ballots_alt.replace('JOSHUA REA', 'FRINGE')
mn_ballots_alt = mn_ballots_alt.replace('GREGG A. IVERSON', 'FRINGE')
mn_ballots_alt = mn_ballots_alt.replace('NEAL BAXTER', 'FRINGE')
mn_ballots_alt = mn_ballots_alt.replace('TROY BENJEGERDES', 'FRINGE')
mn_ballots_alt = mn_ballots_alt.replace('JEFFREY ALAN WAGNER', 'FRINGE')
mn_ballots_alt = mn_ballots_alt.replace('CHRISTOPHER ROBIN ZIMMERMAN', 'FRINGE')
mn_ballots_alt = mn_ballots_alt.replace('CHRISTOPHER CLARK', 'FRINGE')
mn_ballots_alt = mn_ballots_alt.replace('JAYMIE KELLY', 'FRINGE')
mn_ballots_alt = mn_ballots_alt.replace('KURTIS W. HANNA', 'FRINGE')
#Convert columns to list of lists one list is one voter-- fringed version
mn_ballot_lst = mn_ballots_alt.values.tolist()
#Generate list of unique candidates- fringed version
mn_cands = mn_ballots_alt[mn_ballots_alt.columns[0]].unique()


# In[7]:


# for every ballot in the ballot list, you delete all occurences of fringe, so that when we run the irv we can return a vector of length n- number of fringe candidates
# basically just changing the number of candidates in the election
for i in range(len(mn_ballot_lst)):
    candidate = mn_ballot_lst[i]
    mn_ballot_lst[i] = [y for y in candidate if y!="FRINGE"]
    
#for candidate in mn_ballot_lst:
    if 'FRINGE' in mn_ballot_lst:
        print("bad")


# In[8]:


# makes a list of candidates that are not fringe that is produced by the fringed ballots 
mn_cands_fringe = [x for x in mn_cands if x!='FRINGE']


# In[9]:


# runs rcv election with fringe ballots/candidates
mn_rcv_fringe = rcvElections(mn_ballot_lst, list(mn_cands_fringe), 1)
mn_irv_new = mn_rcv_fringe.rcv_run()
#gives rankings based on amount of first place votes
#cleans up columns and returns irv election conducted with fringe candidates
mn_irv_fringe = []
for cand in mn_irv_new:
    if cand not in ['overvote', 'undervote', 'UWI']:
        mn_irv_fringe.append(cand)
mn_irv_fringe

#mn_irv_fringe.remove('FRINGE')
#print(mn_irv_fringe)


# In[10]:


#read in minneopolis election data
random = pd.read_csv('/Users/emariedelanuez/Downloads/clean_mn_dataset.csv')


# In[11]:


#indexes the number of candidates with regards to the "first" column which indicates how many first place votes each candidate got 
idk = random.set_index('candidate').to_dict()['first']


# In[12]:


print(idk)


# In[13]:


##just making all of the words lowercase, so that no errors happen when doing bubble sort
fringe_candidates_list = ['JOHN CHARLES WILSON','CYD GORMAN', 'BOB "AGAIN" CARNEY JR', 'JAMES "JIMMY" L. STROUD','RAHN V. WORKCUFF', 'EDMUND BERNARD BRUYERE','JOHN LESLIE HARTWIG','BILL KAHN','MERRILL ANDERSON','JOSHUA REA','GREGG A. IVERSON','NEAL BAXTER','TROY BENJEGERDES','JEFFREY ALAN WAGNER', 'CHRISTOPHER ROBIN ZIMMERMAN','CHRISTOPHER CLARK', 'JAYMIE KELLY', 'KURTIS W. HANNA']


# In[14]:


# makes a copy of the unfringed irv election that we affectionaly called mn_irv_og
mn_irv_OG = mn_irv_clean.copy()

# for loop that iterates through the unfringed irv election, checking to see if any of the candidates are on our fringe list, if they are then we remove them from the og copy 
for cand in mn_irv_clean:
    if cand in fringe_candidates_list:
        mn_irv_OG.remove(cand)
        
print(mn_irv_OG)
#checks to see if the length of the original irv is the same length as the fringe irv 
print(len(mn_irv_OG) == len(mn_irv_fringe))


# In[15]:


# instantiate an empty list that iterates through the candidates in mn_irv_og and appendes the candidates index number to our fringe rank list
irv_fringe_ranks=[]
for cand in mn_irv_OG:
    irv_fringe_ranks.append(mn_irv_fringe.index(cand))
print(irv_fringe_ranks)



# In[16]:


# bubble sort function that reorders the indexes based on numerical order and for every switch adds "1" to the variable = swap count that delivers the swap value
def kendall_tau(irv_fringe_ranks):
    swapcount = 0 
    for j in irv_fringe_ranks: #range(len(mapped)):
        for i in range(1, len(irv_fringe_ranks)-j):
            if irv_fringe_ranks[i-1] > irv_fringe_ranks[i]:
                swapcount += 1
                irv_fringe_ranks[i-1], irv_fringe_ranks[i] = irv_fringe_ranks[i], irv_fringe_ranks[i-1]
    
    return swapcount

kendall_tau(irv_fringe_ranks)


# In[ ]:





# In[ ]:




