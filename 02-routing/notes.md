# Day 2: Flask Routing (static + Dynamic)  
  
## What is Routing?  
Routing connects URLs (like /home, /about) to Python functions (called **view functions**).  

## Static Route  
@app.route("/about")  
def about():  
    return "This is the about page."  
  
##Dynamic Route  
@app.route("/user/&lt;username&gt;")  
def greet(username):  
    return f"Hello, {username}!"  
  
## Type-Specific Route  
@app.route("/post/&lt;int:post_id&gt;")  
def show_post(post_id):  
    return f"Post ID: {post_id}"  