# import libraries

import numpy as np

import my_function as func

import matplotlib.pyplot as plt

# specify the url

url = 'https://kawalpemilu.org/#pileg:0'

soup = func.getData(url)



# find results within table

results = soup.find('table',{'class':'table'})

rows = results.find_all('tr',{'class':'row'})
print(results)

list_wilayah = []

pdi = []

gerindra = []



# print(rows)

for r in rows:

    # find all columns per result

    data = r.find_all('td')

    # check that columns have data

    if len(data) == 0:

        continue

    # write columns to variables

    wilayah = data[1].find('a').getText()

    satu = data[9].getText()
    dua = data[15].getText()

    # Remove decimal point

    satu = satu.replace('.','')

    dua = dua.replace('.','')

    # Cast Data Type Integer

    satu = int(satu)

    dua = int(dua)

    list_wilayah.append(wilayah)

    pdi.append(satu)

    gerindra.append(dua)



# Convert to numpy

np_wilayah = np.array(list_wilayah)

np_pdi= np.array(pdi)

np_gerindra= np.array(gerindra)



# plot data

fig,ax = plt.subplots(figsize=(10,5))

# fig,ax = plt.subplots()

# print(ax)

pos = list(range(len(np_pdi)))

width = 0.25



# print(ind-width/2)



ax.bar(pos,np_pdi,width,color='red',label='PDI')

ax.bar([p + width for p in pos],np_gerindra,width,color='yellow',label='GERINDRA')

# ax.set_xticks(ind)

ax.set_xticks([p + 0.5 * width for p in pos])

ax.set_xticklabels(np_wilayah)

# # Naming label

plt.xlabel('provinsi')

plt.ylabel('perolehan suara')



# # styling x,y value

plt.yticks(np.arange(np_pdi.min(),np_pdi.max(),4000000))

plt.xticks(rotation='vertical',ha='right')

plt.legend(loc='upper right')

plt.yscale('linear')



plt.show()