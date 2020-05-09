
from flask import Flask, render_template, request, jsonify, redirect
import sys
import mysql.connector

app = Flask(__name__)


# util funtions
def executeScriptsFromFile(cursor, filename):
	fd = open(filename, 'r')
	sqlFile = fd.read()
	fd.close()
	sqlCommands = sqlFile.split(';')
	for command in sqlCommands:
		try_sql_cmd(cursor, command)

def try_sql_cmd(cursor, cmd):
	try:
		cursor.execute(cmd)
		print("success",file=sys.stderr)
	except mysql.connector.Error as err:
		print("SQL error: ", err, file=sys.stderr)

def insert(cursor,form):
	grade = int(form['grade'])
	class_num = int(request.form['class'])
	course_num = int(request.form['course'])
	useDate = request.form['useDate']
	subject = request.form['subject']
	is_normal = int(request.form['is_normal'])
	description = request.form['description']
	user = request.form['user']
	
	#@TODO: validation
	if user and useDate:
		cursor.execute("INSERT INTO info (grade, class,course, useDate, subject,is_normal,description,user) VALUES ( '%d','%d','%d','%s','%s','%d','%s','%s');" % (grade,class_num,course_num,useDate,subject,is_normal,description,user))
		return 0
	else:
		if not user:
			return -1
		if not useDate:
			return -2
		

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():

	dbconnection = mysql.connector.connect(
      host="localhost",
      user="root",
      password="AQua0917"
    )
	cursor = dbconnection.cursor(buffered=True)
	cursor.execute("select count(*) from information_schema.tables where Table_schema = 'deviceDashboard';")
	check_database = cursor.fetchall()
	if check_database == [(0,)]:
		executeScriptsFromFile(cursor, "./temp.sql")
	cursor.execute("USE deviceDashboard;")
	
	status_code = insert(cursor,request.form)
	if(status_code == -1):
		return jsonify({'error' : 'Missing Signature!'})
	elif(status_code == -2):
		return jsonify({'error' : 'Missing Date!'})
	else:
		dbconnection.commit()
	return jsonify({'msg':'success'})



if __name__ == '__main__':
	app.run(debug=True)