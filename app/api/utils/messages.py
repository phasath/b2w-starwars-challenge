"""Tool to allow dynamic messages to client"""

from flask import jsonify

def error_message(code: int, message: str)->jsonify:
    """A function to return a message along with the status code in case of error

    Arguments:
        code {int} -- HTTP Status Code of operation
        message {str} -- A friendly message to help understanding the problem

    Returns:
        jsonify -- the response
    """
    message = {
                "err":
                {
                    "msg": f"{message}"
                }
                }

    resp = jsonify(message)
    resp.status_code = code
    return resp

def success_message(code: int, data: [dict, list])->jsonify:
    """A function to return a status code and the data to the request

    Arguments:
        code {int} -- HTTP Status Code of operation
        data {[type]} -- The data resulted from the operation

    Returns:
        jsonify -- the response
    """

    resp = jsonify(data)
    resp.status_code = code
    return resp
