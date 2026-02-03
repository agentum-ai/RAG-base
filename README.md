📋 **Финальный README.md для GitHub (актуальный под ваши файлы)**

**Копируйте целиком → GitHub → Edit README.md → Вставьте → Commit!**

```markdown
# 🧠 RAG Pro v3.1 — Консультант по базе знаний

[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-0.3-green.svg)](https://langchain.com)
[![FAISS](https://img.shields.io/badge/Vector%20DB-FAISS-orange.svg)](https://github.com/facebookresearch/faiss)

**Семантический поиск + GPT-4o-mini по вашим DOCX/PDF/TXT.**  
Преобразует договоры/документы → чат-бот "цена контракта?" → "145 278 393 руб, источник: стр. 3".

## 🚀 Запуск за 2 минуты

### Предварительные требования
- Python 3.9+
- OpenAI аккаунт (GPT-4o-mini, ~$5/мес)

### Установка
```bash
git clone https://github.com/agentum-ai/RAG-base.git
cd RAG-base
pip install -r requirements.txt
```

### Быстрый старт
```bash
# 1. Ваш OpenAI ключ (5 сек)
echo "sk-proj-your-key" > api_key.txt

# 2. Запуск
python rag_pro_final.py
```

**Вывод:**
```
📂 Сканирование knowledge_base/
📄 TXT: sample_knowledge.txt
✅ Загружено 1 документов (добавьте свои!)
🔄 Multilingual эмбеддинги (RU)...
✂️ Разбито на 150+ чанков
✅ FAISS готов (k=20)
🧪 кто директор? → Конкретный ответ!
🤖 Чат: ❓
```

## 📁 Добавление документов

### 1. DOCX/PDF → TXT (автоматически)
```bash
# Положите файлы в knowledge_base/
python convert_docx.py   # DOCX→TXT
python convert_pdf.py    # PDF→TXT  
python fix_encoding.py   # CP1251→UTF-8
```

### 2. Перестройка индекса
```bash
rmdir /s /q faiss_index  # Очистить
python rag_pro_final.py  # ✅
```

## 💬 Чат-команды
```
❓ "цена муниципального контракта"  # Семантический поиск
! "пункт 2.3 договора"              # Точный extract (k=25)
exit                                # Выход
```

## 📂 Структура файлов

| Файл                | Назначение            |
| ------------------- | --------------------- |
| rag_pro_final.py    | 🎯 Всё в 1 файл!      |
| requirements.txt    | pip install -r        |
| .gitignore          | 🛡️ Безопасность      |
| convert_docx.py     | DOCX→TXT              |
| convert_pdf.py      | PDF→TXT (pdfplumber)  |
| fix_encoding.py     | Windows CP1251→UTF-8  |
| api_key.txt.example | 👈 Скопируйте + ключ! |

## 🛠 Стек v3.1 (оптимизировано)

| Компонент  | Особенности                                      |
| ---------- | ------------------------------------------------ |
| LLM        | GPT-4o-mini (дешево+точно)                       |
| Embeddings | paraphrase-multilingual-mpnet-base-v2 (Русский!) |
| Chunks     | 1500 симв. / 300 overlap                         |
| Retriever  | k=20 (много контекста)                           |
| Vector DB  | FAISS (локально, быстро)                         |

## 📈 Результаты оптимизации

| До           | После           |
| ------------ | --------------- |
| 1 документ   | 3+              |
| 1 чанк       | 150+            |
| "Нет данных" | 145 278 393 руб |
| EN-only      | Русский         |

## 🔐 Безопасность

```
✅ api_key.txt → НЕ коммитьте! (.gitignore)
✅ knowledge_base/ → Локальные файлы (.gitignore)  
✅ faiss_index/ → Авто-удаление
```

## 📝 Локальная knowledge_base/

```
knowledge_base/
├── sample_knowledge.txt           # 🎁 Пример
├── *_extracted.txt                # Конвертированные
└── ваши_договоры.txt              # 👈 Сюда!
```

## 🤝 Репликация (другие пользователи)

```bash
git clone https://github.com/agentum-ai/RAG-base.git
cd RAG-base
pip install -r requirements.txt
mkdir knowledge_base
# Копия ваших TXT сюда
echo "sk-..." > api_key.txt
python rag_pro_final.py
```

## 📞 Связь
**Илья Козлов** | kozlow.ia@gmail.com | Feb 2026  
**Лицензия:** MIT

[🚀 Star проект!](https://github.com/agentum-ai/RAG-base)
