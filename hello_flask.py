from flask import Flask, render_template, request,escape

app = Flask(__name__)

def logg(req: 'flask_request', res: str) -> None:
   with open('tes.log', 'a') as log:
      print( res, file=log, end='|')



@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
   return render_template('entry.html',
                          the_title='Welcome'
                          )


@app.route('/log',methods=['POST'])
def result_page() -> 'html':
   s=[]
   link = request.form['link']
   title = 'Here are your results:'
   results = str(link)
   logg(request,results)
   with open('tes.log') as log:
      for f in log:
         for ff in f.split('|'):
            s.append(escape(ff))               
   titles = ('YTLink',)
   return render_template('viewlog.html',
                           the_title='Here are your Results',
                           the_row_titles=titles,
                           the_data=s,)

if __name__ == '__main__':
   app.run(port=8080,debug=True)
             
