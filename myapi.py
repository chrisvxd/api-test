def do_some_stuff(first_arg, second_arg='Test'):
    """
    @api {get} /user/:id Request User information
    @apiName GetUser
    @apiGroup User

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
