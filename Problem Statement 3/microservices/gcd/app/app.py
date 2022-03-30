from flask import Flask
from flask_restful import Resource,Api


class GCD(Resource):
    def hcf(self,a,b):
        if a == 0 :
            return b     
        return self.hcf(b%a, a)
        
    def get(self,argument0,argument1):
        try:
            num1 = int(argument0)
            num2 = int(argument1)
        except ValueError:
            return {"error":True,"errMsg":"Invalid number entered"}
        return {"error":False,"result":self.hcf(num1,num2)}

app = Flask(__name__)
api = Api(app)
api.add_resource(GCD, "/<string:argument0>/<string:argument1>")

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5056,
        host="0.0.0.0"
    )