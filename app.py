import csv
from flask import Flask
from flask import render_template, jsonify
app = Flask(__name__)

# original pull of csv to create app
def get_csv():
    csv_path = './static/Provider_info_w_cost_report_data.csv'
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list

# Creates index.html template with csv data
@app.route("/")
def index():
    template = 'index.html'
    object_list = get_csv()
    return render_template(template, object_list=object_list)

# creates detail page for each Nursing home
@app.route('/<row_id>/')
def detail(row_id):
    template = 'detail.html'
    object_list = get_csv()
    for row in object_list:
        if row['Federal Provider Number'] == row_id:
            return render_template(template, object=row)



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
