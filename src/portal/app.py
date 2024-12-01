@app.route("/")
def timeline():
    mention = x_api.get_mentions()
    response = emotion_engine.process_interaction(mention) if mention else "No new mentions."
    return render_template("timeline.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
