import os
from statistics import mean

data_dir = "E:\\Machine Learning\\flowers-recognition\\flowers"
flower_names = os.listdir(data_dir)

flower_dirs = [data_dir+"\\"+flower for flower in flower_names]  #making a list of all the individual flower directories

flower_len = [len(os.listdir(flower)) for flower in flower_dirs] #making a list of the number of pictures in each flower sub-directory

flower_dict = dict(zip(flower_names,flower_len))   #dictionary of number of pictures of each corresponding flower

avg = round(mean(flower_len))

print(avg)

