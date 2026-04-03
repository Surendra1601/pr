from flask import Flask, request

app = Flask(__name__)

@app.route("/hackaicon_ethiack_1337_lmao")
def hack():
    return f"""
    Received request from agent 🚀
    
    Headers:
    {dict(request.headers)}
    
    Args:
    {request.args}
    """