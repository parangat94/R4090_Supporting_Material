

import netCDF4
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

fig, axes = plt.subplots(2, 2)


axes[0,0].set_title("Mean Zonal Wind Speeds (m/s) \n at 250 hPa for Months: Dec Jan Feb")
#ax.axis('off')

axes[0,1].set_title("Mean Zonal Wind Speeds (m/s) \n at 250 hPa for Months: Mar Apr May")

axes[1,0].set_title("Mean Zonal Wind Speeds (m/s) \n at 250 hPa for Months: Jun Jul Aug")

axes[1,1].set_title("Mean Zonal Wind Speeds (m/s) \n at 250 hPa for Months: Sep Oct Nov")


#DJF

m = Basemap(projection = 'merc',llcrnrlon = 0.,llcrnrlat=-70.,urcrnrlon=360.,urcrnrlat=60., ax = axes[0,0])
m.drawmapboundary (fill_color ='White', zorder =0)
m.drawcoastlines()
m.drawcountries (linewidth = 2.0)
m.drawmeridians(np.arange(-180, 180, 30), color='0.25', rotation = 35,linewidth=0.5, labels=[False,False,False,True ])
m.drawparallels(np.arange(-70, 60, 15), color='0.25', linewidth=0.5, labels=[True,True,False,False])
f = netCDF4.Dataset('uwnd.mon.ltm.nc', 'r')



#Time averaging 250 hPa temperatures  over December, January and February
uwnd250 = f.variables ['uwnd'][:,8,:,:] # bringing all times in
lon = f.variables['lon'][:]
lat = f.variables['lat'][:]
DJF_mean = np.zeros((73,144))
# denote winter months (DJF)
DJF = np.array([0,1,11]) # the months of interest Can need to average all points over space and Fme (loop).


#Time averaging 250 hPa zonal winds  over December, January and February
for i in range(0,73):
    for j in range(0,144):
        DJF_mean[i,j] = np.mean(uwnd250[DJF,i,j])
lons,lats = np.meshgrid(lon,lat)
x,y = m(lons,lats)
cs = m.contourf(x,y,DJF_mean,levels = np.arange(-30,30,5))
cbar = m.colorbar(cs,location='right',pad='25%')
#plt.clabel(cs, fmt='%.0f', inline = True)
#cs = m.contour(x,y,DJF_mean,levels = np.arange(-30,30,5), colors = 'black')



#MAM
m = Basemap(projection = 'merc',llcrnrlon = 0.,llcrnrlat=-70.,urcrnrlon=360.,urcrnrlat=60., ax = axes[0,1])
m.drawmapboundary (fill_color ='White', zorder =0)
m.drawcoastlines()
m.drawcountries (linewidth = 2.0)
m.drawmeridians(np.arange(-180, 180, 30), color='0.25', linewidth=0.5, rotation = 35, labels=[False,False,False,True ])
m.drawparallels(np.arange(-70, 60, 15), color='0.25', linewidth=0.5, labels=[True,True,False,False])
f = netCDF4.Dataset('uwnd.mon.ltm.nc', 'r')


#Time averaging 250 hPa temperatures  over December, January and February
uwnd250 = f.variables ['uwnd'][:,8,:,:] # bringing all times in
lon = f.variables['lon'][:]
lat = f.variables['lat'][:]
MAM_mean = np.zeros((73,144))

MAM = np.array([2,3,4]) # the months of interest Can need to average all points over space and Fme (loop).


#Time averaging 250 hPa zonal winds  over MAM
for i in range(0,73):
    for j in range(0,144):
        MAM_mean[i,j] = np.mean(uwnd250[MAM,i,j])
lons,lats = np.meshgrid(lon,lat)
x,y = m(lons,lats)
cs = m.contourf(x,y,MAM_mean,levels = np.arange(-30,30,5))
cbar = m.colorbar(cs,location='right',pad='25%')
#plt.clabel(cs, fmt='%.0f', inline = True)
#cs = m.contour(x,y,MAM_mean,levels = np.arange(-30,30,5), colors = 'black')



#JJA
m = Basemap(projection = 'merc',llcrnrlon = 0.,llcrnrlat=-70.,urcrnrlon=360.,urcrnrlat=60., ax = axes[1,0])
m.drawmapboundary (fill_color ='White', zorder =0)
m.drawcoastlines()
m.drawcountries (linewidth = 2.0)
m.drawmeridians(np.arange(-180, 180, 30), color='0.25', linewidth=0.5, rotation = 35, labels=[False,False,False,True ])
m.drawparallels(np.arange(-70, 60, 15), color='0.25', linewidth=0.5, labels=[True,True,False,False])
f = netCDF4.Dataset('uwnd.mon.ltm.nc', 'r')

#Time averaging 250 hPa temperatures  over JJA
uwnd250 = f.variables ['uwnd'][:,8,:,:] # bringing all times in
lon = f.variables['lon'][:]
lat = f.variables['lat'][:]
JJA_mean = np.zeros((73,144))

JJA = np.array([5,6,7]) # the months of interest Can need to average all points over space and Fme (loop).


#Time averaging 250 hPa zonal winds  over December, January and February
for i in range(0,73):
    for j in range(0,144):
        JJA_mean[i,j] = np.mean(uwnd250[JJA,i,j])
lons,lats = np.meshgrid(lon,lat)
x,y = m(lons,lats)
cs = m.contourf(x,y,JJA_mean,levels = np.arange(-30,30,5))
cbar = m.colorbar(cs,location='right',pad='25%')
#plt.clabel(cs, fmt='%.0f', inline = True)
#cs = m.contour(x,y,JJA_mean,levels = np.arange(-30,30,5), colors = 'black')


#SON
m = Basemap(projection = 'merc',llcrnrlon = 0.,llcrnrlat=-70.,urcrnrlon=360.,urcrnrlat=60., ax = axes[1,1])
m.drawmapboundary (fill_color ='White', zorder =0)
m.drawcoastlines()
m.drawcountries (linewidth = 2.0)
m.drawmeridians(np.arange(-180, 180, 30), color='0.25', linewidth=0.5, rotation = 35, labels=[False,False,False,True ])
m.drawparallels(np.arange(-70, 60, 15), color='0.25', linewidth=0.5, labels=[True,True,False,False])
f = netCDF4.Dataset('uwnd.mon.ltm.nc', 'r')

#Time averaging 250 hPa temperatures  over JJA
uwnd250 = f.variables ['uwnd'][:,8,:,:] # bringing all times in
lon = f.variables['lon'][:]
lat = f.variables['lat'][:]
SON_mean = np.zeros((73,144))

SON = np.array([8,9,10]) # the months of interest Can need to average all points over space and Fme (loop).


#Time averaging 250 hPa zonal winds  over December, January and February
for i in range(0,73):
    for j in range(0,144):
        SON_mean[i,j] = np.mean(uwnd250[SON,i,j])
lons,lats = np.meshgrid(lon,lat)
x,y = m(lons,lats)
cs = m.contourf(x,y,SON_mean,levels = np.arange(-30,30,5))
cbar = m.colorbar(cs,location='right',pad='25%')
#plt.clabel(cs, fmt='%.0f', inline = True)
#cs = m.contour(x,y,SON_mean,levels = np.arange(-30,30,5), colors = 'black')

fig.subplots_adjust(hspace=.5)



#plt.title('average 850 hPa temperatures for February')

plt.xticks(rotation = '70')
plt.savefig('season_200winds.pdf')
#plt.tight_layout()
#plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
plt.show()
f.close()
