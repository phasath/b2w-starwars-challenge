"""Tool to allow dynamic messages to client"""

from flask import jsonify

def error_message(code:int, message:str)->jsonify:
    message = {
                "err":
                    {
                        "msg": f"{message}"
                    }
                }

    resp = jsonify(message)
    resp.status_code = code 
    return resp