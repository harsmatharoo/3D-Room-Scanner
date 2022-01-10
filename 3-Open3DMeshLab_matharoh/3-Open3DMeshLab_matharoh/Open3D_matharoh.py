# Name - Harsahib Matharoo
# Student ID - 400185871
#Python Version - 3.8.3


import numpy 
import open3d as o3d

if __name__=="__main__":

    #open the xyz file that was created before, and read the data

    x =open('ToFdata4.xyz','r')
    points_xyz = x.read()
    x.close()

 
# point cloud is now being created from the points that were acquired


    pcd=o3d.io.read_point_cloud('ToFdata4.xyz',format='xyz')
    print(pcd)
    print(numpy.asarray(pcd.points))
    o3d.visualization.draw_geometries([pcd])
    
