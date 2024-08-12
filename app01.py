import trimesh
import pyrender
fuze_trimesh = trimesh.load('zuhe1.glb')
scene = pyrender.Scene.from_trimesh_scene(fuze_trimesh)

pyrender.Viewer(scene, use_raymond_lighting=True)
