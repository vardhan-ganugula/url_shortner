from flask import Flask, render_template, request, redirect
import database_control, json

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        output_url = database_control.write_database(url)
        return render_template('index.html', urlLink= f"http://localhost:5000/{output_url}")
    else:
        return render_template('index.html')

@app.route('/<url_link>')
def url_shortner(url_link):
    get_urldata = database_control.get_database()
    try:
        for i in get_urldata:
            if url_link == i['shortened_link']:
                database_control.update_views(url_link,request.access_route[-1])
                return redirect(i['main_link'])
        else:
            return 'url not found'
    except:
        return "Url not found"
    
@app.route('/data')
def data():
    return render_template('data.html')
@app.route('/generate-url', methods=['POST'])
def generate_url():
    url = request.form['url']
    output_url = database_control.write_database(url)
    return str(output_url)

@app.route('/custom-url', methods=['POST', 'GET'])
def custom_url():
    if request.method == 'POST':
        inp_url = request.form['url']
        customUrl = request.form['customUrl']
        for i in database_control.get_database():
            if customUrl in i["shortened_link"]:
                return render_template('custom.html', err="Link already exists")
        else:
            database_control.write_customUrl(inp_url, customUrl)
            return render_template('custom.html', urlLink= f"http://localhost:5000/{customUrl}")
    else:   
        return render_template('custom.html')
@app.route('/dashboard')
def get_user_ip():
    with open('database.json', 'r') as file:
        data = json.load(file)
    unique_views = 0
    total_views = 0
    for i in data:
        total_views += i['views']
        unique_views += len(set(i['ip_addr']))

    return render_template('dashboard.html', data = data, unique_views = unique_views, total_views = total_views, totalLinks = len(data))

if __name__ == '__main__':
    app.run(debug=True)
