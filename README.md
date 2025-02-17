# Stored XSS Attack in Flask & SQLite

🚀 A demonstration of Stored Cross-Site Scripting (XSS) using Flask and SQLite3.



📌 Overview
This project demonstrates a Stored XSS vulnerability in a Flask web app. Users can submit comments, which are stored in an SQLite database. However, since user input is not sanitized, JavaScript code can be injected and executed when viewing the comments.



⚠️ Warning: This project is for educational purposes only. Do not use it for malicious activities.

🛠 Tech Stack
Backend: Flask (Python)
Database: SQLite3
Frontend: HTML, CSS, JavaScript
🚀 Features
✅ Submit Comments – Users can enter text-based comments.
✅ Stored XSS Attack – Malicious JavaScript can be injected and executed.
✅ Database Storage – Comments are stored using SQLite3.
✅ Flask Routing – Handles comment submission and display.



📂 Project Structure

Stored-XSS-Flask-SQLite/
│-- static/               # Contains CSS files
│   ├── style.css
│-- templates/            # Contains HTML files
│   ├── index.html
│   ├── post.html
│-- app.py                # Main Flask app
│-- database.db           # SQLite3 Database
│-- README.md             # Project Documentation



#  Install Dependencies
pip install flask

# Run the Flask App
python app.py


The server runs at http://127.0.0.1:5000/
Open your browser and go to http://127.0.0.1:5000/


🔥 Exploiting Stored XSS
1️⃣ Go to the comment submission page (/).
2️⃣ Enter the following malicious script in the comment box:
<script>alert('XSS Attack Successful!');</script>

3️⃣ Submit the comment.
4️⃣ Visit /post → The script will execute, triggering an alert box!



⚠️ Disclaimer
This project is for educational purposes only to learn about web security and XSS attacks. Do not use it for illegal activities.


🏆 Contributing
Feel free to submit issues or pull requests to improve the project!


📜 License
MIT License. Free to use and modify.

🚀 Made for Ethical Hacking & Cybersecurity Learning!
