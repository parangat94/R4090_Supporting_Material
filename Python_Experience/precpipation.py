from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap
from datetime import date
import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np


fname = 'precip.mon.total.v401.nc'

#South Pole
South = Basemap(projection='spstere', boundinglat=10, lon_0=270)

#North Pole
North = Basemap(projection='npstere',boundinglat=10,lon_0=270)


#Africa
Africa = Basemap(projection='merc',llcrnrlon = -19, llcrnrlat = -35, urcrnrlon = 52, urcrnrlat = 39)

#USA
US = Basemap(projection='merc',llcrnrlon = 230, llcrnrlat = 25, urcrnrlon = 300, urcrnrlat = 52)


#Asia
Asia = Basemap(projection='merc',llcrnrlon = 73, llcrnrlat = 0, urcrnrlon = 129, urcrnrlat = 50)

#Precipitation file
f = nc.Dataset(fname, 'r')

#Print variable names for reference
for var in f.variables:
    print(var)



p = f.variables['precip'][:,:,:]

lat = f.variables['lat'][:]
lon = f.variables['lon'][:]
lons, lats = np.meshgrid(lon,lat)

x1, y1 = North(lons,lats)
x2, y2 = South(lons,lats)
x3, y3 = US(lons,lats)
x4, y4 = Africa(lons,lats)
x5, y5 = Asia(lons,lats)




clim = p[972:1332,:,:]




#Part A

p_avg = []

for i in range(0,360,12):
    avg = np.mean(clim[i:i+11,:,:], axis = 0)
    p_avg.append(avg)

#Find average for long and lat
#Mean Clim Period


climate = np.mean(p_avg, axis = 0)

#Part A

#N Pole

plt.figure()
North.drawmapboundary(fill_color = 'White', zorder = 0)
North.drawcoastlines()
North.drawcountries(linewidth = 1.0)
North.drawmeridians(np.arange(0,360,30), labels =[False,False,False,True])
North.drawparallels(np.arange(-90,90,30), labels =[True, True, False, False])

# C Bar
cs = North.contourf(x1, y1, climate, levels = np.arange(0,34,2))
cbar = North.colorbar(cs,location = 'bottom',pad = "25%", label = 'Precipitation (cm)')


plt.title('North Pole 1981-2010 Average Precipitation')
plt.savefig('NorthPole_Precip.png')

#S Pole
plt.figure()
South.drawmapboundary(fill_color = 'White', zorder = 0)
South.drawcoastlines()
South.drawcountries(linewidth = 1.0)
South.drawmeridians(np.arange(0,360,30), labels =[False,False,False,True])
South.drawparallels(np.arange(-90,90,30), labels =[True, True, False, False])

''' Color Bar '''
cs = South.contourf(x2, y2, climate, levels = np.arange(0,34,2))
cbar = South.colorbar(cs,location = 'bottom',pad = "25%", label = 'Precipitation (cm)')

''' Title and Save figure '''
plt.title('South Pole 1981-2010 Average Precipitation')
plt.savefig('SouthPole_Precip.png')

''' United States '''
plt.figure()
US.drawmapboundary(fill_color = 'White', zorder = 0)
US.drawcoastlines()
US.drawcountries(linewidth = 1.0)
US.drawstates()
US.drawmeridians(np.arange(0,360,30), labels = [False,False,False,True])
US.drawparallels(np.arange(-90,90,30), labels = [True, True, False, False])


cs = US.contourf(x3, y3, climate, levels = np.arange(0,30,2))
cbar = US.colorbar(cs,location = 'bottom',pad = "25%", label = 'Precipitation (cm)')


plt.title('United States 1981-2010 Average Precipitation')
plt.savefig('UnitedStates_Precip.png')

#Africa
plt.figure()
Africa.drawmapboundary(fill_color = 'White', zorder = 0)
Africa.drawcoastlines()
Africa.drawcountries(linewidth = 1.0)
Africa.drawstates()
Africa.drawmeridians(np.arange(0,360,30), labels = [False,False,False,True])
Africa.drawparallels(np.arange(-90,90,30), labels = [True, True, False, False])

''' Color Bar '''
cs = Africa.contourf(x4, y4, climate, levels = np.arange(0,30,2))
cbar = Africa.colorbar(cs,location =  'bottom',pad = "25%", label = 'Precipitation (cm)')

''' Title and Save figure '''
plt.title('Africa 1981-2010 Average Precipitation')
plt.savefig('Africa_Precip.png')

#Asia
plt.figure()
Asia.drawmapboundary(fill_color = 'White', zorder = 0)
Asia.drawcoastlines()
Asia.drawcountries(linewidth = 1.0)
Asia.drawstates()
Asia.drawmeridians(np.arange(0,360,30), labels = [False,False,False,True])
Asia.drawparallels(np.arange(-90,90,30), labels = [True, True, False, False])

''' Color Bar '''
cs = Asia.contourf(x5, y5, climate, levels = np.arange(0,38,2))
cbar = Asia.colorbar(cs,location = 'bottom',pad = "25%", label = 'Precipitation (cm)')

''' Title and Save figure '''
plt.title('Asia 1981-2010 Average Precipitation')
plt.savefig('Asia_Precip.png')




#B



''' Indexing for the wanted years: (1920, 1950, 1980, 2014) '''
prec1920 = p[240:252,:,:]
avg1920 = np.nanmean(prec1920, axis=0)

prec1950 = p[600:612,:,:]
avg1950 = np.nanmean(prec1950, axis=0)

prec1980 = p[960:972,:,:]
avg1980 = np.nanmean(prec1980, axis=0)

prec2014 = p[1368:1380,:,:]
avg2014 = np.nanmean(prec2014, axis=0)


#Anomalies

anom1920 = avg1920 - climate
anom1950 = avg1950 - climate
anom1980 = avg1980 - climate
anom2014 = avg2014 - climate

#N pole

plt.figure(figsize = (25,25))
plt.subplot(221)

North.drawmapboundary(fill_color = 'White', zorder = 0)
North.drawcoastlines()
North.drawcountries(linewidth = 1.0)
North.drawmeridians(np.arange(0,360,30), labels =[False,False,False,True])
North.drawparallels(np.arange(-90,90,30), labels =[True, True, False, False])

cs = North.contourf(x1, y1, anom1920, levels = np.arange(-12,12,1))
cbar = North.colorbar(cs,location='right',pad = "25%", label='Precipitation (cm)')

plt.title('1920 North Pole Precipitation Anomaly')



plt.subplot(222)

North.drawmapboundary(fill_color = 'White', zorder = 0)
North.drawcoastlines()
North.drawcountries(linewidth = 1.0)
North.drawmeridians(np.arange(0,360,30), labels =[False,False,False,True])
North.drawparallels(np.arange(-90,90,30), labels =[True, True, False, False])

cs = North.contourf(x1, y1, anom1950, levels = np.arange(-12,12,1))
cbar = North.colorbar(cs,location='right',pad = "25%", label='Precipitation (cm)')

plt.title('1950 North Pole Precipitation Anomaly')



plt.subplot(223)

North.drawmapboundary(fill_color = 'White', zorder = 0)
North.drawcoastlines()
North.drawcountries(linewidth = 1.0)
North.drawmeridians(np.arange(0,360,30), labels =[False,False,False,True])
North.drawparallels(np.arange(-90,90,30), labels =[True, True, False, False])

cs = North.contourf(x1, y1, anom1980, levels = np.arange(-12,12,1))
cbar = North.colorbar(cs,location='right',pad = "25%", label='Precipitation (cm)')

plt.title('1980 North Pole Precipitation Anomaly')





plt.subplot(224)

North.drawmapboundary(fill_color = 'White', zorder = 0)
North.drawcoastlines()
North.drawcountries(linewidth = 1.0)
North.drawmeridians(np.arange(0,360,30), labels =[False,False,False,True])
North.drawparallels(np.arange(-90,90,30), labels =[True, True, False, False])

cs = North.contourf(x1, y1, anom2014, levels = np.arange(-12,12,1))
cbar = North.colorbar(cs,location='right',pad = "25%", label='Precipitation (cm)')

plt.title('2014 North Pole Precipitation Anomaly')
plt.savefig('NorthPole_PrecipAnom.png')

'''*****************************************************************************'''
'''*****************************************************************************'''

''' South Pole '''

plt.figure(figsize=(25,25))
plt.subplot(221)

South.drawmapboundary(fill_color = 'White', zorder = 0)
South.drawcoastlines()
South.drawcountries(linewidth = 1.0)
South.drawmeridians(np.arange(0,360,30), labels =[False,False,False,True])
South.drawparallels(np.arange(-90,90,30), labels =[True, True, False, False])

cs = South.contourf(x2, y2, anom1920, levels = np.arange(-12,12,1))
cbar = South.colorbar(cs,location = 'bottom',pad = "25%", label = 'Precipitation (cm)')

plt.title('1920 South Pole Precipitation Anomaly')



plt.subplot(222)

South.drawmapboundary(fill_color = 'White', zorder = 0)
South.drawcoastlines()
South.drawcountries(linewidth = 1.0)
South.drawmeridians(np.arange(0,360,30), labels =[False,False,False,True])
South.drawparallels(np.arange(-90,90,30), labels =[True, True, False, False])

cs = South.contourf(x2, y2, anom1950, levels = np.arange(-12,12,1))
cbar = South.colorbar(cs,location='right',pad = "25%", label='Precipitation (cm)')

plt.title('1950 South Precipitation Anomaly')


plt.subplot(223)

South.drawmapboundary(fill_color = 'White', zorder = 0)
South.drawcoastlines()
South.drawcountries(linewidth = 1.0)
South.drawmeridians(np.arange(0,360,30), labels =[False,False,False,True])
South.drawparallels(np.arange(-90,90,30), labels =[True, True, False, False])

cs = South.contourf(x2, y2, anom1980, levels = np.arange(-12,12,1))
cbar = South.colorbar(cs,location='right',pad = "25%", label='Precipitation (cm)')

plt.title('1980 South Precipitation Anomaly')


plt.subplot(224)

South.drawmapboundary(fill_color = 'White', zorder = 0)
South.drawcoastlines()
South.drawcountries(linewidth = 1.0)
South.drawmeridians(np.arange(0,360,30), labels =[False,False,False,True])
South.drawparallels(np.arange(-90,90,30), labels =[True, True, False, False])

cs = South.contourf(x2, y2, anom2014, levels = np.arange(-12,12,1))
cbar = South.colorbar(cs,location='right',pad = "25%", label='Precipitation (cm)')

plt.title('2014 South Pole Precipitation Anomaly')
plt.savefig('SouthPole_PrecipAnom.png')

#USA

plt.figure(figsize=(25,25))
plt.subplot(221)

US.drawmapboundary(fill_color = 'White', zorder = 0)
US.drawcoastlines()
US.drawcountries(linewidth = 1.0)
US.drawmeridians(np.arange(0,360,30), labels =[False,False,False,True])
US.drawparallels(np.arange(-90,90,30), labels =[True, True, False, False])

cs = US.contourf(x3, y3, anom1920, levels = np.arange(-12,12,1))
cbar = US.colorbar(cs,location='right',pad = "25%", label='Precipitation (cm)')

plt.title('1920 United States Precipitation Anomaly')




plt.subplot(222)

US.drawmapboundary(fill_color = 'White', zorder = 0)
US.drawcoastlines()
US.drawcountries(linewidth = 1.0)
US.drawmeridians(np.arange(0,360,30), labels =[False,False,False,True])
US.drawparallels(np.arange(-90,90,30), labels =[True, True, False, False])

cs = US.contourf(x3, y3, anom1950, levels = np.arange(-12,12,1))
cbar = US.colorbar(cs,location='right',pad = "25%", label='Precipitation (cm)')

plt.title('1950 United States Precipitation Anomaly')


plt.subplot(223)

US.drawmapboundary(fill_color = 'White', zorder = 0)
US.drawcoastlines()
US.drawcountries(linewidth = 1.0)
US.drawmeridians(np.arange(0,360,30), labels =[False,False,False,True])
US.drawparallels(np.arange(-90,90,30), labels =[True, True, False, False])

cs = US.contourf(x3, y3, anom1980, levels = np.arange(-12,12,1))
cbar = US.colorbar(cs,location='right',pad = "25%", label='Precipitation (cm)')

plt.title('1980 United States Precipitation Anomaly')

'''*****************************************************************************'''

plt.subplot(224)

US.drawmapboundary(fill_color = 'White', zorder = 0)
US.drawcoastlines()
US.drawcountries(linewidth = 1.0)
US.drawmeridians(np.arange(0,360,30), labels =[False,False,False,True])
US.drawparallels(np.arange(-90,90,30), labels =[True, True, False, False])

cs = US.contourf(x3, y3, anom2014, levels = np.arange(-12,12,1))
cbar = US.colorbar(cs,location='right',pad = "25%", label='Precipitation (cm)')

plt.title('2014 United States Precipitation Anomaly')
plt.savefig('US_PrecipAnom.png')


#Africa

plt.figure(figsize=(25,25))
plt.subplot(221)

Africa.drawmapboundary(fill_color = 'White', zorder = 0)
Africa.drawcoastlines()
Africa.drawcountries(linewidth = 1.0)
Africa.drawmeridians(np.arange(0,360,30), labels =[False,False,False,True])
Africa.drawparallels(np.arange(-90,90,30), labels =[True, True, False, False])

cs = Africa.contourf(x4, y4, anom1920, levels = np.arange(-12,12,1))
cbar = Africa.colorbar(cs,location='right',pad = "25%", label='Precipitation (cm)')

plt.title('1920 Africa Precipitation Anomaly')



plt.subplot(222)

Africa.drawmapboundary(fill_color = 'White', zorder = 0)
Africa.drawcoastlines()
Africa.drawcountries(linewidth = 1.0)
Africa.drawmeridians(np.arange(0,360,30), labels =[False,False,False,True])
Africa.drawparallels(np.arange(-90,90,30), labels =[True, True, False, False])

cs = Africa.contourf(x4, y4, anom1950, levels = np.arange(-12,12,1))
cbar = Africa.colorbar(cs,location='right',pad = "25%", label='Precipitation (cm)')

plt.title('1950 Africa Precipitation Anomaly')



plt.subplot(223)

Africa.drawmapboundary(fill_color = 'White', zorder = 0)
Africa.drawcoastlines()
Africa.drawcountries(linewidth = 1.0)
Africa.drawmeridians(np.arange(0,360,30), labels =[False,False,False,True])
Africa.drawparallels(np.arange(-90,90,30), labels =[True, True, False, False])

cs = Africa.contourf(x4, y4, anom1980, levels = np.arange(-12,12,1))
cbar = Africa.colorbar(cs,location='right',pad = "25%", label='Precipitation (cm)')

plt.title('1980 Africa Precipitation Anomaly')

'''*****************************************************************************'''

plt.subplot(224)

Africa.drawmapboundary(fill_color = 'White', zorder = 0)
Africa.drawcoastlines()
Africa.drawcountries(linewidth = 1.0)
Africa.drawmeridians(np.arange(0,360,30), labels =[False,False,False,True])
Africa.drawparallels(np.arange(-90,90,30), labels =[True, True, False, False])

cs = Africa.contourf(x4, y4, anom2014, levels = np.arange(-12,12,1))
cbar = Africa.colorbar(cs,location='right',pad = "25%", label='Precipitation (cm)')

plt.title('2014 Africa Precipitation Anomaly')
plt.savefig('Africa_PrecipAnom.png')

# Asia

plt.figure(figsize=(25,25))
plt.subplot(221)

Asia.drawmapboundary(fill_color = 'White', zorder = 0)
Asia.drawcoastlines()
Asia.drawcountries(linewidth = 1.0)
Asia.drawmeridians(np.arange(0,360,30), labels =[False,False,False,True])
Asia.drawparallels(np.arange(-90,90,30), labels =[True, True, False, False])

cs = Asia.contourf(x5, y5, anom1920, levels = np.arange(-12,12,1))
cbar = Asia.colorbar(cs,location='right',pad = "25%", label='Precipitation (cm)')

plt.title('1920 Asia Precipitation Anomaly')



plt.subplot(222)

Asia.drawmapboundary(fill_color = 'White', zorder = 0)
Asia.drawcoastlines()
Asia.drawcountries(linewidth = 1.0)
Asia.drawmeridians(np.arange(0,360,30), labels =[False,False,False,True])
Asia.drawparallels(np.arange(-90,90,30), labels =[True, True, False, False])

cs = Asia.contourf(x5, y5, anom1950, levels = np.arange(-12,12,1))
cbar = Asia.colorbar(cs,location='right',pad = "25%", label='Precipitation (cm)')

plt.title('1950 Asia Precipitation Anomaly')



plt.subplot(223)

Asia.drawmapboundary(fill_color = 'White', zorder = 0)
Asia.drawcoastlines()
Asia.drawcountries(linewidth = 1.0)
Asia.drawmeridians(np.arange(0,360,30), labels =[False,False,False,True])
Asia.drawparallels(np.arange(-90,90,30), labels =[True, True, False, False])

cs = Asia.contourf(x5, y5, anom1980, levels = np.arange(-12,12,1))
cbar = Asia.colorbar(cs,location='right',pad = "25%", label='Precipitation (cm)')

plt.title('1980 Asia Precipitation Anomaly')



plt.subplot(224)

Asia.drawmapboundary(fill_color = 'White', zorder = 0)
Asia.drawcoastlines()
Asia.drawcountries(linewidth = 1.0)
Asia.drawmeridians(np.arange(0,360,30), labels =[False,False,False,True])
Asia.drawparallels(np.arange(-90,90,30), labels =[True, True, False, False])

cs = Asia.contourf(x5, y5, anom2014, levels = np.arange(-12,12,1))
cbar = Asia.colorbar(cs,location='right',pad = "25%", label='Precipitation (cm)')

plt.title('2014 Asia Precipitation Anomaly')
plt.savefig('Asia_PrecipAnom.png')
plt.show()
