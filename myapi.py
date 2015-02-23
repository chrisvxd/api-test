


def functional_method(first_arg, second_arg='Test'):
    """
    @api {fn} functional_method Functional Method
    @apiName FunctionalMethod
    @apiGroup TestApi

    @apiParam {Number} first_arg Some number.
    @apiParam {String} [second_arg] Some string.

    @apiExample {python} Example usage:
        functional_method(5, "This is cool")

    @apiSuccessExample {json} Success
        {
            "firstname": 5,
            "lastname": "This is cool"
        }

    """

    return {
        'first_arg': first_arg,
        'second_arg': second_arg
    }
