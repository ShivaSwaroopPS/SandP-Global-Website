from flask import Flask, jsonify, render_template ,Response 


app= Flask(__name__)

JOBS = [
  {
    'Req ID': '296419',
    'Title': 'Software Quality Analyst',
    'Location': 'Bengaluru, India',
    'Category': 'Information Technology',
    'Posted On': '02/28/2024'
  },
  {
    'Req ID': '296398',
    'Title': 'Python Developer',
    'Location': 'Bengaluru, India',
    'Category': 'Information Technology',
    'Posted On': '02/13/2024'
  },
  {
    'Req ID': '295673',
    'Title': 'Senior SRE Engineer - Data Platforms',
    'Location': 'Bengaluru, India',
    'Category': 'Information Technology',
    'Posted On': '01/28/2024'
  },
  {
    'Req ID': '295991',
    'Title': 'DTS Service Delivery Manager (SDM)',
    'Location': 'Bengaluru, India',
    'Category': 'Information Technology',
    'Posted On': '01/23/2024'
  },
  {
    'Req ID': '293205',
    'Title': 'Sr Software Engineer',
    'Location': 'Bengaluru, India',
    'Category': 'Information Technology',
    'Posted On': '01/18/2024'
  },
  {
    'Req ID': '295614',
    'Title': 'Data Scientist',
    'Location': 'Bengaluru, India',
    'Category': 'Information Technology',
    'Posted On': '12/19/2023'
  },
  {
    'Req ID': '295134',
    'Title': 'Data Engineer',
    'Location': 'Bengaluru, India',
    'Category': 'Information Technology',
    'Posted On': '12/14/2023'
  },
  {
    'Req ID': '295136',
    'Title': 'Sr Data Engineer',
    'Location': 'Bengaluru, India',
    'Category': 'Information Technology',
    'Posted On': '12/14/2023'
  },
  {
    'Req ID': '294941',
    'Title': 'Cloud Architect/Engineer',
    'Location': 'Bengaluru, India',
    'Category': 'Information Technology',
    'Posted On': '12/13/2023'
  }

]

@app.route("/")
def hello():
  return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)