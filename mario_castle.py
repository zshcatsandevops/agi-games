from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Basic window setup
window.borderless = False
window.fullscreen = False
window.color = color.rgb(135, 206, 235)  # soft sky blue fallback

# =========================================================
# GROUND + WORLD BASE
# =========================================================
ground = Entity(
    model='plane',
    scale=200,
    texture='grass',
    texture_scale=(20, 20),
    collider='box'
)

# Moat (blue water around castle)
moat = Entity(
    model='plane',
    scale=80,
    position=(0, 0.1, 30),
    color=color.blue.tint(-0.3),
    texture='shore',  # shore texture included in Ursina base
    double_sided=True
)

# =========================================================
# CASTLE STRUCTURE
# =========================================================
main_base = Entity(
    model='cube',
    scale=(60, 10, 60),
    position=(0, 5, 30),
    texture='brick',
    texture_scale=(8, 2),
    color=color.rgb(255, 240, 220),
    collider='box'
)

main_body = Entity(
    model='cube',
    scale=(45, 35, 45),
    position=(0, 27.5, 30),
    texture='brick',
    texture_scale=(6, 4),
    color=color.rgb(255, 245, 235),
    collider='box'
)

# Central tower
central_tower = Entity(
    model=Cylinder(resolution=16),  # uses built-in mesh
    scale=(12, 50, 12),
    position=(0, 35, 30),
    texture='brick',
    texture_scale=(4, 8),
    color=color.rgb(250, 240, 230),
    collider='box'
)

central_roof = Entity(
    model=Cone(resolution=16),
    scale=(16, 25, 16),
    position=(0, 72, 30),
    color=color.red
)

# =========================================================
# SIDE TOWERS
# =========================================================
tower_positions = [(-20, 20), (20, 20), (-20, 40), (20, 40)]
for x, z in tower_positions:
    Entity(
        model=Cylinder(resolution=16),
        scale=(6, 30, 6),
        position=(x, 20, 30 + z - 30),
        texture='brick',
        texture_scale=(2, 6),
        color=color.rgb(250, 240, 230),
        collider='box'
    )
    Entity(
        model=Cone(resolution=16),
        scale=(9, 15, 9),
        position=(x, 42, 30 + z - 30),
        color=color.red.tint(-0.2)
    )

# =========================================================
# ENTRANCE + BRIDGE
# =========================================================
entrance = Entity(
    model='cube',
    scale=(15, 20, 10),
    position=(0, 15, 55),
    texture='brick',
    texture_scale=(3, 3),
    color=color.rgb(255, 240, 220),
    collider='box'
)

bridge = Entity(
    model='cube',
    scale=(12, 1, 40),
    position=(0, 5.5, 10),
    texture='white_cube',
    color=color.rgb(150, 100, 50),
    collider='box'
)

for z in [-9, 29]:
    Entity(
        model='cube',
        scale=(12, 2, 1),
        position=(0, 7, z),
        color=color.gray,
        collider='box'
    )

# =========================================================
# FLAGS
# =========================================================
flag_positions = [(0, 85, 30), (-20, 47, 20), (20, 47, 20), (-20, 47, 40), (20, 47, 40)]
for x, y, z in flag_positions:
    Entity(model='plane', scale=(3, 2, 1), position=(x, y, z), color=color.red, double_sided=True)
    Entity(model='cube', scale=(0.2, 4, 0.2), position=(x, y-2, z), color=color.gray)

# =========================================================
# TREES
# =========================================================
tree_positions = [(-40, 10), (40, 10), (-40, 50), (40, 50), (-60, 30), (60, 30)]
for x, z in tree_positions:
    Entity(model=Cylinder(resolution=10), scale=(1.5, 8, 1.5), position=(x, 4, z), color=color.brown, collider='box')
    Entity(model='sphere', scale=(6, 8, 6), position=(x, 12, z), color=color.green)

# =========================================================
# PLAYER + CAMERA
# =========================================================
player = FirstPersonController(
    position=(0, 10, -30),
    speed=20,
    gravity=1.0,
    jump_height=2.5
)

Sky()

Text(
    text="Peach's Castle — WASD to move, Mouse to look",
    position=(-0.8, 0.4),
    scale=1.2,
    color=color.black
)

camera.rotation_x = -10

app.run()
