from flask import Flask,render_template
import pyjokes
import jinja2
env = jinja2.Environment()
app=Flask(__name__)
app.jinja_env.globals.update(zip=zip)

joke=[]
@app.route("/single_joke")
def single_joke():
    joke.append(pyjokes.get_joke())
    length=len(joke)
    return render_template("output.html",jokes=joke,len=length)

@app.route("/multiple_jokes")
def multi_jokes():
    temp=pyjokes.get_jokes()
    for i in temp:
        joke.append(i)
    length=len(joke)
    return render_template("output.html",jokes=joke,len=length)

if __name__=="__main__":
    app.run(debug=True)
