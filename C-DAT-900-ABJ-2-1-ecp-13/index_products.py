import sqlite3, json, os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
DB = os.getenv("PRODUCT_DB_PATH", "./product_embeddings.db")

def ensure_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, sku TEXT UNIQUE, title TEXT, price REAL, short_desc TEXT, long_desc TEXT, images TEXT, embedding TEXT)')
    conn.commit()
    conn.close()

def index_products(products_json='products.json'):
    with open(products_json, 'r', encoding='utf-8') as f:
        products = json.load(f)
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    for p in products:
        text_for_emb = f"{p.get('title','')} - {p.get('short_desc','')}"
        emb_resp = client.embeddings.create(model='text-embedding-3-small', input=text_for_emb)
        emb = emb_resp.data[0].embedding
        cur.execute('INSERT OR REPLACE INTO products (sku, title, price, short_desc, long_desc, images, embedding) VALUES (?, ?, ?, ?, ?, ?, ?)', (
            p.get('sku'), p.get('title'), p.get('price') or 0, p.get('short_desc',''), p.get('long_desc',''), json.dumps(p.get('images',[])), json.dumps(emb)
        ))
    conn.commit()
    conn.close()
    print("Indexation terminée.")

if __name__ == '__main__':
    ensure_db()
    index_products()