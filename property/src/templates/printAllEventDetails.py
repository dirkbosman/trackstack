import yaml
import pandas as pd
import numpy as np

from IPython.display import display
import pandas as pd
from pandas import DataFrame

with open(r'/....') as file:
  documents = yaml.full_load(file)
  a_list = []
  a_vals = []
  a_items = []

  for item, doc in documents.items():
    for val in doc['parameters']:
      a_items.append(item)
      a_vals.append(val)
      a_list.extend(doc)
  
  itemz = list(set(a_items))
  itemz.sort()
  res = list(set(a_list))
  res.sort()
  a_vals=list(set(a_vals))
  a_vals.sort()

  print("--------------------------")
  print ("Events_Count: " + str(len(itemz)))
  print(itemz)
  print("--------------------------")
  print ("#Categories_Count: " + str(len(res)))
  print(res)
  print("--------------------------")
  print ("#Parameters_Count: " + str(len(a_vals)))
  print(a_vals)
  print("--------------------------")
  
  df = pd.DataFrame(itemz,columns=['Events'])
  df.head(10)
  display(df)
  
  