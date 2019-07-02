from flask import jsonify, request
import application.api.echo as apiEcho
import infra.http.auth as auth
import config


@config.app.route("/", methods=['GET'])
def hello():
    return "<h1 style='color:blue'>Olá Andre!! Isso foi Atualizado com CI/CD</h1>"
