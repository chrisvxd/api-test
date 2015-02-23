def restful_method(id):
    """
    @api {get} /user/:id Request User information
    @apiName GetUser
    @apiGroup TestApi

    @apiParam {Number} id Users unique ID.

    @apiExample {shell} Example usage:
        curl -i http://localhost/user/4711

    @apiSuccessExample {json} 200 Success-Response
        HTTP/1.1 200 OK
        {
            "firstname": "John",
            "lastname": "Doe"
        }

    @apiErrorExample {json} 404 Error-Response
        HTTP/1.1 404 Not Found
        {
            "error": "UserNotFound"
        }

    """

    return None


def functional_method(first_arg, second_arg='Test'):
    """
    @api {get} functional_method Functional Method
    @apiName FunctionalMethod
    @apiGroup TestApi

    @apiParam {Number} first_arg Some number.
    @apiParam {String} [second_arg] Some string.

    @apiExample {python} Example usage:
        functional_method(5, "This is cool")

    @apiSuccessExample {json} Success-Response
        {
            "firstname": 5,
            "lastname": "This is cool"
        }

    """

    return {
        'first_arg': first_arg,
        'second_arg': second_arg
    }
