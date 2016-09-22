from system.core.model import Model
import re


class Product (Model):
    def __init__(self):
        super(Product, self).__init__()

    def get_products(self):
        return self.db.query_db("SELECT * FROM products ORDER BY created_at DESC")

    def add_product(self, product):
        # regex to check that price is only numeric
        price_regex = re.compile(r'^\d+[.]\d+$')

        # price validation before passing to database
        errors = {}

        if not product['price']:
            errors['price'] = "Price must be entered"
        elif not price_regex.match(product['price']):
            errors['price'] = "Price must be only digit"

        # if we hit errors, return them, else return create user
        # and return the user that we created back to
        if errors:
            return {'status': False, "errors": errors}
        else:
            # if everything looks good, we insert product to database
            query = "INSERT INTO products (name, description, price, created_at, updated_at) VALUE (:name, :description, :price, NOW(), NOW())"
            data = {
                'name': product['name'],
                'description': product['description'],
                'price': product['price']
            }
            self.db.query_db(query, data)

            # then retrieve the last insert product
            get_product_query = "SELECT * FROM products ORDER BY id DESC LIMIT 1"
            products = self.db.query_db(get_product_query)
            return {"status": True, "product": products[0]}

        return self.db.query_db(query, data)

    def get_product_by_id(self, product_id):
        query = "SELECT * FROM products WHERE id = :product_id"
        data = {
            'product_id': product_id
        }
        return self.db.query_db(query, data)

    def update_product(self, product):
        query = "UPDATE products SET name=:name, description=:description, price=:price WHERE id = :id"

        data = {
            'id': product['id'],
            'name': product['name'],
            'description': product['description'],
            'price': product['price'],
        }

        return self.db.query_db(query, data)

    def delete_product(self, product_id):
        query = "DELETE FROM products WHERE id = :id"

        data = {
            "id": product_id
        }

        return self.db.query_db(query, data)
