from matplotlib import pyplot as plt

prog_languages = ["javascript","python","java","c","php","c#","visualdevtools","swift","kotlin","go"]

users = [12.4,9,8.2,6.3,6.1,6,2.8,2.4,2.3,1.5]

explode = (0,0.1,0,0,0,0,0,0,0,0)

plt.pie(users,labels = prog_languages,explode = explode, autopct='%1.1f%%',startangle=90,pctdistance=0.85)

centre_circle = plt.Circle((0,0),0.8,fc = 'white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)


plt.axis('equal')

plt.tight_layout()

plt.show()