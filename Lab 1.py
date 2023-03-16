
# coding: utf-8

# ## ROLL : 225229113

# # 1. Read and display the files of tabular data

# ## Printing properties like Size,shape,dimensions

# In[ ]:


print("Size=",f.size)


# In[ ]:


print("Shape=",f.shape)


# In[ ]:


print("ndim=",f.ndim)


# In[ ]:


print("ndim of fouls=",f["fouls"].ndim)


# ## Visualizing data files

# In[ ]:


import seaborn as a
g=a.pairplot(f,kind="reg")


# In[ ]:


f.plot(kind="bar")


# In[ ]:


f.plot(kind="hist")


# In[ ]:


f.plot.scatter(x="games",y="goals")


# In[ ]:


from matplotlib import pyplot as plt
teams = ['Argentina', 'Canada', 'France', 'Morocco', ' Portugal']
won = [74, 43, 38, 51, 50]
fig = plt.figure(figsize =(8,8))
plt.pie(won,labels = teams)


# # "TSV" — tab-separated values (.tsv)

# In[ ]:


import pandas as pd 
df = pd.read_csv('FIFAtsv.txt',sep = '\t')
print(df)


# # “ARFF” - Attribute-Relation File Format (.arff)

# In[ ]:


import pandas as pd
file=pd.read_csv('FIFA dataset.arff',sep='\t')
file.head()


# # 2. Read and display the spreadsheet files

# # "XLS" — Excel spreadsheet (.xls)
# 

# In[ ]:


import pandas as pd
file=("FIFA xlsdataset.xls")
a=pd.read_excel(file)
a


# # "XLSX" — Excel spreadsheet (.xlsx)
# 

# In[ ]:


import pandas as pd
file=("FIFA xlsxdataset.xlsx")
a=pd.read_excel(file)
a


# # "ODS" — OpenDocument spreadsheet (.ods)

# In[ ]:


pip install odfpy


# In[ ]:


import pandas as pd
file=('FIFA odsdataset.ods')
a=pd.read_excel(file)
a


# # "DIF" — VisiCalc data interchange format (.dif)

# In[ ]:


import pandas as pd 
txt = open('FIFA difdataset.dif', 'rb').read()
print(txt)  


# # 3. Read and display the files in interchange data formats

# # “HTML” – Hypertext Markup Language (.html)

# In[ ]:


f=open("FIFA htmldataset.html")


# # "JSON" — JavaScript Object Notation (.json)

# In[ ]:


import json
with open('FIFA jsondataset.json') as f:
    a = json.load(f)
print(a)


# # 4. Read and display the data files

# # PKL – Pickle files

# In[ ]:


import pickle
a = ['abi','hari','apar']
b = []
with open("testPickleFile", 'wb') as f:
    pickle.dump(a, f)   
with open("testPickleFile", 'rb') as f:
    b = pickle.load(f)
print(b)    


# # Zip

# In[ ]:


from zipfile import ZipFile
file = 'FIFA zip.zip'
with ZipFile(file, 'r') as zip:
    zip.printdir()
    zip.extractall()

