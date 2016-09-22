# ======================================================================================================================
# Products Routes:
# ======================================================================================================================
from system.core.router import routes

# REST-ful Routes
routes['default_controller'] = 'Products'                        # Default route /
routes['GET']['/products'] = 'Products#index'                    # Show all items
routes['GET']['/products/new'] = 'Products#new'                  # Show new form
routes['POST']['/products'] = 'Products#create'                  # Create an item
routes['GET']['/products/<int:id>'] = 'Products#show'            # Show item with :id
routes['GET']['/products/<int:id>/edit'] = 'Products#edit'       # Show edit form for item with :id
routes['POST']['/products/<int:id>/update'] = 'Products#update'  # Update item with :id
routes['GET']['/products/<int:id>/delete'] = 'Products#delete'   # Show delete form for item with :id
routes['POST']['/products/<int:id>'] = 'Products#destroy'        # Delete item with :id

