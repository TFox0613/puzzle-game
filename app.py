from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 解謎答案
ANSWER1 = "love2024"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/puzzle', methods=['GET', 'POST'])
def puzzle():
    if request.method == 'POST':
        user_answer = request.form.get('answer', '').strip().lower()
        if user_answer == ANSWER1:
            return redirect(url_for('success'))
        else:
            return render_template('puzzle1.html', error="答錯囉，再想想！")
    return render_template('puzzle1.html')

@app.route('/success')
def success():
    return render_template('success.html')
    
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
