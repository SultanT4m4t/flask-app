import psycopg2
from psycopg2.extras import RealDictCursor
from config import Config

def get_db_connection():
    """Create and return a database connection"""
    conn = psycopg2.connect(
        Config.DATABASE_URL,
        cursor_factory=RealDictCursor
    )
    return conn

def init_db():
    """Initialize database tables"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Create categories table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL UNIQUE
        )
    ''')
    
    # Create products table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name VARCHAR(200) NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            category_id INTEGER REFERENCES categories(id),
            image_url VARCHAR(500),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    cur.close()
    conn.close()
    print("Database tables created successfully")

def seed_sample_data():
    """Add sample categories and products for testing"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Check if data already exists
    cur.execute('SELECT COUNT(*) as count FROM categories')
    if cur.fetchone()['count'] > 0:
        cur.close()
        conn.close()
        return
    
    # Insert sample categories
    categories = ['Electronics', 'Clothing', 'Books']
    for cat in categories:
        cur.execute('INSERT INTO categories (name) VALUES (%s)', (cat,))
    
    # Insert sample products
    products = [
        ('Laptop', 999.99, 1, 'static/images/products/laptop.png'),
        ('Smartphone', 699.99, 1, 'https://via.placeholder.com/300x200?text=Smartphone'),
        ('Headphones', 149.99, 1, 'https://via.placeholder.com/300x200?text=Headphones'),
        ('T-Shirt', 29.99, 2, 'https://via.placeholder.com/300x200?text=T-Shirt'),
        ('Jeans', 59.99, 2, 'https://via.placeholder.com/300x200?text=Jeans'),
        ('Sneakers', 89.99, 2, 'https://via.placeholder.com/300x200?text=Sneakers'),
        ('Python Guide', 39.99, 3, 'https://via.placeholder.com/300x200?text=Python+Guide'),
        ('Design Book', 44.99, 3, 'https://via.placeholder.com/300x200?text=Design+Book'),
    ]
    
    for product in products:
        cur.execute(
            'INSERT INTO products (name, price, category_id, image_url) VALUES (%s, %s, %s, %s)',
            product
        )
    
    conn.commit()
    cur.close()
    conn.close()
    print("Sample data seeded successfully")




