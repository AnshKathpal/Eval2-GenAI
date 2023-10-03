from flask import Flask,request,jsonify
app = Flask(__name__)

posts = []

@app.route("/post",methods = ["POST"])
def create_post():
    data = request.json
    if "content" in data:
        new_post = {"content" : data["content"]}
        posts.append(new_post)
        return jsonify({"message" : "Post Created"}),200
    return jsonify({"message" : "Invalid req data"}),400


if __name__ == "__main__":
    app.run(debug=True)