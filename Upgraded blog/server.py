from flask import Flask, render_template, request
import requests
from post import Post

app = Flask(__name__)

# ----------------------CREATING AN INDIVIDUAL OBJECT FOR EACH BLOGPOSTS--------#
posts = requests.get("https://api.npoint.io/7d13965a4fc4073ff6d5").json()


# print(posts)
# for post in posts:
#     post_obj = Post(post['id'], post['body'], post['title'], post['subtitle'])
#     all_formatted_posts.append(post_obj)


@app.route("/")
def homepage():
    return render_template("index.html", blog_post=posts)


# ------------------------for  about page and contact page---------------------#
@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


# ------------------------for rendering the post-------------------------------#
@app.route("/post/<int:index>")
def get_post(index):
    chosen_post = None
    for post in posts:
        if post['id'] == index:
            chosen_post = post
    return render_template("post.html", blog=chosen_post)


# ------------------------getting the contact form to post the entry received-------------------------------#

@app.route("/contact", methods=['POST', 'GET'])
def get_request():
    if request.method == "POST":
        name = request.form['username']
        email = request.form['email']
        phone_number = request.form['phone_number']
        message = request.form['message']
        print(f"{name}\n {email}\n {phone_number}\n {message}")
        return render_template("contact.html", message_sent=True)
    return render_template("contact.html", message_sent= False)


if __name__ == "__main__":
    app.run(debug=True)
