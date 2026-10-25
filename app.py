from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Patient Portal Routes
@app.route('/patient-register', methods=['GET', 'POST'])
def patient_register():
    if request.method == 'POST':
        return redirect(url_for('health_profile'))
    return render_template('patient_register.html')

@app.route('/health-profile', methods=['GET', 'POST'])
def health_profile():
    if request.method == 'POST':
        return redirect(url_for('patient_dashboard'))
    return render_template('health_profile.html')

@app.route('/patient-dashboard')
def patient_dashboard():
    return render_template('patient_dashboard.html', active_tab='overview')

@app.route('/patient-dashboard/screening')
def dashboard_screening():
    return render_template('patient_dashboard.html', active_tab='screening')

@app.route('/patient-dashboard/reports')
def dashboard_reports():
    return render_template('patient_dashboard.html', active_tab='reports')

@app.route('/patient-dashboard/risk-calculator')
def dashboard_risk():
    return render_template('patient_dashboard.html', active_tab='risk')

@app.route('/patient-dashboard/appointments')
def dashboard_appointments():
    return render_template('patient_dashboard.html', active_tab='appointments')

@app.route('/patient-dashboard/reminders')
def dashboard_reminders():
    return render_template('patient_dashboard.html', active_tab='reminders')

@app.route('/patient-dashboard/diet-lifestyle')
def dashboard_diet():
    return render_template('patient_dashboard.html', active_tab='diet')

@app.route('/patient-dashboard/clinics')
def dashboard_clinics():
    return render_template('patient_dashboard.html', active_tab='clinics')

@app.route('/patient-dashboard/profile')
def dashboard_profile():
    return render_template('patient_dashboard.html', active_tab='profile')

# Doctor Portal Routes
@app.route('/doctor-login', methods=['GET', 'POST'])
def doctor_login():
    if request.method == 'POST':
        return redirect(url_for('doctor_dashboard'))
    return render_template('doctor_login.html')

@app.route('/doctor-dashboard')
def doctor_dashboard():
    return render_template('doctor_dashboard.html', active_tab='queue')

@app.route('/doctor-dashboard/review')
def doctor_review():
    return render_template('doctor_dashboard.html', active_tab='review')

@app.route('/doctor-dashboard/prescription')
def doctor_prescription():
    return render_template('doctor_dashboard.html', active_tab='prescription')

@app.route('/doctor-dashboard/referral')
def doctor_referral():
    return render_template('doctor_dashboard.html', active_tab='referral')

@app.route('/doctor-dashboard/analytics')
def doctor_analytics():
    return render_template('doctor_dashboard.html', active_tab='analytics')

@app.route('/doctor-dashboard/teleconsult')
def doctor_teleconsult():
    return render_template('doctor_dashboard.html', active_tab='teleconsult')

if __name__ == '__main__':
    app.run(debug=True)