from matplotlib import pyplot as plt

#india population 
RELIGION = ["HINDU","MUSLIM","CHRISTIAN","SIKH","JAIN","BUDDIST","UNAVAILABLE","MISC"]

PERCENTAGE = [85.09,12.92,1.87,0.05,0.72,0.16,0.27,0.02]

plt.pie(PERCENTAGE,autopct='%0.1f%%', labels=RELIGION)

plt.legend(RELIGION)

plt.show()
