from flask import Flask, render_template, request

# comment to test gitignore

######################## MAIN START #############################################################################################################################
app = Flask(__name__)

# What do I put here?

 # Homepage: GET
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
            """
                positions_list = list()
                for all positions in TABLE:(for p in positions)
                    positions_list.append(p.to_string())
                """
                #positions_list = Position.query.all()
            return render_template('positions.html'""", positions=positions_list""")
            
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
        

if __name__ == '__main__': # If this is the main method
    app.run(debug=True) # run the app, when debug=True is passed through you can edit and restart the webpage without stopping the app
######################## MAIN END ###############################################################################################################################