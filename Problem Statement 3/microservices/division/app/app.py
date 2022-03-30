from flask import Flask
from flask_restful import Resource,Api


class Division(Resource):
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
        if(num2 == 0):
            return {"error":True,"errMsg":"Zero Division Error"}
        return {"error":False,"result":num1/num2}

app = Flask(__name__)
api = Api(app)
api.add_resource(Division, "/<string:argument0>/<string:argument1>")

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5054,
        host="0.0.0.0"
    )