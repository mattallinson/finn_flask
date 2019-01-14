from flask import Flask, url_for, render_template, request
import finnish_number_name_maker as fnnm

app = Flask(__name__)
test_number = []
@app.route('/')
def hello():
	test_number.append(fnnm.number_maker())
	return render_template('hello.html', number=test_number[-1])

@app.route('/retry')
def retry():
	return render_template('hello.html', number=test_number[-1])

	
@app.route('/', methods=['POST'])
@app.route('/retry', methods=['POST'])	
def answer():
	number = test_number[-1]
	if request.method == 'POST':
		answer = request.form['answer']
		if fnnm.finnish_number_name_maker(number) == answer:
			return render_template('correct.html', answer=answer, number=number)
		else:
			return render_template('fail.html', answer=answer, number=number)


if __name__ == '__main__':
	app.run()