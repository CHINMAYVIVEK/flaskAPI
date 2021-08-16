from os import pardir, truncate
from flask import Flask
from flask_restful import Resource, Api, reqparse
import mysql.connector

app = Flask(__name__)
api = Api(app)


mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "",
database = "test")
mydbcursor = mydb.cursor()


class CreateCategory(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()

            parser.add_argument('name', type=str, help="name for categories")
            parser.add_argument('description', type=str)
            parser.add_argument('created', type=str)
            args = parser.parse_args()

            _categoryName = args['name']
            _categoryDescription = args['description']
            _categoryCreated = args['created']

            insert_query = """ INSERT INTO 
            categories (name, description,created) 
            VALUES (%s, %s, %s) 
            """

            val = (_categoryName, _categoryDescription,_categoryCreated)
            mydbcursor.execute(insert_query,val)

            mydb.commit()
            print(mydbcursor.rowcount, "Record Inserted")


            return {'Name': args['name'], 'Description': args['description'], 'Created': args['created']}
        
        except Exception as e:
            return {'error':str(e)}

api.add_resource(CreateCategory, '/create-category')

if __name__ == '__main__':
    app.run(debug=True)