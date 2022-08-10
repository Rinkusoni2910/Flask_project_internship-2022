#step 1
from flask import Flask, render_template,request
import re

#step2
app=Flask(__name__)

#step 3
@app.route('/',methods=['POST','GET'])
def match():
    if request.method=='POST':
        Regular_Expression=request.form['regex']
        Input_String=request.form['string']
        c=0
        result_list=[]
        for match_ele in re.finditer(r"{}".format(Regular_Expression),Input_String):
            match_string=""
            match_string=match_string+"Match no.{}: The Regular Expression: \"{}\" starts at index: \"{}\" and ends at index: \"{}\"".format(c,match_ele.group(),match_ele.start(),match_ele.end())
            result_list.append(match_string)
            c=c+1
        return render_template("Matched_String.html",Print="Match Found!",regex=Regular_Expression,string=Input_String,count=c,eles=result_list)
    return render_template("Matched_String.html",count=-1)

#step 4
if __name__=='__main__':
    app.run(debug=True)