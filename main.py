from uuid import uuid4
from flask import Flask
from flask import render_template

class Token:
    def __init__(self, tokenFile):
        self.tokenFile = tokenFile
    def addToken(self, tokenToAdd):
        token = [str(tokenToAdd)]
        tokenFile = open(self.tokenFile ,"w")
        tokenFile.writelines(token)
    def generateToken(self):
        return uuid4()
    def checkToken(self, tokenToBeChecked):
        tokenFile = open(self.tokenFile ,"r")
        token = (tokenFile.readlines())
        if tokenToBeChecked in token:
            return True
        else:
            return False  
    def createToken(self):
        token = self.generateToken()
        self.addToken(token)
    def tokenisation(self, token):
        if self.checkToken(token):
            self.createToken()
            return True
        else: 
            return False

from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "TOKENISATION"
@app.route('/tokenisation/<string:token>')
def tokenisation(token):
    tokenClass = Token('token.txt')
    if tokenClass.tokenisation(token):
        return render_template('200.html'), 200
    else: 
        return render_template('404.html'), 404
    

app.run()

# Usage 
# token = Token('token.txt')
# token.tokenisation('6829055c-8ffc-4a8d-a066-b43ad91b5342')
