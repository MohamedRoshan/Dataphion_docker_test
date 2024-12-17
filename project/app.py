from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

# Initialize Flask app
app = Flask(__name__)  # Corrected from _name_
app.secret_key = "secretkey"  # For flashing messages

def init_db():
    """Initialize the SQLite database and create a users table if it doesn't exist."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    """Render the home page with options to register or log in."""
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            flash("Registration successful! You can now log in.", "success")
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash("Username already exists. Please try a different one.", "danger")
        finally:
            conn.close()

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            return redirect(url_for('login_success'))
        else:
            flash("Invalid username or password. Please try again.", "danger")

    return render_template('login.html')

@app.route('/login_success')
def login_success():
    """Display a login success page."""
    return render_template('login_success.html')

@app.route('/go_back')
def go_back():
    """Redirect to the login page."""
    return redirect(url_for('login'))

if __name__ == '__main__':
    init_db()  # Ensure database and table are initialized
    app.run(host="0.0.0.0",port=int("5000"),debug=True)
    #give flask port no to 0.0.0.0 ( specificallly for flask)
    
