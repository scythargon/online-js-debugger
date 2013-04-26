from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def hello():
	print '\n\n\n\n\n\n'
	#print dir(request.args)
	args = request.args.to_dict()
	ret = out = str(args)
	if args.has_key('error'):
		error = args['error']
		ret = 'console.log("' + error + '")'
		out = '\n'.join(error.split('|'))
	
	print out
	

	return Response(ret, mimetype='application/json')

if __name__ == "__main__":
    app.run(debug = True,host='0.0.0.0')