import os
from PIL import Image, ImageDraw, ImageFilter

def draw_radial_gradient(draw, width, height, center_x, center_y, radius, color_center, color_outer):
    for r in range(radius, 0, -4):
        t = r / radius
        r_col = int(color_center[0] * (1 - t) + color_outer[0] * t)
        g_col = int(color_center[1] * (1 - t) + color_outer[1] * t)
        b_col = int(color_center[2] * (1 - t) + color_outer[2] * t)
        a_col = int(color_center[3] * (1 - t) + color_outer[3] * t) if len(color_center) > 3 else 255
        draw.ellipse([center_x - r, center_y - r, center_x + r, center_y + r], fill=(r_col, g_col, b_col, a_col))

def create_studio(width=640, height=300, c1=(0, 240, 255), c2=(147, 51, 234), bg=(12, 16, 26)):
    img = Image.new("RGBA", (width, height), (*bg, 255))
    glow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    draw_radial_gradient(gdraw, width, height, int(width * 0.35), int(height * 0.4), int(min(width, height) * 0.7), (*c1, 100), (*bg, 0))
    draw_radial_gradient(gdraw, width, height, int(width * 0.65), int(height * 0.6), int(min(width, height) * 0.7), (*c2, 90), (*bg, 0))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=30))
    img.alpha_composite(glow)
    draw = ImageDraw.Draw(img)
    for x in range(0, width, 40):
        draw.line([(x, 0), (x, height)], fill=(255, 255, 255, 6), width=1)
    for y in range(0, height, 40):
        draw.line([(0, y), (width, y)], fill=(255, 255, 255, 6), width=1)
    return img

def gen_help_shipping(fp):
    # Cyan/Blue theme
    img = create_studio(640, 300, (0, 240, 255), (59, 130, 246))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 320, 150
    # Draw simple premium truck icon
    # Cargo box
    draw.rounded_rectangle([cx - 80, cy - 50, cx + 20, cy + 20], radius=8, fill=(20, 30, 50, 240), outline=(0, 240, 255, 255), width=4)
    # Cabin
    draw.rounded_rectangle([cx + 25, cy - 20, cx + 75, cy + 20], radius=6, fill=(20, 30, 50, 240), outline=(0, 240, 255, 255), width=4)
    # Connector
    draw.line([(cx + 20, cy + 10), (cx + 25, cy + 10)], fill=(0, 240, 255, 255), width=4)
    # Wheels
    draw.ellipse([cx - 50, cy + 15, cx - 20, cy + 45], fill=(12, 16, 26, 255), outline=(59, 130, 246, 255), width=4)
    draw.ellipse([cx + 35, cy + 15, cx + 65, cy + 45], fill=(12, 16, 26, 255), outline=(59, 130, 246, 255), width=4)
    img.resize((640, 300), Image.Resampling.LANCZOS).save(fp, "PNG", quality=95)
    print(f"Generated: {fp}")

def gen_help_warranty(fp):
    # Red/Purple theme
    img = create_studio(640, 300, (239, 68, 68), (147, 51, 234))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 320, 150
    # Draw premium shield icon
    points = [
        (cx, cy - 60),
        (cx + 50, cy - 40),
        (cx + 50, cy + 10),
        (cx, cy + 60),
        (cx - 50, cy + 10),
        (cx - 50, cy - 40)
    ]
    draw.polygon(points, fill=(20, 30, 50, 240), outline=(239, 68, 68, 255), width=4)
    # Checkmark inside shield
    draw.line([(cx - 15, cy), (cx - 5, cy + 15)], fill=(147, 51, 234, 255), width=5)
    draw.line([(cx - 5, cy + 15), (cx + 20, cy - 15)], fill=(147, 51, 234, 255), width=5)
    img.resize((640, 300), Image.Resampling.LANCZOS).save(fp, "PNG", quality=95)
    print(f"Generated: {fp}")

def gen_help_billing(fp):
    # Pink/Orange theme
    img = create_studio(640, 300, (236, 72, 153), (245, 158, 11))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 320, 150
    # Draw premium credit card icon
    draw.rounded_rectangle([cx - 80, cy - 50, cx + 80, cy + 40], radius=10, fill=(20, 30, 50, 240), outline=(236, 72, 153, 255), width=4)
    # Magnetic stripe
    draw.rectangle([cx - 80, cy - 30, cx + 80, cy - 15], fill=(236, 72, 153, 255))
    # Chip
    draw.rounded_rectangle([cx - 60, cy - 5, cx - 40, cy + 15], radius=2, fill=(245, 158, 11, 255))
    img.resize((640, 300), Image.Resampling.LANCZOS).save(fp, "PNG", quality=95)
    print(f"Generated: {fp}")

def gen_help_corporate(fp):
    # Green/Teal theme
    img = create_studio(640, 300, (16, 185, 129), (0, 240, 255))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 320, 150
    # Draw briefcase icon
    draw.rounded_rectangle([cx - 80, cy - 30, cx + 80, cy + 50], radius=10, fill=(20, 30, 50, 240), outline=(16, 185, 129, 255), width=4)
    # Handle
    draw.rounded_rectangle([cx - 30, cy - 50, cx + 30, cy - 30], radius=6, fill=(12, 16, 26, 0), outline=(16, 185, 129, 255), width=4)
    # Lock details
    draw.ellipse([cx - 25, cy + 5, cx - 15, cy + 15], fill=(0, 240, 255, 255))
    draw.ellipse([cx + 15, cy + 5, cx + 25, cy + 15], fill=(0, 240, 255, 255))
    img.resize((640, 300), Image.Resampling.LANCZOS).save(fp, "PNG", quality=95)
    print(f"Generated: {fp}")

if __name__ == "__main__":
    dest_dir = "assets/images/home"
    os.makedirs(dest_dir, exist_ok=True)
    gen_help_shipping(os.path.join(dest_dir, "help_shipping.png"))
    gen_help_warranty(os.path.join(dest_dir, "help_warranty.png"))
    gen_help_billing(os.path.join(dest_dir, "help_billing.png"))
    gen_help_corporate(os.path.join(dest_dir, "help_corporate.png"))
    print("Help assets generated successfully!")
