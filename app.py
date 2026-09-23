import flask
import requests

app = flask.Flask(__name__)

token_mandae = 'COLOCAR O TOKEN'
token_braspress = 'COLOCAR O TOKEN'


@app.route("/", methods=["GET", "POST"])
def inicio():
    if flask.request.method == "POST":
        # nf = flask.request.form["nf"]
        # id = flask.request.form["id"]
        codigo = flask.request.form["codigo"]

        url = f"https://api.mandae.com.br/v2/trackings/{codigo}"

        resposta = requests.get(
            url,
            headers={
                "Authorization": token_mandae
            }
        )

        print(resposta.status_code)

        dados = resposta.json()

        codigo_rastreio = dados["trackingCode"]
        eventos = dados["events"]

        return flask.render_template(
            "index.html",
            codigo=codigo_rastreio,
            eventos=eventos
        )

    return flask.render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)