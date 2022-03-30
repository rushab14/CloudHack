from flask import Flask
from flask_restful import Resource,Api


class Equals(Resource):
    def get(self,argument0,argument1):
        try:
            if('.' in argument0):
                num1 = float(argument0)
            else:
                num1 = int(argument0)
            if('.' in argument1):
                num2 = float(argument1)
            else:
                num2 = int(argument1)
        except ValueError:
            return {"error":True,"errMsg":"Invalid number entered"}
        return {"error":False,"result":num1==num2}

app = Flask(__name__)
api = Api(app)
api.add_resource(Equals, "/<string:argument0>/<string:argument1>")

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5061,
        host="0.0.0.0"
    )