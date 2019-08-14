from flask import Flask
from flask import render_template, jsonify



json_path = './static/Provider_info_w_cost_report_data.json'
json_file = open(json_path,'r')
data = json_file.read()
print data
