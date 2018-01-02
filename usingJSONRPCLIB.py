import jsonrpclib

url = "http://%s:%s/jsonrpc" % (HOST,PORT)
server = jsonrpclib.Server(url)
uid = server.call(service="common", method="login", args=[DB,USER,PASS])

def invoke(model, method, *args):
    args = [DB,uid,PASS,model,method] + list(args)
    return server.call(service = "object", method="execute", args= args)

args={
    'color': 8,
    'memo' : 'This is another note',
    'create_uid' : uid,
}
note_id = invoke('note.note', 'create', args)