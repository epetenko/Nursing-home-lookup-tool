from flask_frozen import Freezer
from app import app, get_csv
freezer = Freezer(app)


# def detail(row_id):
#     template = 'detail.html'
#     object_list = get_csv()
#     for row in object_list:
#         if row['Federal Provider Number'] == row_id:
#             yield render_template(template, object=row)


@freezer.register_generator
def detail():
    for row in get_csv():
        yield {'row_id': row['Federal Provider Number']}

if __name__ == '__main__':
    freezer.freeze()
