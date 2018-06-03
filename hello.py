def application(environ, start_response):
	out = "\n".join(environ.get('QUERY_STRING').split("&"))
	start_response('200 OK', [('Content-Type', 'text/plain')])
	return [out] 
