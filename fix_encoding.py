# fix_encoding.py — исправленная версия
import os

# ТОЧНОЕ имя твоего файла
txt_file = "knowledge_base/договор_2023-СП_от_01.05.2024.txt"

print(f"🔧 Фиксим: {txt_file}")

try:
    # Пробуем UTF-8 BOM + CP1251
    with open(txt_file, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    
    # Если пусто — CP1251
    if len(content.strip()) < 100:
        with open(txt_file, 'r', encoding='cp1251') as f:
            content = f.read()
        print("   ✓ CP1251 найден")
    
    # Сохраняем UTF-8
    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {len(content)} симв. → UTF-8!")
    
except Exception as e:
    print(f"✗ Ошибка: {e}")
