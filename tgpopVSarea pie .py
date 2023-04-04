from matplotlib import pyplot as plt

telangana_districts = ["Adilabad","Kothagudem","Hyderabad","jagitial","Jangaon","bhupalapally","gadwal","kamareddy","karimnagar","khammam","Asifabad","mahabubabad","mahabubnagar","macherial","medak","medchal","mulugu","nagarkurnool","narayanapet","nalgonda","nirmal","nizambad","peddapali","sircilla","rangareddy","sangareddy","siddipet","suryapet","vikarabad","wanaparthy","warangal_rural","WARANGAL_URBAN","Yadadri"]

area_in_sqkms = [4153,7483,217,2419,2188,6175,2928,3652,2128,4361,4878,2877,5285,4016,2786,1084,3881,6545,7122,3845,4288,2236,2019,5031,4403,3632,3607,3386,2152,2175,1309,3092]

plt.pie(area_in_sqkms,autopct='%0.1f%%')

plt.legend(telangana_districts)

plt.show()