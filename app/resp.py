from flask import jsonify


def succeed(data):
    return jsonify({
        "code": 0,
        "message": None,
        "data": data
    })


def fail(code: int, message: str):
    return jsonify({
        "code": code,
        "message": message
    })
