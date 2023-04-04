from matplotlib import pyplot as plt

continent_names = ["Asia","Africa","North_america","South_america","Antarctica","Europe","Australia"]


continent_areas = [17.2,11.6,9.3,6.8,5.1,3.8,2.9]


plt.pie(continent_areas,labels=continent_names,autopct="%0.1f%%")

plt.axis('equal')

plt.show()