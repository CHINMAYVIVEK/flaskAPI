from flask import Flask,jsonify,render_template
import mysql.connector

# from config.dbConfig import mydb_connection as mydbcursor


app = Flask(__name__)

app.config["Debug"] = True

mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "",
database = "test")
mydbcursor = mydb.cursor()


@app.route("/get-categories")
def get_categories():

    select_query = " SELECT * FROM categories " 

    mydbcursor.execute(select_query)
    results = mydbcursor.fetchall()

    return jsonify(results)


@app.route("/get-products")
def get_products():

    select_query = """ SELECT
    C.name AS Categories_name,
    P.name AS Products_name, P.price
    FROM  products as P 
    INNER JOIN  categories as C 
    ON P.category_id = C.id
    """

    mydbcursor.execute(select_query)
    results = mydbcursor.fetchall()

    return render_template('test_template.html', results=results)
    # return results


@app.route("/set-product",methods=['POST'])
def set_products(name, description, created):

    insert_query = """ INSERT INTO 
    categories (name, description,created) 
    VALUES (%s, %s, %s)
    """

    val = (name, description,created)
    mydbcursor.execute(insert_query,val)

    mydb.commit()
    print(mydbcursor.rowcount, "Record Inserted")

    # results = mydbcursor.fetchall()

    # return render_template('test_template.html', results=results)
    return "results"




__name__ == '__main__'
app.run(debug=True)