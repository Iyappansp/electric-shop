import os
import urllib.request
from PIL import Image

# Curated high-definition Unsplash photography for every product in the Voltage catalog
PRODUCT_UNSPLASH_MAP = {
    # Laptops
    1: "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=800&auto=format&fit=crop&q=90", # AeroBook Pro 16 OLED
    2: "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=800&auto=format&fit=crop&q=90", # Vortex Gaming Laptop
    3: "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=800&auto=format&fit=crop&q=90", # EliteBook Ultraslim 14
    4: "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=800&auto=format&fit=crop&q=90", # StudyMate Air 13
    5: "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=800&auto=format&fit=crop&q=90", # Zenith Ultrabook X
    29: "https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=800&auto=format&fit=crop&q=90", # ThinkBook Studio 14

    # Smartphones
    6: "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=800&auto=format&fit=crop&q=90", # Nimbus Phone 15
    7: "https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?w=800&auto=format&fit=crop&q=90", # AuraPhone Pro Max
    8: "https://images.unsplash.com/photo-1565849904461-04a58ad377e0?w=800&auto=format&fit=crop&q=90", # Pulse Lite 5G
    9: "https://images.unsplash.com/photo-1574944985070-8f3ebc6b79d2?w=800&auto=format&fit=crop&q=90", # DroidCore X3
    31: "https://images.unsplash.com/photo-1510557880182-3d4d3cba35a5?w=800&auto=format&fit=crop&q=90", # iPhone 16 Pro
    32: "https://images.unsplash.com/photo-1580910051074-3eb694886505?w=800&auto=format&fit=crop&q=90", # Xperia Ultra 5G

    # Headphones & Audio
    10: "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800&auto=format&fit=crop&q=90", # SoundHalo ANC Pro
    11: "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=800&auto=format&fit=crop&q=90", # GameSound Wireless GX
    12: "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=800&auto=format&fit=crop&q=90", # StudioTrue Reference
    13: "https://images.unsplash.com/photo-1572536147248-ac59a8abfa4b?w=800&auto=format&fit=crop&q=90", # SprintFit Sport Buds
    14: "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=800&auto=format&fit=crop&q=90", # AirWave Buds 2
    33: "https://images.unsplash.com/photo-1590658006821-04f4008d5717?w=800&auto=format&fit=crop&q=90", # TuneSport Wireless

    # Smartwatches
    15: "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=800&auto=format&fit=crop&q=90", # PulseWatch Fit Pro
    16: "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800&auto=format&fit=crop&q=90", # ChronoLux Premium
    17: "https://images.unsplash.com/photo-1434493789847-2f02dc6ca35d?w=800&auto=format&fit=crop&q=90", # EveryDay Watch SE
    18: "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=800&auto=format&fit=crop&q=90", # JuniorTrack Kids
    36: "https://images.unsplash.com/photo-1510017803434-a899398421b3?w=800&auto=format&fit=crop&q=90", # Apex Run Ultra
    37: "https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=800&auto=format&fit=crop&q=90", # Galaxy Watch Ultra 2

    # Gaming & Gear
    19: "https://images.unsplash.com/photo-1587202372775-e229f172b9d7?w=800&auto=format&fit=crop&q=90", # TitanForce Gaming PC
    20: "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=800&auto=format&fit=crop&q=90", # PixelView 27" 240Hz
    21: "https://images.unsplash.com/photo-1600080972464-8e5f35f63d08?w=800&auto=format&fit=crop&q=90", # GripCommand Pro
    22: "https://images.unsplash.com/photo-1612287230202-1ff1d85d1bdf?w=800&auto=format&fit=crop&q=90", # StreamCast Capture
    34: "https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?w=800&auto=format&fit=crop&q=90", # ProStream Webcam 4K
    35: "https://images.unsplash.com/photo-1547119957-637f8679db1e?w=800&auto=format&fit=crop&q=90", # ROG Swift 360Hz

    # Accessories
    23: "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=800&auto=format&fit=crop&q=90", # MechType Pro Keyboard
    24: "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=800&auto=format&fit=crop&q=90", # PrecisionGlide Mouse
    25: "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=800&auto=format&fit=crop&q=90", # VaultDrive 2TB SSD
    26: "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?w=800&auto=format&fit=crop&q=90", # PowerLine 100W GaN Charger
    27: "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=800&auto=format&fit=crop&q=90", # LinkWeave Mesh Router
    28: "https://images.unsplash.com/photo-1558002038-1055907df827?w=800&auto=format&fit=crop&q=90", # HomeGlow Smart Hub
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
out_dir = r"d:\mageten\electric-shop\assets\images\products"

def update_product_images():
    for pid, url in PRODUCT_UNSPLASH_MAP.items():
        filename = f"product_{pid}.png"
        dest_path = os.path.join(out_dir, filename)
        tmp_path = dest_path + ".tmp"
        print(f"Updating Product {pid} -> {filename}...")
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as resp, open(tmp_path, "wb") as f:
                f.write(resp.read())
            
            with Image.open(tmp_path) as img:
                img = img.convert("RGB")
                img.save(dest_path, "PNG", quality=95)
                
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
            print(f"[SUCCESS] Product {pid} updated ({os.path.getsize(dest_path)} bytes)")
        except Exception as e:
            print(f"[FAIL] Product {pid} failed: {e}")

if __name__ == "__main__":
    update_product_images()
