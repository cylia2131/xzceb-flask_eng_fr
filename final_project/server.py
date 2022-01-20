from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation as m

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    result = m.translator.englishToFrench(textToTranslate)
    return result

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    result = m.translator.frenchToEnglish(textToTranslate)
    return result

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
