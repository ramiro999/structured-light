import open3d as o3d

# Cargar el archivo .ply
ply = o3d.io.read_point_cloud("pcd.ply")

# Visualizar el archivo .ply
o3d.visualization.draw_geometries([ply])