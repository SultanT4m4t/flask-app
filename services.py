from models import get_db_connection

def get_all_categories():
    """Retrieve all categories from database"""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM categories ORDER BY name')
    categories = cur.fetchall()
    cur.close()
    conn.close()
    return categories

def get_all_products():
    """Retrieve all products with their category names"""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        SELECT p.*, c.name as category_name 
        FROM products p
        LEFT JOIN categories c ON p.category_id = c.id
        ORDER BY p.created_at DESC
    ''')
    products = cur.fetchall()
    cur.close()
    conn.close()
    return products

def get_products_by_category(category_id):
    """Retrieve products filtered by category"""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        SELECT p.*, c.name as category_name 
        FROM products p
        LEFT JOIN categories c ON p.category_id = c.id
        WHERE p.category_id = %s
        ORDER BY p.created_at DESC
    ''', (category_id,))
    products = cur.fetchall()
    cur.close()
    conn.close()
    return products

def get_category_by_id(category_id):
    """Get a single category by ID"""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM categories WHERE id = %s', (category_id,))
    category = cur.fetchone()
    cur.close()
    conn.close()
    return category