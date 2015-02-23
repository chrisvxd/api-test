


def functional_method(first_arg, second_arg='Test'):
    """
    @api {get} functional_method(first_arg,second_arg) Functional Method
    @apiName FunctionalMethod
    @apiGroup TestApi

    @apiDescription This is a test apiDoc method. This should be the description.

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
