def run(request):
    data = request.json['data']

    # Call a domain function
    
    response = {
        'status': True,
        'message': 'The echo data was readed with sucess',
        'return': data
    }

    return response