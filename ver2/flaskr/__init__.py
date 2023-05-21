# SOF #####################################################

## Imports
import os, sqlite3
## Flask
from flask import Flask, render_template, request
from flaskr.order import Order
from flaskr.position import Position
### Flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

## CREATE APP #############################################

def create_app(test_config=None):

### APP CREATION ##########################################

    app = Flask(__name__, instance_relative_config=True) # create and configure the appz
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

### APP CREATION END ######################################

### HTTPS REQUESTS ########################################
    @app.route('/')
    def homepage(): 
        title = "PythonTrader"
        return render_template('home.html', title=title)
    
    # Homepage: Controlling the Buttons - Navigates to the Titled Page on the button
    @app.route('/', methods=['POST'])
    def ui_nav_buttons_hp(): # UI Navigation Buttons Homepage
        if request.method == 'POST': 
            if request.form.get('positions') == 'Positions': # Positions Button
            # add code to pull all positions from sql, then...
            
                positions_list = list()
                x = Position('apple', 'aapl', '100', '')
            
                #positions_list = Position.query.all()
                return render_template('positions.html', positions=positions_list)
            
            elif request.form.get('orders') == 'Orders': # Orders Button
                print('order_button')
            #orders_list = Order.query.all()
                return render_template('orders.html'""", orders=orders_list""")
            elif request.form.get('settings') == 'Settings':
                print('settings_button')
                return render_template('settings.html')
            else:
                print('step in at line 25')
                pass
        else:
            return render_template('home.html')
    
### HTTPS REQUESTS END ####################################

### DB FUNCTIONS ##########################################

    from . import db
    db.init_app(app)
    
    return app

### DB FUNCTIONS END ######################################

## CREATE APP END #########################################
# EOF #####################################################