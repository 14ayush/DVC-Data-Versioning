#try to make the csv file using the os module
import pandas as pd 
import os

data={'Name':['Ayush','Abhinav','Akash','Akshay','Jonny','Mayank'],
      'Age':['23','18','26','24','35','32'],
      'City':['Meerut','Noida','Delhi','Issar','Punjab','Lucknow']}
df=pd.DataFrame(data)

data_dir='data'
os.makedirs(data_dir,exist_ok=True)
file_path=os.path.join(data_dir,'Sample.csv')
df.to_csv(file_path,index=False)
print(f"The csv file created Successfully at :{file_path}")
