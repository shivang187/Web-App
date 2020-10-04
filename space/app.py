from flask import Flask, render_template, request
app = Flask(__name__,template_folder='template',static_folder='template\css')
@app.route('/')
def index():
	return render_template('index.html')
@app.route('/supernova', methods=['GET', 'POST'])
def supernova():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('index1.html')


@app.route('/gravitywave', methods=['GET', 'POST'])
def gravitywave():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('index3.html')

@app.route('/gamma', methods=['GET', 'POST'])
def gamma():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('index2.html')

if __name__=='__main__':
	app.run(debug=True)