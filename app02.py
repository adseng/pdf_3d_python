import trimesh
import pyrender
from PIL import Image
import numpy as np

# 加载 .glb 文件
fuze_trimesh = trimesh.load('zuhe1.glb')
scene = pyrender.Scene.from_trimesh_scene(fuze_trimesh)

viewport_width = 800
viewport_height = 800

# 设置相机位置
# 相机在模型正上方的位置和朝向
camera_pose = np.array([
    [1.0, 0.0, 0.0, 0.0],  # X轴方向
    [0.0, 1.0, 0.0, 200.0],  # Y轴方向
    [0.0, 0.0, 1.0, 400.0],  # Z轴方向和位置
    [0.0, 0.0, 0.0, 1.0]
])

camera = pyrender.PerspectiveCamera(yfov=viewport_width / viewport_height, aspectRatio=1, znear=0.1, zfar=1000, name='camera1')
scene.add(camera, pose=camera_pose)

# 设置光照
# 不设置光照，渲染出来的模型没有颜色

light = pyrender.DirectionalLight(color=[1.0, 1.0, 1.0], intensity=3.0)
scene.add(light, pose=camera_pose)

scene.get_nodes(name='camera1')

# 创建渲染器
renderer = pyrender.OffscreenRenderer(viewport_width=viewport_width, viewport_height=viewport_height)

# 渲染场景
color, _ = renderer.render(scene)


# 将 numpy 数组转换为 PIL 图像对象
img = Image.fromarray(color)

# 保存图像
img.save('output.png')

# 清理
renderer.delete()
