from flask import Flask
import csv
import datetime

app = Flask("my-webb-app")


@app.route("/")
def hello_world():
    return f"<h1>Hello, World!, My app name is : {__name__}</h1>"


@app.route("/list_products")
def list_products():
    return "<h1>Product 1 jjjh</h1>"


@app.route("/file_columns")
def get_file_columns():
    data = []
    with open('data/air_conditioners.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    return f"<h1>first element : {data[0]}</h1>"


def get_rating(row):
    return row.get('ratings')


def convert_to_float(val):
    try:
        converted_value = float(val)
    except ValueError:
        converted_value = 0
    
    return converted_value
        

@app.route("/top_10_products")
def get_10_top():
    data = []
    with open('data/air_conditioners.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    
    # convert rating to float
    for row in data:
        row["ratings"] = convert_to_float(row["ratings"])
        
    data.sort(key= lambda a: a["ratings"], reverse=True)
    new_data = data[0:10]
    return f"<h1>Histroy is : {new_data}</h1>"


@app.route("/history")
def get_modification_history():
    with open('data/creation_history.txt', 'r', newline='') as txtfile:
        history_dates = txtfile.readlines()
    
    new_history_dates = []
    for row in history_dates:
        new_history_dates.append(row.replace('\n', ''))   
    return f"<h1>Histroy is : {new_history_dates}</h1>"

@app.route("/save_data")
def save_data_to_file():
    today = datetime.datetime.now()
    with open('data/creation_history.txt', 'a', newline='') as txtfile:
        txtfile.write(f"{today.isoformat()} \n")
    
    data = []
    with open('data/air_conditioners.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    
    new_data = data[0:20]
    with open('data/air_conditioners_20.csv', 'w', newline='') as csvfile:
        column_names = new_data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=column_names)
        writer.writeheader()    
        writer.writerows(new_data)


    return f"<h1>Data is saved</h1>"


