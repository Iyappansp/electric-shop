import os
import math
from PIL import Image, ImageDraw, ImageFilter

def draw_radial_gradient(draw, width, height, center_x, center_y, radius, color_center, color_outer):
    for r in range(radius, 0, -6):
        t = r / radius
        r_col = int(color_center[0] * (1 - t) + color_outer[0] * t)
        g_col = int(color_center[1] * (1 - t) + color_outer[1] * t)
        b_col = int(color_center[2] * (1 - t) + color_outer[2] * t)
        a_col = int(color_center[3] * (1 - t) + color_outer[3] * t) if len(color_center) > 3 else 255
        draw.ellipse([center_x - r, center_y - r, center_x + r, center_y + r], fill=(r_col, g_col, b_col, a_col))

def create_studio(width=1280, height=960, c1=(0, 240, 255), c2=(147, 51, 234), bg=(10, 14, 24)):
    img = Image.new("RGBA", (width, height), (*bg, 255))
    glow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    draw_radial_gradient(gdraw, width, height, int(width * 0.35), int(height * 0.4), int(min(width, height) * 0.65), (*c1, 100), (*bg, 0))
    draw_radial_gradient(gdraw, width, height, int(width * 0.65), int(height * 0.6), int(min(width, height) * 0.65), (*c2, 90), (*bg, 0))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=40))
    img.alpha_composite(glow)
    draw = ImageDraw.Draw(img)
    for x in range(0, width, 60):
        draw.line([(x, 0), (x, height)], fill=(255, 255, 255, 6), width=1)
    for y in range(0, height, 60):
        draw.line([(0, y), (width, y)], fill=(255, 255, 255, 6), width=1)
    return img

def save_img(img, filepath, w=640, h=480):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    img.resize((w, h), Image.Resampling.LANCZOS).save(filepath, "PNG", quality=95)
    print(f"Generated Detailed Image: {filepath}")

# 1. apple_product_1: AuraPhone Pro Max (Back view with Triple Camera system)
def gen_apple_1(fp):
    img = create_studio(1280, 960, (255, 255, 255), (59, 130, 246), bg=(8, 12, 20))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 480
    
    # Phone main body (Titanium Gold chassis)
    draw.rounded_rectangle([cx-160, cy-290, cx+160, cy+290], radius=48, fill=(28, 32, 40, 255), outline=(198, 180, 150, 220), width=6)
    
    # Camera Island (Glass panel raised)
    draw.rounded_rectangle([cx-135, cy-265, cx-15, cy-145], radius=28, fill=(20, 24, 30, 255), outline=(220, 200, 170, 80), width=2)
    
    # Triple Lenses
    lenses = [(cx-75, cy-230), (cx-75, cy-180), (cx-110, cy-205)]
    for lx, ly in lenses:
        # Outer lens metal rim
        draw.ellipse([lx-20, ly-20, lx+20, ly+20], fill=(35, 38, 45, 255), outline=(198, 180, 150, 200), width=3)
        # Inner lens dark glass
        draw.ellipse([lx-14, ly-14, lx+14, ly+14], fill=(8, 10, 15, 255), outline=(50, 50, 60, 255), width=2)
        # Deep lens reflection (sensor glow)
        draw.ellipse([lx-6, ly-6, lx+2, ly+2], fill=(0, 180, 255, 140))
        draw.ellipse([lx+3, ly+3, lx+8, ly+8], fill=(255, 255, 255, 180)) # White spec reflection
        
    # LiDAR sensor & Flash
    draw.ellipse([cx-42, cy-195, cx-30, cy-183], fill=(45, 45, 55, 255)) # LiDAR
    draw.ellipse([cx-45, cy-230, cx-33, cy-218], fill=(255, 255, 220, 255), outline=(255, 255, 255, 255), width=1) # Flash
    
    # Apple Logo representation (Minimalist logo representation)
    draw.ellipse([cx-25, cy+10, cx+25, cy+60], fill=(198, 180, 150, 180))
    draw.chord([cx-25, cy-5, cx+25, cy+45], start=0, end=180, fill=(8, 12, 20, 255))
    draw.ellipse([cx+5, cy-15, cx+20, cy+5], fill=(198, 180, 150, 180)) # Leaf
    
    save_img(img, fp)

# 2. apple_product_2: AirWave Buds 2 (Earbuds with charging case)
def gen_apple_2(fp):
    img = create_studio(1280, 960, (59, 130, 246), (236, 72, 153), bg=(10, 14, 24))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 520
    
    # Case Body (glossy white with gradients)
    draw.rounded_rectangle([cx-120, cy-50, cx+120, cy+120], radius=48, fill=(240, 240, 245, 255), outline=(210, 210, 215, 255), width=4)
    # Lid split line
    draw.line([(cx-120, cy-10), (cx+120, cy-10)], fill=(170, 170, 175, 255), width=3)
    # Status green LED
    draw.ellipse([cx-5, cy+30, cx+5, cy+40], fill=(0, 240, 100, 255), outline=(255, 255, 255, 100), width=1)
    
    # Earbud Left (floating next to it)
    elx, ely = cx-190, cy-100
    draw.ellipse([elx-22, ely-22, elx+22, ely+22], fill=(250, 250, 255, 255), outline=(210, 210, 215, 255), width=2) # head
    draw.rounded_rectangle([elx-8, ely, elx+8, ely+65], radius=6, fill=(250, 250, 255, 255), outline=(210, 210, 215, 255), width=2) # stem
    draw.ellipse([elx+10, ely-12, elx+26, ely+4], fill=(215, 215, 220, 255)) # silicone tip
    draw.line([(elx-4, ely+58), (elx+4, ely+58)], fill=(180, 180, 185, 255), width=2) # metal contact bottom
    
    # Earbud Right
    erx, ery = cx+190, cy-100
    draw.ellipse([erx-22, ery-22, erx+22, ery+22], fill=(250, 250, 255, 255), outline=(210, 210, 215, 255), width=2)
    draw.rounded_rectangle([erx-8, ery, erx+8, ery+65], radius=6, fill=(250, 250, 255, 255), outline=(210, 210, 215, 255), width=2)
    draw.ellipse([erx-26, ery-12, erx-10, ery+4], fill=(215, 215, 220, 255))
    draw.line([(erx-4, ery+58), (erx+4, ery+58)], fill=(180, 180, 185, 255), width=2)
    
    save_img(img, fp)

# 3. apple_product_3: ChronoLux Premium (Luxury round smartwatch)
def gen_apple_3(fp):
    img = create_studio(1280, 960, (245, 158, 11), (255, 255, 255), bg=(8, 10, 16))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 480
    
    # Strap links (Premium titanium link band)
    draw.rounded_rectangle([cx-60, cy-320, cx+60, cy+320], radius=12, fill=(38, 42, 50, 255), outline=(80, 85, 95, 255), width=2)
    for ly in range(cy-300, cy+320, 45):
        if abs(ly - cy) > 130:
            draw.line([(cx-60, ly), (cx+60, ly)], fill=(70, 75, 85, 255), width=3)
            
    # Watch round case (Metallic titanium gold)
    draw.ellipse([cx-170, cy-170, cx+170, cy+170], fill=(24, 28, 35, 255), outline=(210, 185, 110, 255), width=10)
    
    # Inner dark display screen
    draw.ellipse([cx-150, cy-150, cx+150, cy+150], fill=(10, 12, 16, 255))
    
    # Screen dial dial ticks (12 hours)
    for i in range(12):
        angle = math.radians(i * 30)
        x1 = cx + int(132 * math.sin(angle))
        y1 = cy - int(132 * math.cos(angle))
        x2 = cx + int(144 * math.sin(angle))
        y2 = cy - int(144 * math.cos(angle))
        draw.line([(x1, y1), (x2, y2)], fill=(210, 185, 110, 255), width=3)
        
    # Complications (small dial graphics on watch screen)
    draw.ellipse([cx-40, cy-90, cx+40, cy-10], outline=(100, 110, 130, 200), width=2) # Top sub-dial
    draw.line([(cx, cy-50), (cx+25, cy-70)], fill=(0, 240, 255, 255), width=2)
    
    # Hands (Hour, Minute, Red Second hand)
    draw.line([(cx, cy), (cx+65, cy-45)], fill=(255, 255, 255, 255), width=7) # Hour
    draw.line([(cx, cy), (cx-30, cy-110)], fill=(250, 250, 255, 255), width=5) # Minute
    draw.line([(cx, cy), (cx+115, cy+40)], fill=(239, 68, 68, 255), width=2) # Second hand
    
    # Glass glare overlay
    draw.arc([cx-145, cy-145, cx+145, cy+145], start=210, end=330, fill=(255, 255, 255, 50), width=4)
    
    save_img(img, fp)

# 4. apple_product_4: PowerLine 100W GaN Charger
def gen_apple_4(fp):
    img = create_studio(1280, 960, (255, 255, 255), (147, 51, 234), bg=(10, 14, 24))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 480
    
    # Isometric block charger drawing
    # Top face
    draw.polygon([(cx-150, cy-80), (cx, cy-150), (cx+150, cy-80), (cx, cy-10)], fill=(250, 250, 255, 255), outline=(190, 190, 200, 255), width=3)
    # Left face
    draw.polygon([(cx-150, cy-80), (cx, cy-10), (cx, cy+180), (cx-150, cy+110)], fill=(225, 225, 230, 255), outline=(190, 190, 200, 255), width=3)
    # Right face (with USB ports)
    draw.polygon([(cx, cy-10), (cx+150, cy-80), (cx+150, cy+110), (cx, cy+180)], fill=(235, 235, 240, 255), outline=(190, 190, 200, 255), width=3)
    
    # 3 USB-C ports on the right face
    ports_y = [cy+30, cy+80, cy+130]
    for py in ports_y:
        # Receptacle shape in isometric perspective
        rx, ry = cx+60, py
        draw.polygon([(rx-25, ry-20), (rx+25, ry-35), (rx+25, ry-10), (rx-25, ry+5)], fill=(30, 32, 38, 255), outline=(170, 170, 180, 255), width=2)
        # Inner connector tab
        draw.line([(rx-12, ry-12), (rx+12, ry-19)], fill=(0, 172, 193, 255), width=3)
        
    # Printed logo on left face "100W GaN" Representation (geometric logo styling)
    draw.rounded_rectangle([cx-100, cy+30, cx-60, cy+60], radius=4, fill=(150, 150, 160, 100))
    draw.ellipse([cx-50, cy+40, cx-35, cy+55], outline=(150, 150, 160, 200), width=2)
    
    save_img(img, fp)

# 5. apple_product_5: iPhone 16 Pro (Front bezel-less screen with wallpaper)
def gen_apple_5(fp):
    img = create_studio(1280, 960, (59, 130, 246), (16, 185, 129), bg=(8, 12, 20))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 480
    
    # Phone chassis rim (Sleek dark titanium)
    draw.rounded_rectangle([cx-160, cy-300, cx+160, cy+300], radius=50, fill=(20, 20, 24, 255), outline=(80, 85, 95, 255), width=6)
    
    # Inner border screen active area
    draw.rounded_rectangle([cx-151, cy-291, cx+151, cy+291], radius=42, fill=(10, 10, 12, 255))
    
    # Colorful wallpaper gradient inside screen boundaries (using Pillow layers)
    wallpaper = Image.new("RGBA", (300, 580), (15, 20, 30, 255))
    wdraw = ImageDraw.Draw(wallpaper, "RGBA")
    # Draw complex glowing wallpaper shapes
    draw_radial_gradient(wdraw, 300, 580, 80, 100, 280, (0, 200, 255, 180), (15, 20, 30, 0))
    draw_radial_gradient(wdraw, 300, 580, 220, 450, 280, (236, 72, 153, 160), (15, 20, 30, 0))
    draw_radial_gradient(wdraw, 300, 580, 150, 290, 200, (147, 51, 234, 140), (15, 20, 30, 0))
    # Composite the screen wallpaper
    img.alpha_composite(wallpaper, (cx-150, cy-290))
    
    # Screen reflection & Dynamic Island capsule
    draw.rounded_rectangle([cx-50, cy-255, cx+50, cy-235], radius=10, fill=(0, 0, 0, 255))
    # Small green status dot next to island
    draw.ellipse([cx+55, cy-247, cx+59, cy-243], fill=(0, 255, 100, 255))
    
    # Glass glare overlay line
    draw.line([(cx-145, cy-285), (cx+145, cy+180)], fill=(255, 255, 255, 30), width=3)
    
    save_img(img, fp)

# 6. apple_product_6: Apex Run Ultra Watch (Rugged sports watch with orange strap)
def gen_apple_6(fp):
    img = create_studio(1280, 960, (245, 158, 11), (239, 68, 68), bg=(10, 12, 18))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 480
    
    # Orange textured strap (Rugged sports loop)
    draw.rounded_rectangle([cx-75, cy-330, cx+75, cy+330], radius=24, fill=(245, 110, 30, 255), outline=(210, 80, 10, 255), width=3)
    for ly in range(cy-310, cy+320, 16):
        if abs(ly - cy) > 130:
            draw.line([(cx-70, ly), (cx+70, ly)], fill=(215, 90, 15, 255), width=2)
            
    # Watch titanium rectangular case with rounded corners
    draw.rounded_rectangle([cx-150, cy-150, cx+150, cy+150], radius=50, fill=(35, 38, 44, 255), outline=(190, 195, 205, 255), width=10)
    
    # Screw accents on case corners
    screws = [(cx-120, cy-120), (cx+120, cy-120), (cx-120, cy+120), (cx+120, cy+120)]
    for sx, sy in screws:
        draw.ellipse([sx-6, sy-6, sx+6, sy+6], fill=(70, 75, 85, 255), outline=(130, 135, 145, 255), width=1)
        
    # Bezel ring
    draw.rounded_rectangle([cx-125, cy-125, cx+125, cy+125], radius=32, fill=(10, 12, 18, 255), outline=(45, 48, 55, 255), width=2)
    
    # Screen face
    draw.rounded_rectangle([cx-120, cy-120, cx+120, cy+120], radius=28, fill=(14, 18, 26, 255))
    
    # Screen HUD graphics (sports theme)
    # Circle progress ring in center
    draw.ellipse([cx-75, cy-75, cx+75, cy+75], outline=(0, 240, 255, 160), width=6)
    draw.ellipse([cx-60, cy-60, cx+60, cy+60], outline=(245, 158, 11, 200), width=2)
    # Glowing digital activity graphs
    draw.line([(cx-40, cy), (cx-20, cy-25), (cx, cy-10), (cx+20, cy-40), (cx+40, cy-20)], fill=(0, 255, 100, 220), width=3)
    
    # Crown dial wheel on right side
    draw.rounded_rectangle([cx+152, cy-45, cx+164, cy+45], radius=6, fill=(190, 195, 205, 255), outline=(100, 105, 115, 255), width=2)
    # Orange action button on left side
    draw.rounded_rectangle([cx-164, cy-35, cx-152, cy+35], radius=4, fill=(245, 110, 30, 255))
    
    save_img(img, fp)

# 7. rog_product_1: AeroBook Pro 16 ROG edition (Gaming laptop)
def gen_rog_1(fp):
    img = create_studio(1280, 960, (239, 68, 68), (147, 51, 234), bg=(8, 10, 18))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 480
    
    # Laptop Screen lid raised
    draw.polygon([(cx-310, cy-200), (cx+310, cy-200), (cx+340, cy+50), (cx-340, cy+50)], fill=(20, 22, 28, 255), outline=(239, 68, 68, 255), width=5)
    
    # LCD Screen boundaries
    draw.polygon([(cx-295, cy-185), (cx+295, cy-185), (cx+325, cy+35), (cx-325, cy+35)], fill=(12, 14, 18, 255))
    
    # Wallpaper graphic (Laser triangle cyberpunk pattern)
    w_pts = [(cx, cy-160), (cx+180, cy+20), (cx-180, cy+20)]
    draw.polygon(w_pts, fill=(147, 51, 234, 40), outline=(0, 240, 255, 180), width=2)
    draw.line([(cx, cy-160), (cx, cy+20)], fill=(239, 68, 68, 200), width=4)
    
    # Keyboard base deck
    draw.polygon([(cx-340, cy+50), (cx+340, cy+50), (cx+400, cy+200), (cx-400, cy+200)], fill=(32, 34, 42, 255), outline=(147, 51, 234, 200), width=4)
    
    # Keyboard area glowing red
    draw.polygon([(cx-290, cy+65), (cx+290, cy+65), (cx+340, cy+150), (cx-340, cy+150)], fill=(18, 20, 26, 255), outline=(239, 68, 68, 180), width=2)
    # Simulate keys dots
    for kx in range(cx-260, cx+270, 36):
        draw.line([(kx, cy+85), (kx+15, cy+135)], fill=(239, 68, 68, 120), width=3)
        
    save_img(img, fp)

# 8. rog_product_2: Vortex Gaming Laptop ROG (Aggressive gaming laptop with RGB keyboard)
def gen_rog_2(fp):
    img = create_studio(1280, 960, (239, 68, 68), (0, 240, 255), bg=(8, 10, 18))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 480
    
    # Aggressive laptop lid
    draw.polygon([(cx-330, cy-220), (cx+330, cy-220), (cx+360, cy+30), (cx-360, cy+30)], fill=(15, 17, 22, 255), outline=(0, 240, 255, 255), width=5)
    
    # LCD Screen
    draw.polygon([(cx-310, cy-200), (cx+310, cy-200), (cx+340, cy+15), (cx-340, cy+15)], fill=(8, 10, 14, 255))
    
    # Epic neon gaming graphics on screen
    draw_radial_gradient(draw, 1280, 960, cx, cy-80, 160, (239, 68, 68, 160), (0, 240, 255, 0))
    
    # Base keyboard chassis
    draw.polygon([(cx-360, cy+30), (cx+360, cy+30), (cx+420, cy+190), (cx-420, cy+190)], fill=(28, 30, 36, 255), outline=(239, 68, 68, 180), width=4)
    
    # RGB Keyboard grid
    draw.polygon([(cx-310, cy+45), (cx+310, cy+45), (cx+360, cy+140), (cx-360, cy+140)], fill=(12, 14, 18, 255), outline=(0, 240, 255, 120), width=2)
    # Multi-color keyboard row simulation
    draw.line([(cx-280, cy+65), (cx+280, cy+65)], fill=(239, 68, 68, 200), width=3) # Red row
    draw.line([(cx-290, cy+95), (cx+290, cy+95)], fill=(147, 51, 234, 200), width=3) # Purple row
    draw.line([(cx-300, cy+125), (cx+300, cy+125)], fill=(0, 240, 255, 200), width=3) # Cyan row
    
    save_img(img, fp)

# 9. rog_product_3: Zenith Ultrabook X ROG (Sleek minimalist thin gaming laptop)
def gen_rog_3(fp):
    img = create_studio(1280, 960, (147, 51, 234), (239, 68, 68), bg=(10, 14, 24))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 480
    
    # Thin laptop screen
    draw.polygon([(cx-320, cy-210), (cx+320, cy-210), (cx+335, cy+30), (cx-335, cy+30)], fill=(24, 24, 28, 255), outline=(147, 51, 234, 220), width=3)
    
    # Screen bezel-less display
    draw.polygon([(cx-312, cy-202), (cx+312, cy-202), (cx+327, cy+22), (cx-327, cy+22)], fill=(14, 18, 28, 255))
    
    # Neon wave graphic wallpaper
    draw.ellipse([cx-150, cy-180, cx+150, cy+20], fill=(239, 68, 68, 30), outline=(147, 51, 234, 160), width=2)
    
    # Ultra-thin base plate
    draw.polygon([(cx-335, cy+30), (cx+335, cy+30), (cx+380, cy+170), (cx-380, cy+170)], fill=(40, 42, 50, 255), outline=(147, 51, 234, 160), width=3)
    
    # Keyboard & trackpad
    draw.polygon([(cx-280, cy+45), (cx+280, cy+45), (cx+320, cy+120), (cx-320, cy+120)], fill=(18, 20, 24, 255), outline=(100, 100, 110, 255), width=1)
    
    save_img(img, fp)

# 10. rog_product_4: TitanForce Gaming PC ROG (Desktop PC cabinet with RGB interior fans)
def gen_rog_4(fp):
    img = create_studio(1280, 960, (239, 68, 68), (16, 185, 129), bg=(8, 10, 16))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 480
    
    # PC Tower metal case
    draw.rounded_rectangle([cx-150, cy-280, cx+150, cy+280], radius=20, fill=(20, 22, 28, 255), outline=(60, 65, 75, 255), width=8)
    
    # Tempered glass window boundary
    draw.rounded_rectangle([cx-130, cy-250, cx+130, cy+250], radius=12, fill=(10, 12, 18, 255), outline=(110, 115, 125, 200), width=3)
    
    # Glowing CPU fan cooler block (Water block custom loops)
    draw.ellipse([cx-55, cy-80, cx+55, cy+30], fill=(20, 24, 35, 255), outline=(239, 68, 68, 255), width=5)
    # Glowing ring inside
    draw.ellipse([cx-40, cy-65, cx+40, cy+15], outline=(0, 240, 255, 220), width=3)
    
    # Motherboard details & GPU block below
    draw.rounded_rectangle([cx-100, cy+60, cx+100, cy+125], radius=6, fill=(35, 38, 48, 255), outline=(16, 185, 129, 200), width=3) # GPU Block
    draw.line([(cx-90, cy+92), (cx+90, cy+92)], fill=(0, 240, 255, 255), width=2) # GPU strip LED
    
    # Front dual glowing intake fans (simulated transparent glow)
    # Top fan glow
    draw_radial_gradient(draw, 1280, 960, cx, cy-170, 45, (0, 240, 255, 80), (10, 12, 18, 0))
    draw.ellipse([cx-35, cy-205, cx+35, cy-135], outline=(0, 240, 255, 240), width=3)
    # Bottom fan glow
    draw_radial_gradient(draw, 1280, 960, cx, cy+180, 45, (147, 51, 234, 80), (10, 12, 18, 0))
    draw.ellipse([cx-35, cy+145, cx+35, cy+215], outline=(147, 51, 234, 240), width=3)
    
    # Semi-reflective diagonal glass glare line
    draw.line([(cx-120, cy-240), (cx+120, cy+100)], fill=(255, 255, 255, 35), width=4)
    
    save_img(img, fp)

if __name__ == "__main__":
    brands_dir = r"d:\mageten\electric-shop\assets\images\brands"
    
    gen_apple_1(os.path.join(brands_dir, "apple_product_1.png"))
    gen_apple_2(os.path.join(brands_dir, "apple_product_2.png"))
    gen_apple_3(os.path.join(brands_dir, "apple_product_3.png"))
    gen_apple_4(os.path.join(brands_dir, "apple_product_4.png"))
    gen_apple_5(os.path.join(brands_dir, "apple_product_5.png"))
    gen_apple_6(os.path.join(brands_dir, "apple_product_6.png"))
    
    gen_rog_1(os.path.join(brands_dir, "rog_product_1.png"))
    gen_rog_2(os.path.join(brands_dir, "rog_product_2.png"))
    gen_rog_3(os.path.join(brands_dir, "rog_product_3.png"))
    gen_rog_4(os.path.join(brands_dir, "rog_product_4.png"))
    
    print("All Apple and ROG brand product assets generated with gorgeous, high-contrast, premium detailed graphics!")
