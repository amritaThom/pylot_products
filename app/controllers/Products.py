# ======================================================================================================================
# Products Controller:
# ======================================================================================================================
from system.core.controller import *
from flask import flash, escape


class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        self.load_model('Product')
        self.db = self._app.db

    # ==================================================================================================================
    # ['GET']['/products'] = 'Products#index': - display all product info
    # ==================================================================================================================
    def index(self):
        print "Controller: Products - ['GET']['/products'] = 'Products#index'"
        products = self.models['Product'].get_products()
        return self.load_view('products/index.html', products=products)

    # ==================================================================================================================
    # ['GET']['/products/new'] = 'Products#new': - display a form that allows the user to create a new product
    # ==================================================================================================================
    def new(self):
        print "Products#new"
        return self.load_view('products/add.html')

    # ==================================================================================================================
    # ['GET'] edit - display a form that allows the user to update a product info [ this would need a view file ]
    # ==================================================================================================================
    def edit(self, id):
        print "Products#edit", id
        product = self.models['Product'].get_product_by_id(id)
        return self.load_view('products/edit.html', product=product[0])

    # ==================================================================================================================
    # ['GET'] show - display a particular product info [ this would need a view file ]:
    # ==================================================================================================================
    def show(self, id):
        print "Products#show", id
        product = self.models['Product'].get_product_by_id(escape(id))
        return self.load_view('products/show.html', product=product[0])

    # ==================================================================================================================
    # ['POST'] create
    # ==================================================================================================================
    def create(self):
        print "Products#create"
        post = request.form

        # cleaning up the data before passing to the database to handle
        product = {
            'name': escape(post['name']),
            'description': escape(post['description']),
            'price': escape(post['price'])
        }

        # call and product to the add_product method from model
        # and write some logic based on the return value
        create_status = self.models['Product'].add_product(product)

        if create_status['status']:
            # the product have been created successfully, we will direct back to our index page
            return redirect('/products')
        else:
            # set flashed error messages here from the error message we returned from the Model
            # and use key for the flash catergories
            for key in create_status['errors']:
                flash(u'{}'.format(create_status['errors'][key]), key)
            return redirect('/products/new')

    # ==================================================================================================================
    # ['POST'] destroy - to process the form submitted from index method to remove a particular product
    # [ have this process the POST data and redirect back to '/products]
    # ==================================================================================================================
    def destroy(self, id):
        print "Products#destroy", id

        self.models['Product'].delete_product(escape(id))
        return redirect('/products')

    # ==================================================================================================================
    # ['POST'] update -
    # ==================================================================================================================
    def update(self, id):
        print "Product#update", id
        post = request.form

        product = {
            'id': escape(id),
            'name': escape(post['name']),
            'description': escape(post['description']),
            'price': escape(post['price'])
        }

        self.models['Product'].update_product(product)
        return redirect('/products')








