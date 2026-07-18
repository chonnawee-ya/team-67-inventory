import json
import os

def display_products(file_path):
    if not os.path.exists(file_path):
        print("ไม่พบสินค้าในสต็อก")
        return
    
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
            
            if not data:
                print("ไม่พบสินค้าในสต็อก")
                return
            
            print(f"{'รหัส':<10} | {'ชื่อสินค้า':<20} | {'จำนวน':<10}")
            print("-" * 45)
            
            for item in data:
                item_id = item.get('id', 'N/A')
                item_name = item.get('name', 'N/A')
                item_qty = item.get('qty', 0)
                
                print(f"{item_id:<10} | {item_name:<20} | {item_qty:<10}")
                
        except json.JSONDecodeError:
            print("ข้อผิดพลาด: ไฟล์ JSON เรียบเรียงข้อมูลไม่ถูกต้อง")

