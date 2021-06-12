from flask import Flask, render_template, jsonify, request


app = Flask(__name__)

#To receive form data
@app.route('/')
def theform():
    
     form = '''<form method="POST" action ="/test">
                 <input type="text" name = "string_to_cut">
                 <input type = "submit" value = "Submit"> 
                 </form>'''

     return form



#To output form data        
@app.route('/test', methods= ['POST','GET'])
def json():
     thirdChar = ""
     value = request.form['string_to_cut']    
     #To obtain every third letter
     counter = 0
     for i in range(len(value)):
          counter+=1
          if counter%3 != 0 and counter!=0:
               continue
               
          else:
               thirdChar += value[i]
              
     
     return jsonify({"return_string" : thirdChar})



    
if __name__ == '__main__':
    app.run(debug=True)

    