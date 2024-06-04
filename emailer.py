import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define your email server and login credentials
SMTP_SERVER = 'smtp.mail.yahoo.com'
SMTP_PORT = 587
SMTP_USER = 'your-email@yahoo.com'
SMTP_PASSWORD = 'your-password'

# List of universities with their email addresses
universities = [
    {"name": "University of Edinburgh", "email": "futurestudents@ed.ac.uk"},
    {"name": "ETH Zurich", "email": "admissions@ethz.ch"},
    {"name": "University of Zurich", "email": "studiensekretariat@uzh.ch"},
    {"name": "University of Amsterdam", "email": "admissions@uva.nl"},
    {"name": "Leiden University", "email": "study@leiden.edu"},
    {"name": "University of Copenhagen", "email": "studyprogrammes@adm.ku.dk"},
    {"name": "Lund University", "email": "admissions@lu.se"},
    {"name": "Uppsala University", "email": "admissions@uu.se"},
    {"name": "University of Helsinki", "email": "admissions@helsinki.fi"},
    {"name": "Aarhus University", "email": "bss@au.dk"},
    {"name": "University of Tokyo", "email": "international@gs.mail.u-tokyo.ac.jp"},
    {"name": "Kyoto University", "email": "gakusei-kousei@admin.kyoto-u.ac.jp"},
    {"name": "National University of Singapore (NUS)", "email": "askadmissions@nus.edu.sg"},
    {"name": "Nanyang Technological University (NTU)", "email": "adm_local@ntu.edu.sg"},
    {"name": "University of Hong Kong (HKU)", "email": "admissions@hku.hk"},
    {"name": "Chinese University of Hong Kong (CUHK)", "email": "ugadm@cuhk.edu.hk"},
    {"name": "Seoul National University", "email": "admissions@snu.ac.kr"},
    {"name": "Korea University", "email": "admission@korea.ac.kr"},
    {"name": "Yonsei University", "email": "admission@yonsei.ac.kr"},
    {"name": "University of Auckland", "email": "int-questions@auckland.ac.nz"},
    {"name": "Victoria University of Wellington", "email": "international@vuw.ac.nz"},
    {"name": "University of Cape Town", "email": "admissions@uct.ac.za"},
    {"name": "University of Pretoria", "email": "csc@up.ac.za"},
    {"name": "University of São Paulo", "email": "uspint@usp.br"},
    {"name": "University of Buenos Aires", "email": "secgrad@rec.uba.ar"},
    {"name": "Universidad de Chile", "email": "admision@uchile.cl"},
    {"name": "University of Queensland", "email": "admissions@uq.edu.au"},
    {"name": "Monash University", "email": "study@monash.edu"},
    {"name": "Australian National University", "email": "international.admissions@anu.edu.au"},
    {"name": "University of Western Australia", "email": "admissions@uwa.edu.au"},
    {"name": "University of Alberta", "email": "regrec@ualberta.ca"},
    {"name": "University of Ottawa", "email": "admissions@uottawa.ca"},
    {"name": "York University", "email": "futurestudents@yorku.ca"},
    {"name": "University of Warwick", "email": "ugadmissions@warwick.ac.uk"},
    {"name": "University of Manchester", "email": "admissions@manchester.ac.uk"},
    {"name": "King's College London", "email": "undergraduate.admissions@kcl.ac.uk"},
    {"name": "University of Glasgow", "email": "student.recruitment@glasgow.ac.uk"},
    {"name": "Durham University", "email": "undergraduate.admissions@durham.ac.uk"},
    {"name": "University of Birmingham", "email": "admissions@contacts.bham.ac.uk"},
    {"name": "Trinity College Dublin", "email": "admissions@tcd.ie"},
    {"name": "University College Dublin", "email": "internationaladmissions@ucd.ie"},
    {"name": "University of Limerick", "email": "admissions@ul.ie"},
    {"name": "Vrije Universiteit Amsterdam", "email": "admissions@vu.nl"},
    {"name": "Delft University of Technology", "email": "contactcentre-esa@tudelft.nl"},
    {"name": "Erasmus University Rotterdam", "email": "admission@eur.nl"},
    {"name": "KU Leuven", "email": "admissions@kuleuven.be"},
]

# Email template
email_template = """
Subject: Inquiry Regarding Admissions, Scholarships, and Prerequisites for International Students

Dear Admissions Team,

I hope this email finds you well. My name is [your name here], and I am writing to inquire about the admissions process, available scholarships, and any prerequisites or exceptions for international students interested in studying at {school_name}.

As an international student seeking to further my education, I am particularly interested in {school_name}'s renowned academic programs and its commitment to supporting diverse student populations. I have carefully reviewed the information available on your website, but I would greatly appreciate more detailed guidance on the following points:

Admissions Process: Could you please provide information on the specific steps and requirements for international students to apply for admission to {school_name}? Additionally, I would like to know if there are any deadlines or additional documents I should be aware of during the application process.

Scholarship Opportunities: I am keenly interested in any scholarships or financial aid options available for international students. Could you kindly provide details on the scholarships offered by {school_name}, including eligibility criteria, application procedures, and deadlines?

Prerequisites and Exceptions: As a foreign student with unique circumstances, I am curious to know if there are any specific prerequisites for admission or any exceptions made for applicants facing challenges such as disabilities or lack of previous university experience. Understanding any flexibility in the admissions criteria would be immensely helpful.

Support Services for International Students: Lastly, I would appreciate information on the support services available to international students at {school_name}, including assistance with visa applications, housing options, academic advising, and any resources for students with disabilities.

I understand that you may receive numerous inquiries, but any assistance or guidance you could provide would be invaluable to me as I navigate the process of applying to universities abroad. I am genuinely excited about the possibility of studying at {school_name} and contributing to its vibrant academic community.

Thank you for your time and attention to my inquiry. I look forward to hearing from you soon.

Warm regards,

[your name here]
[addy]
[contact email]
[contact phone number]
"""

def send_email(to_email, subject, body):
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = SMTP_USER
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        # Connect to the email server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SMTP_USER, to_email, msg.as_string())
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

def main():
    subject = "Inquiry Regarding Admissions, Scholarships, and Prerequisites for International Students"

    for university in universities:
        school_name = university["name"]
        to_email = university["email"]

        # Fill in the email template with the school name
        body = email_template.format(school_name=school_name)

        # Send the email
        send_email(to_email, subject, body)

if __name__ == "__main__":
    main()
