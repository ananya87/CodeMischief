#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request, flash
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask("__name__")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('postgresql://postgresql:20122012@localhost:5432/logs?sslmode=require')

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)


# In[ ]:


class Logg(db.Model):
    __tablename__ = 'Logging'
   
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String,nullable=False)
    message = db.Column(db.String,nullable=False)
    module=db.Column(db.String,nullable=False)
    
    def __init__(self, level, message, module):
        self.level=level
        self.message=message
        self.module=module
        
@app.route('/todo/api/v1.0/log/<string:level>/<string:message>/<string:module>',methods=["GET"])

def insertuser(level,message,module):

    newlevel =level
    newmessage=message
    newmodule=module
    log_record=Logg(newlevel, newmessage, newmodule)
    #db.execute("INSERT INTO Logging (level, ,message, module) VALUES (:newlevel, :newmessage,:newmodule)",
            #{"level": newlevel, "message": newmessage, "module":newmodule}) 
    db.session.add(log_record)
    db.session.commit()
    
    print(newlevel,newmessage,newmodule)
    print(log_record)
    
    return ('done')

if __name__ == '__main__':
        app.run(debug=True,use_reloader=False)
  

    
    


# In[ ]:




