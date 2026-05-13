from flask import jsonify


def respOf(code: int, message: str, data):
    return jsonify({
        "code": code,
        "message": message,
        "data": data
    })
