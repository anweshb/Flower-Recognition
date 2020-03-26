import os

data_dir = "E:\\Machine Learning\\flowers-recognition\\flowers"
flower_names = os.listdir(data_dir)

flower_dirs = [data_dir+"\\"+flower for flower in flower_names]  #making a list of all the individual flower directories

flower_dict = dict(zip(flower_names,len(os.listdir(flower_dirs))))

print(flower_dict)