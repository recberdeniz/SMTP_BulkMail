# This code script is written by @recberdeniz to exercise about python GUI application for Python Programming
# Before using a GUI you should check your mail provider options that could allow less secure app access
# I used hotmail/outlook mail provider and the process succeed I have also tried to send a mail with my gmail,
# but google could not allow that less secure app access.
# Receiver mail addresses should split with ",". For example; username@gmail.com, testmail@hotmail.com,...
import sys
from PyQt5 import QtWidgets
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SMTP Mail Sender")
        self.init_ui()

    def init_ui(self):
        self.mail = QtWidgets.QLabel("Mail")
        self.mailadd = QtWidgets.QLineEdit()
        self.pw = QtWidgets.QLabel("Password")
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.mailcontent_text = QtWidgets.QLabel("Mail Content")
        self.mailcontent = QtWidgets.QTextEdit()
        self.recievers_text = QtWidgets.QLabel("Recievers")
        self.recievers = QtWidgets.QTextEdit()
        self.send_button = QtWidgets.QPushButton("Send")
        self.error_txt = QtWidgets.QLabel("")
        self.subject = QtWidgets.QLabel("Subject")
        self.subject_content = QtWidgets.QLineEdit()

        v_box = QtWidgets.QVBoxLayout()

        v_box.addStretch()
        v_box.addWidget(self.mail)
        v_box.addWidget(self.mailadd)
        v_box.addWidget(self.pw)
        v_box.addWidget(self.password)
        v_box.addWidget(self.subject)
        v_box.addWidget(self.subject_content)
        v_box.addStretch()

        v_box2 = QtWidgets.QHBoxLayout()

        v_box2.addStretch()
        v_box2.addWidget(self.send_button)
        v_box2.addWidget(self.error_txt)
        v_box2.addStretch()

        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addWidget(self.mailcontent)
        h_box.addWidget(self.recievers)
        h_box.addStretch()

        h_box2 = QtWidgets.QHBoxLayout()

        h_box2.addStretch()
        h_box2.addWidget(self.mailcontent_text)
        h_box2.addStretch()
        h_box2.addWidget(self.recievers_text)
        h_box2.addStretch()

        v_box.addLayout(h_box2)
        v_box.addLayout(h_box)
        v_box.addLayout(v_box2)

        self.setLayout(v_box)

        self.send_button.clicked.connect(self.send_mail)


        self.show()

    def send_mail(self):
        ready_2_send = list()
        mail = self.mailadd.text()
        pw = self.password.text()
        subject = self.subject_content.text()
        recievers = self.recievers.toPlainText()
        mail_content = self.mailcontent.toPlainText()
        new = recievers.split(',')
        # recievers list
        for i in new:
            ready_2_send.append(i.replace(" ", ""))
        #recievers list ready to mail


        if len(mail) == 0:
            self.error_txt.setText("Mail address has not entered!")

        elif len(pw) == 0:
            self.error_txt.setText("Password has not entered!")

        elif len(subject) == 0:
            self.error_txt.setText("Subject has not entered!")

        else:
            message = MIMEMultipart()
            message["From"] = mail
            message["Subject"] = subject
            message_body = MIMEText(mail_content, "plain")
            message.attach(message_body)

            try:

                mail = smtplib.SMTP("smtp.office365.com", 587)
                mail.ehlo()
                mail.starttls()
                mail.login(message["From"], pw)
                mail.sendmail(message["From"], ready_2_send, message.as_string())
                print("Mail sended succesfully!")
                mail.close()

            except:
                sys.stderr.write("Error Occured!")
                sys.stderr.flush()


app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())


