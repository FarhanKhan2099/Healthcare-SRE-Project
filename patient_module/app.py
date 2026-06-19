from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://appuser:App%402026!@localhost/healthcare_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Patient(db.Model):
    __tablename__ = 'patients'
    patient_id  = db.Column(db.Integer, primary_key=True)
    full_name   = db.Column(db.String(100), nullable=False)
    phone       = db.Column(db.String(20))
    blood_group = db.Column(db.String(5))
    age         = db.Column(db.Integer)
    address     = db.Column(db.String(200))
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/api/v1/patients', methods=['POST'])
def create_patient():
    data = request.get_json()
    patient = Patient(
        full_name   = data['full_name'],
        phone       = data.get('phone'),
        blood_group = data.get('blood_group'),
        age         = data.get('age'),
        address     = data.get('address')
    )
    db.session.add(patient)
    db.session.commit()
    return jsonify({'message': 'Patient created', 'patient_id': patient.patient_id}), 201

@app.route('/api/v1/patients', methods=['GET'])
def get_all_patients():
    patients = Patient.query.all()
    return jsonify([{
        'patient_id':  p.patient_id,
        'full_name':   p.full_name,
        'phone':       p.phone,
        'blood_group': p.blood_group,
        'age':         p.age
    } for p in patients])

@app.route('/api/v1/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    p = Patient.query.get_or_404(patient_id)
    return jsonify({
        'patient_id':  p.patient_id,
        'full_name':   p.full_name,
        'phone':       p.phone,
        'blood_group': p.blood_group,
        'age':         p.age,
        'address':     p.address
    })

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5001, debug=True)
