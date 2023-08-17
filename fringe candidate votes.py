#!/usr/bin/env python
# coding: utf-8

# In[113]:


import pandas as pd
import numpy
import matplotlib.pyplot as plt
import random
import itertools
from numpy.random import choice


# In[6]:


data= pd.read_csv('/Users/emariedelanuez/Downloads/minneopolis_data_stv.csv')


# In[11]:


data.head()


# In[12]:


voting_columns=["1ST CHOICE MAYOR MINNEAPOLIS", "2ND CHOICE MAYOR MINNEAPOLIS", "3RD CHOICE MAYOR MINNEAPOLIS"]


# In[16]:


#gets you all the unique values in the column
data["1ST CHOICE MAYOR MINNEAPOLIS"].unique()


# In[59]:


def list_of_candidates(data):
    candidates = []
    for column in voting_columns:
        candidates_column = data[column].unique()
        for candidate in candidates_column:
            if candidate not in candidates:
                candidates.append(candidate)
                
    return candidates


# In[62]:


candidates = list_of_candidates(data)
candidates


# In[51]:


#sums
initial_first_place_votes = data[voting_columns[0]].value_counts()


# In[54]:


threshold = 80101/(1+1)
print(threshold)


# In[48]:


# Convert DataFrame to dictionary
data_dict = data[voting_columns[0]].value_counts().to_dict()


# In[97]:


def votes_dict(data):
    votes={}
    candidates = list_of_candidates(data)
    first_round_dict = data[voting_columns[0]].value_counts().to_dict()
    for c in candidates: 
        if c in first_round_dict:
            votes[c] = first_round_dict[c]
        else:
            votes[c] = 0
    return votes
      

        
    
    
    


# In[106]:


votes = votes_dict(data)
print(votes)


# In[110]:


def threshold_check(data, threshold):
    votes_dictionary_og = votes_dict(data)
    for candidate in votes_dictionary_og.values():
        if candidate >= threshold:
            return candidate

candidate= threshold_check(data, threshold)

#if candidate is None:
  #  then #call stv function 


# In[114]:


votes_dictionary_og = votes_dict(data)
print(votes_dictionary_og)
lowest_value = min(votes_dictionary_og.values())
print(lowest_value)

    


# In[ ]:


# Transfer method functions
#cand is candidate who votes are getting transferred,  ballot_list is just data, win_lose is just a paramter that decided if you are winning or losing i guess and cutoff is ithe threshold
def stv_transfer(self, cand, ballot_list, win_lose, cutoff):
    remove_cand = self.remove_cand
    if win_lose == 'lose':
        remove_cand(cand, ballot_list)
    else:
        cand_ballots_index = []
        single_cand_ballots_index = []
        for n, ballot in enumerate(ballot_list):
            if ballot[0] == cand and len(ballot) == 1:
                single_cand_ballots_index.append(n)
            elif ballot[0] == cand and len(ballot) >1:
                cand_ballots_index.append(n)

        rand_winners1 = random.sample(single_cand_ballots_index, min(int(cutoff), len(single_cand_ballots_index)))
        rand_winners2 = random.sample(cand_ballots_index, int(cutoff)- len(rand_winners1))
        rand_winners = rand_winners1 + rand_winners2

        #remove winning ballots from simulation
        for index in sorted(rand_winners, reverse = True):
            del ballot_list[index]

        #remove candidate from rest of ballots
        remove_cand(cand, ballot_list)



    

