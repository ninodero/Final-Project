booking_page = """
<!DOCTYPE html>
<html>
<head>
	<title>Booking Page</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>
<body>
	<div class="container">
		<h1>Booking Page</h1>
		<form method="POST" action ="/book">
			<div class="form-group">
				<label for="name">Name:</label>
				<input type="text" name="name" class="form-control">
			</div>
			<div class="form-group">
				<label for="ticket_type">Ticket Type:</label>
				<select name="ticket_type" class="form-control">
					<option value="Standard">Standard</option>
					<option value="VIP">VIP</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">Book Ticket</button>
		</form>
	</div>
</body>
</html>
"""


from flask import Flask, render_template, request

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'username'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'ticket_booking_db'

from flaskext.mysql import MySQL


mysql = MySQL(app)


@app.route('/')
def booking():
	return render_template('booking.html')

@app.route('/book', methods=['POST'])
def book_ticket():
	name = request.form['name']
	ticket_type = request.form['ticket_type']


	cur = mysql.connection.cursor()
	cur.execute("INSERT INTO bookings (name, ticket_type) VALUES (%s, %s)", (name, ticket_type))
	mysql.connection.commit()
	cur.close()

	return "Ticket booked successfully!"

if __name__ == '__main__':

	app.run(debug=True)

