from matplotlib import pyplot as plt

volkswagon_subbrands = ["Audi","Bently","Buggati","ducati","Lamborgini","porshe","seat","skoda","volkswagon_commercial","scania"]

sale_value = [7.6,5.6,4.5,5.4,6.1,3.7,16.3,15.6,27.9,14.5]

plt.pie(sale_value,labels=volkswagon_subbrands,autopct='%1.1f%%')

plt.axis('equal')

plt.show()