# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configuration for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'dirash.techsolutions@gmail.com'  # replace with your Gmail
app.config['MAIL_PASSWORD'] = 'fslq zfdk iuct qdbn'          # replace with your Gmail password or App Password
app.config['MAIL_DEFAULT_SENDER'] = 'ndirash.techsoluctions@gmail.com'  # replace with your Gmail

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        subject = request.form['subject']
        recipient = request.form['recipient']
        body = request.form['body']
        print(subject)
        print(recipient)
        print(body)

        msg = Message(subject, recipients=[recipient])
        msg.body = body
        
        try:
            mail.send(msg)
            print('Email sent successfully!', 'success')
            flash('Email sent successfully!', 'success')
        except Exception as e:
            print(f'Failed to send email: {str(e)}', 'danger')
            flash(f'Failed to send email: {str(e)}', 'danger')

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

