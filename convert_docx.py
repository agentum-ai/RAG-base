import glob
from docx import Document
import os

print("🔄 Конвертация DOCX → TXT")
docx_files = glob.glob("knowledge_base/*.docx")
print(f"Найдено {len(docx_files)} DOCX")

for docx_path in docx_files:
    if docx_path.endswith('~$'):
        print(f"⏭️  Пропуск временного: {os.path.basename(docx_path)}")
        continue
    try:
        doc = Document(docx_path)
        text = '\n'.join([p.text for p in doc.paragraphs if p.text.strip()])
        txt_path = docx_path.replace('.docx', '_extracted.txt')
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"✅ {os.path.basename(docx_path)} → {os.path.basename(txt_path)} ({len(text)} символов)")
    except Exception as e:
        print(f"❌ {os.path.basename(docx_path)}: {e}")

print("🎉 Готово!")
