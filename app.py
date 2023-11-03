from flask import Flask, render_template, request, jsonify
from ice_breaker import ice_break

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# Route to handle the POST request for processing person information
@app.route("/process", methods=["POST"])
def process():
    """
    Process the POST request to obtain information about a person.
    Expects 'name' and 'company' fields in the form data.

    Returns a JSON response containing person information and profile picture URL.
    """
    name = request.form["name"]

    # Retrieve person information and profile picture URL using ice_break function
    person_info, profile_pic_url = ice_break(name=name, company=company)

    # Return a JSON response with person information and profile picture URL
    return jsonify({
        "summary": person_info.summary,
        "interests": person_info.topics_of_interest,
        "facts": person_info.facts,
        "ice_breakers": person_info.ice_breakers,
        "picture_url": profile_pic_url,
    })

if __name__ == "__main__":
    # Run the Flask app on host 0.0.0.0 and enable debugging
    app.run(host="0.0.0.0", debug=True, port=3000)
