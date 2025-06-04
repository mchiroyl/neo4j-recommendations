

from flask import Flask, render_template, request
from neo4j import GraphDatabase

app = Flask(__name__)

# Conexión a la base de datos demo
URI = "neo4j+s://demo.neo4jlabs.com:7687"
USERNAME = "recommendations"
PASSWORD = "recommendations"

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

# Recomendaciones por usuario
def get_user_recommendations(user_id):
    with driver.session(database="recommendations") as session:
        query = """
        MATCH (u:User) WHERE u.userId = $userId
        MATCH (u)-[:RATED]->(m:Movie)<-[:RATED]-(other:User)-[:RATED]->(rec:Movie)
        WHERE NOT (u)-[:RATED]->(rec)
        RETURN DISTINCT rec.title AS title, rec.released AS released
        ORDER BY rec.released DESC
        LIMIT 10
        """
        result = session.run(query, userId=user_id)
        return [{"title": r["title"], "released": r["released"]} for r in result]

# Recomendaciones por película
def get_movie_recommendations(title):
    with driver.session(database="recommendations") as session:
        query = """
        MATCH (m:Movie {title: $title})<-[:RATED]-(u:User)-[:RATED]->(rec:Movie)
        WHERE rec <> m
        RETURN DISTINCT rec.title AS title, rec.released AS released
        ORDER BY rec.released DESC
        LIMIT 10
        """
        result = session.run(query, title=title)
        return [{"title": r["title"], "released": r["released"]} for r in result]

@app.route("/", methods=["GET", "POST"])
def index():
    user_recs = []
    movie_recs = []
    user_id = ""
    movie_title = ""

    if request.method == "POST":
        if "user_id" in request.form:
            user_id = request.form["user_id"].strip()
            user_recs = get_user_recommendations(user_id)
        if "movie_title" in request.form:
            movie_title = request.form["movie_title"].strip()
            movie_recs = get_movie_recommendations(movie_title)

    return render_template("index.html",
                           user_recs=user_recs,
                           movie_recs=movie_recs,
                           user_id=user_id,
                           movie_title=movie_title)

if __name__ == "__main__":
    app.run(debug=True)
