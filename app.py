from dotenv import load_dotenv

load_dotenv()

from flask import Flask, render_template, jsonify
from config import Config
from models import init_db, seed_sample_data
import services

app = Flask(__name__)

app.config.from_object(Config)

# @app.route('/')
@app.route('/')
def index():
    """Homepage - display all products"""
    categories = services.get_all_categories()
    products = services.get_all_products()
    result = render_template('index.html', products=products, categories=categories)
    return result

@app.route('/category/<int:category_id>')
def category(category_id):
    """Show products filtered by category"""
    categories = services.get_all_categories()
    category = services.get_category_by_id(category_id)
    products = services.get_products_by_category(category_id)
    return render_template('category.html', 
                         products=products, 
                         categories=categories,
                         current_category=category)

@app.route('/api/products')
def api_products():
    """API endpoint - return all products as JSON"""
    products = services.get_all_products()
    return jsonify({'products': products, 'status': 'success'})

@app.route('/api/categories')
def api_categories():
    """API endpoint - return all categories as JSON"""
    categories = services.get_all_categories()
    return jsonify({'categories': categories, 'status': 'success'})

@app.route('/vals-araba-bannerman-2026')
def google_page():
    return render_template('test.html')

if __name__ == '__main__':
    # Initialize database and add sample data when running locally
    init_db()
    seed_sample_data()
    app.run(debug=True)
