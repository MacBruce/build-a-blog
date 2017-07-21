#the majority of the assignment is near identical to user signup that we did
#the videos were very helpful

from flask import Flask, request, redirect, render_template
from isEmpty import *
from flask_sqlalchemy import SQLAlchemy

# create runnable app & connect to db
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://blog:doublerainbow@localhost:3306/blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


# create blog model for db
class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    body = db.Column(db.String(3000))


    def __init__(self, title, body):
        
        self.title = title
        self.body = body

# handle home route by redirecting to home page
@app.route('/', methods=['POST', 'GET'])
def index():
    return redirect('/blog')

@app.route('/blog', methods=['POST', 'GET'])
def blog():
    #url building
    if request.args:
        post_id = request.args.get('id')
        blog = Blog.query.get(post_id)
        return render_template('singlepost.html', blog=blog)
    else:
        blogs = Blog.query.all()
        return render_template('blog.html', blogs=blogs)


@app.route('/newpost', methods=['POST', 'GET'])
def newpost():

    title_er = 'Your blog needs a title'
    body_er = 'Your blog needs a body'

    if request.method == 'POST':
        #grab data from forms
        blog_title = request.form['title']
        blog_body = request.form['body']

        if isEmpty(blog_title) and isEmpty(blog_body):
            return render_template('newpost.html', title_er=title_er, body_er=body_er)
        elif isEmpty(blog_title) or isEmpty(blog_body):
            if isEmpty(blog_title):
                return render_template('newpost.html', title_er=title_er)
            return render_template('newpost.html', body_er = body_er)
        else:
            new_blog = Blog(blog_title, blog_body)
            db.session.add(new_blog)
            db.session.commit()
            newID = new_blog.id
            dynamic_str = "?id=" + str(newID)

            return redirect('/blog' + dynamic_str)
             
    return render_template('newpost.html')

      




if __name__ == '__main__':
    app.run()

