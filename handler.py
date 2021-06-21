from flask_restful import Resource, reqparse

ARGUMENT_STRING_TO_CUT = "string_to_cut"
KEY_RETURN_STRING = "return_string"


class Handler(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(ARGUMENT_STRING_TO_CUT, type=str, help='String to cut')

    def post(self):
        args = self.parser.parse_args(strict=True)
        if args[ARGUMENT_STRING_TO_CUT]:
            return {KEY_RETURN_STRING: args[ARGUMENT_STRING_TO_CUT][2::3]}, 200
        return {'message': 'Invalid request: {} is None'.format(ARGUMENT_STRING_TO_CUT)}, 400
