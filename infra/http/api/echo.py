from flask import jsonify, request
import application.api.echo as apiEcho
import infra.http.auth as auth
import config


@config.app.route('/api/v1/echo', methods=['POST'])
@auth.requires_auth
def request_echo():
    try:
        if request.content_type == 'application/json':
            # Verify Body
            if not('data' in request.json):
                raise ValueError('Specify key data in Body')
        else:
            raise ValueError('The Content-Type is invalid')

        response = apiEcho.run(request)
        return jsonify(response), 200
    except Exception as err:
        print(err)
        response = {
            'status': False,
            'message': err.args[0]
        }
        print(response)
        return jsonify(response), 500