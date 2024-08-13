import calendar
import time

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
    [0.0, 1.0, 0.0, 0.0],  # Y轴方向
    [0.0, 0.0, 1.0, 400.0],  # Z轴方向和位置
    [0.0, 0.0, 0.0, 1.0]
])

camera = pyrender.PerspectiveCamera(yfov=viewport_width / viewport_height, aspectRatio=1, znear=0.1, zfar=1000,
                                    name='camera1')
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

img_out_path = './out_file/brain.png'
# 保存图像
img.save(img_out_path)

# 清理
renderer.delete()

# 折线图
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('x')
plt.title('Sin Function')
# 保存为图片, 保存到项目下的 out文件夹
plt_file_path = './out_file/sin.png'
plt.savefig(plt_file_path)

from fpdf import FPDF, Align

pl = 0
pr = 0
pt = 0
pb = 0

posX = 20
posY = 20

pdf = FPDF(orientation="P", unit="pt", format="A4")
pdf.page_mode = "FULL_SCREEN"
pdf.add_font("NotoSansSC", fname="assets/NotoSansSC-VariableFont_wght.ttf")
pdf.set_font("NotoSansSC", "", 15)

pdf.add_page()

# header
pdf.set_xy(20, 20)

pdf.cell(h=20, text="近红外报告", center=True)
pdf.set_y(pdf.get_y() + 20)

# 增加 患者信息

pdf.cell(h=20, text="姓名")
pdf.cell(h=20, text="李白")

pdf.cell(h=20, text="性别")
pdf.cell(h=20, text="男")
pdf.set_y(pdf.get_y() + 20)

pdf.set_y(pdf.get_y() + 20)

scale = 0.2
pdf.image(name=img_out_path, x=pdf.get_x(), y=pdf.get_y(), w=viewport_width * scale, h=viewport_height * scale)
pdf.set_x(pdf.get_x() + viewport_width * scale)

pdf.image(name=plt_file_path, x=pdf.get_x(), y=pdf.get_y(), w=viewport_width * scale, h=viewport_height * scale)
pdf.set_y(pdf.get_y() + viewport_height * scale)
pdf.set_x(pdf.get_x() + viewport_width * scale)

pdf_out_path = f'./out_file/hello_world{time.time()}.pdf'
pdf.output(pdf_out_path)
