import pdfplumber
import glob
import os

print("🔄 Конвертирую PDF → TXT...")

pdf_files = glob.glob("knowledge_base/**/*.pdf", recursive=True)
print(f"📄 Найдено PDF: {len(pdf_files)}")

converted = 0
for pdf_path in pdf_files:
    try:
        with pdfplumber.open(pdf_path) as pdf:
            full_text = ""
            for page_num, page in enumerate(pdf.pages, 1):
                text = page.extract_text()
                if text:
                    full_text += f"\n--- Страница {page_num} ---\n{text}"
            
            # TXT файл рядом с PDF
            txt_path = pdf_path.replace('.pdf', '_extracted.txt')
            os.makedirs(os.path.dirname(txt_path), exist_ok=True)
            
            with open(txt_path, 'w', encoding='utf-8') as f:
                f.write(full_text.strip())
            
            print(f"✓ {os.path.basename(pdf_path)} → {os.path.basename(txt_path)} ({len(full_text)} симв.)")
            converted += 1
            
    except Exception as e:
        print(f"✗ {os.path.basename(pdf_path)}: {e}")

print(f"\n✅ Конвертировано: {converted}/{len(pdf_files)} PDF")
