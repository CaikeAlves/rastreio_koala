import flask
import requests

app = flask.Flask(__name__)

token_mandae = "COLOCAR_TOKEN_AQUI"


@app.route("/", methods=["GET", "POST"])
def inicio():
    if flask.request.method == "POST":
        # nf = flask.request.form["nf"]
        # id = flask.request.form["id"]
        codigo = flask.request.form["codigo"]

        url = f"https://api.mandae.com.br/v2/trackings/{codigo}"

        # resposta = requests.get(
        #     url,
        #     headers={
        #         "Authorization": token_mandae
        #     }
        # )

        # print(resposta.status_code)

        # dados = resposta.json()
        dados = {
            "trackingCode": "KOALA001351",
            "events": [
                {
                    "date": "2026-09-05 00:52",
                    "name": "Encomenda coletada",
                    "description": "Sua encomenda está em processo de separação e logo será encaminhada para a transportadora."
                }
            ]
        }

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