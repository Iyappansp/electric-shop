import os
import math
from PIL import Image, ImageDraw, ImageFilter, ImageFont

def draw_radial_gradient(draw, width, height, center_x, center_y, radius, color_center, color_outer):
    for r in range(radius, 0, -4):
        t = r / radius
        r_col = int(color_center[0] * (1 - t) + color_outer[0] * t)
        g_col = int(color_center[1] * (1 - t) + color_outer[1] * t)
        b_col = int(color_center[2] * (1 - t) + color_outer[2] * t)
        a_col = int(color_center[3] * (1 - t) + color_outer[3] * t) if len(color_center) > 3 else 255
        draw.ellipse([center_x - r, center_y - r, center_x + r, center_y + r], fill=(r_col, g_col, b_col, a_col))

def create_studio(width=1280, height=960, c1=(0, 240, 255), c2=(147, 51, 234), bg=(12, 16, 26)):
    img = Image.new("RGBA", (width, height), (*bg, 255))
    glow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    draw_radial_gradient(gdraw, width, height, int(width * 0.35), int(height * 0.4), int(min(width, height) * 0.65), (*c1, 110), (*bg, 0))
    draw_radial_gradient(gdraw, width, height, int(width * 0.65), int(height * 0.6), int(min(width, height) * 0.65), (*c2, 100), (*bg, 0))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=45))
    img.alpha_composite(glow)
    draw = ImageDraw.Draw(img)
    for x in range(0, width, 60):
        draw.line([(x, 0), (x, height)], fill=(255, 255, 255, 8), width=1)
    for y in range(0, height, 60):
        draw.line([(0, y), (width, y)], fill=(255, 255, 255, 8), width=1)
    return img

def save_img(img, filepath, w=640, h=480):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    img.resize((w, h), Image.Resampling.LANCZOS).save(filepath, "PNG", quality=95)
    print(f"Generated: {filepath}")

# 1. Regenerate Zenith Ultrabook X (product_5.png) in Landscape 640x480
def gen_zenith_ultrabook_landscape(fp):
    img = create_studio(1280, 960, (59, 130, 246), (147, 51, 234), bg=(10, 14, 24))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 440
    w, h = 330, 185
    
    # Laptop Screen lid (Landscape perspective)
    pts_s = [(cx - w, cy - h), (cx + w, cy - h), (cx + int(w*1.08), cy + int(h*0.2)), (cx - int(w*1.08), cy + int(h*0.2))]
    draw.polygon(pts_s, fill=(18, 24, 38, 255), outline=(59, 130, 246, 240), width=4)
    
    disp_s = [(cx - int(w*0.92), cy - int(h*0.88)), (cx + int(w*0.92), cy - int(h*0.88)), (cx + int(w*1.0), cy + int(h*0.1)), (cx - int(w*1.0), cy + int(h*0.1))]
    draw.polygon(disp_s, fill=(8, 14, 28, 255), outline=(147, 51, 234, 180), width=2)
    
    # Screen wallpaper graphic
    draw.ellipse([cx-120, cy-120, cx+120, cy], fill=(59, 130, 246, 60), outline=(0, 240, 255, 200), width=2)
    
    # Base Keyboard Deck (Landscape)
    pts_d = [(cx - int(w*1.08), cy + int(h*0.2)), (cx + int(w*1.08), cy + int(h*0.2)), (cx + int(w*1.24), cy + int(h*0.6)), (cx - int(w*1.24), cy + int(h*0.6))]
    draw.polygon(pts_d, fill=(24, 30, 48, 255), outline=(59, 130, 246, 200), width=3)
    
    # Keyboard grid
    kb_pts = [(cx - int(w*0.9), cy + int(h*0.25)), (cx + int(w*0.9), cy + int(h*0.25)), (cx + int(w*1.1), cy + int(h*0.5)), (cx - int(w*1.1), cy + int(h*0.5))]
    draw.polygon(kb_pts, fill=(32, 40, 60, 255), outline=(147, 51, 234, 160), width=2)
    
    save_img(img, fp, 640, 480)

# 2. Store Map Wide Graphic (store_map.png)
def gen_store_map_wide(fp):
    w_img, h_img = 1600, 700
    img = Image.new("RGBA", (w_img, h_img), (14, 18, 28, 255))
    draw = ImageDraw.Draw(img, "RGBA")
    
    # Dark cyber map grid background
    for x in range(0, w_img, 80):
        draw.line([(x, 0), (x, h_img)], fill=(255, 255, 255, 12), width=1)
    for y in range(0, h_img, 80):
        draw.line([(0, y), (w_img, y)], fill=(255, 255, 255, 12), width=1)
        
    # Roads / Highways
    draw.line([(0, 350), (w_img, 350)], fill=(30, 42, 64, 255), width=36)
    draw.line([(0, 350), (w_img, 350)], fill=(0, 240, 255, 80), width=6)
    
    draw.line([(600, 0), (600, h_img)], fill=(30, 42, 64, 255), width=28)
    draw.line([(600, 0), (600, h_img)], fill=(59, 130, 246, 80), width=4)
    
    draw.line([(1100, 0), (1100, h_img)], fill=(30, 42, 64, 255), width=28)
    draw.line([(1100, 0), (1100, h_img)], fill=(147, 51, 234, 80), width=4)

    # Diagonal main boulevard
    draw.line([(200, 0), (1400, h_img)], fill=(36, 50, 76, 255), width=42)
    draw.line([(200, 0), (1400, h_img)], fill=(16, 185, 129, 90), width=6)

    # Voltage Store Pin Marker (Center)
    cx, cy = 800, 350
    # Pulse rings
    draw.ellipse([cx-120, cy-120, cx+120, cy+120], fill=(0, 240, 255, 20), outline=(0, 240, 255, 120), width=2)
    draw.ellipse([cx-60, cy-60, cx+60, cy+60], fill=(0, 240, 255, 40), outline=(0, 240, 255, 200), width=3)
    
    # Pin marker
    draw.ellipse([cx-35, cy-75, cx+35, cy-5], fill=(239, 68, 68, 255), outline=(255, 255, 255, 240), width=4)
    draw.polygon([(cx-30, cy-25), (cx+30, cy-25), (cx, cy+25)], fill=(239, 68, 68, 255))
    draw.circle((cx, cy-40), radius=12, fill=(255, 255, 255, 255))

    save_img(img, fp, 1200, 500)

if __name__ == "__main__":
    base_dir = r"c:\Users\infot\Contacts\OneDrive\Desktop\PDI\electric-shop\assets\images"
    gen_zenith_ultrabook_landscape(os.path.join(base_dir, "products", "product_5.png"))
    gen_store_map_wide(os.path.join(base_dir, "home", "store_map.png"))
    print("Zenith landscape asset & wide map generated successfully!")
