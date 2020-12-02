from flask import Flask, render_template, url_for, request

app = Flask(__name__)

book=[
	{
		'id': 1,
		'title': 'un titre',
	},
	{
		'id': 2,
		'title': 'un autre titre random',
	}
]

# Page d'accueil
@app.route("/")
def index():
    return render_template('index.html')

# Retourne tous les livres
@app.route("/books", methods=["GET"])
def get_books():
    pass

# Retourne un livre selon son id
@app.route("/book/<int:id>", methods=["GET"])
def get_book_by_id():
    pass

# Retourne un livre selon son titre
@app.route("/book/<title>", methods=["GET"])
def get_book_by_title():
    pass

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
