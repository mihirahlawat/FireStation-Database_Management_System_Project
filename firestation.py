from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import pymysql.cursors
import datetime
import time
from xlrd import *
from xlsxwriter import *


from PyQt5.uic import loadUiType

ui,_ = loadUiType('firestation.ui')
login_ui,_ = loadUiType('loginportal.ui')
user_ui,_ = loadUiType('user_report.ui')

class LoginPage(QMainWindow, login_ui):
	def __init__(self):
		QMainWindow.__init__(self)
		self.setupUi(self)
		self.Handle_Buttons()
		self.style_3()

	def Handle_Buttons(self):
		self.createAccount.clicked.connect(self.create)
		self.cr_clear.clicked.connect(self.create_clr)
		self.log_in.clicked.connect(self.login)
		self.log_clear.clicked.connect(self.login_clr)

	# def dark(self):
	# 	style = open('Themes/dark.css', 'r')
	# 	style = style.read()
	# 	self.setStyleSheet(style)

	# def light(self):
	# 	style = open('Themes/light.css', 'r')
	# 	style = style.read()
	# 	self.setStyleSheet(style)

	# def style_2(self):
	# 	style = open('Themes/style_2.css', 'r')
	# 	style = style.read()
	# 	self.setStyleSheet(style)

	def style_3(self):
		style = open('Themes/style_3.css', 'r')
		style = style.read()
		self.setStyleSheet(style)

	# def style_4(self):
	# 	style = open('Themes/style_4.css', 'r')
	# 	style = style.read()
	# 	self.setStyleSheet(style)

	# def style_5(self):
	# 	style = open('Themes/style_5.css', 'r')
	# 	style = style.read()
	# 	self.setStyleSheet(style)

	def adminpass(self):
		self.window = MainApp()
		self.close()
		self.window.show()

	def userpass(self):
		self.window = UserPage(self)
		self.close()
		self.window.show()

	def create(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()

	    nam = self.firstname.text()
	    user = self.cr_username.text()
	    passw = self.cr_password.text()
	    cont = self.contact_line.text()
	    if self.type_admin.isChecked():
	    	self.cur.execute('''INSERT INTO admins (name,username,password)
	    	    VALUES (%s,%s,%s);
	    	    ''',(nam,user,passw))
	    	self.db.commit()
	    	self.statusBar().showMessage('Account Created')

	    if self.type_user.isChecked():
	    	self.cur.execute('''INSERT INTO users (name,username,password,contact)
	    	    VALUES (%s,%s,%s,%s);
	    	    ''',(nam,user,passw,cont))
	    	self.db.commit()
	    	self.statusBar().showMessage('Account Created')

	    self.firstname.setText('')
	    self.cr_username.setText('')
	    self.cr_password.setText('')
	    self.contact_line.setText('')		

	def create_clr(self):
		self.firstname.setText('')
		self.cr_username.setText('')
		self.cr_password.setText('')
		self.contact_line.setText('')

	def login(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()

	    user = self.log_username.text()
	    password = self.log_password.text()

	    self.cur.execute('''SELECT * FROM admins WHERE username=%s AND password=%s;''',(user,password))
	    data = self.cur.fetchone()
	    if data != None:
	    	self.adminpass()
	    else:
	    	self.cur.execute('''SELECT * FROM users WHERE username=%s AND password=%s;''',(user,password))
	    	self.data = self.cur.fetchone()
	    	if self.data != None:
	    		print('found')
	    		self.userpass()
	    	else:
	    		self.label_11.setText('Make sure you entered your username and password correctly')

	def login_clr(self):
		self.log_username.setText('')
		self.log_password.setText('')



#################################################################
#################################################################
#################################################################



class UserPage(QMainWindow, user_ui):
	def __init__(self, parent):
		QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.parent = parent
		self.Handle_UI_Changes()
		self.Handle_Buttons()

	def Handle_UI_Changes(self):
		self.tabWidget.tabBar().setVisible(False)
		data = self.parent.data
		self.user = data
		self.style_3()
		self.label_6.setText('WELCOME '+str(self.user[0]))
		self.firstname.setText(self.user[0])
		self.contact_line.setText(str(self.user[3]))

	def Handle_Buttons(self):
		self.pushButton.clicked.connect(self.open_home)
		self.pushButton_4.clicked.connect(self.open_report)
		self.pushButton_30.clicked.connect(self.open_settings)
		self.pushButton_15.clicked.connect(self.logout)

		self.pushButton_12.clicked.connect(self.add_report)
		self.pushButton_16.clicked.connect(self.add_clr)

		self.pushButton_13.clicked.connect(self.update_user)
		self.pushButton_17.clicked.connect(self.update_clr)

	def style_3(self):
		style = open('Themes/style_3.css', 'r')
		style = style.read()
		self.setStyleSheet(style)
	

	###########################
	########### Tabs ##########
	def open_home(self):
	    self.tabWidget.setCurrentIndex(0)
	def open_report(self):
	    self.tabWidget.setCurrentIndex(1)
	def open_settings(self):
	    self.tabWidget.setCurrentIndex(2)


	###########################
	########### Home ##########
	def logout(self):
		self.window = LoginPage()
		self.close()
		self.window.show()


	###########################
	########## Report #########
	def add_report(self):
		self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
		self.cur = self.db.cursor()

		street = self.lineEdit_22.text()
		city = self.lineEdit_20.text()
		state = self.lineEdit_23.text()
		pin = self.lineEdit_21.text()
		descrip = self.textEdit.toPlainText()
		date = time.strftime('%Y-%m-%d %H:%M:%S')

		self.cur.execute('''INSERT INTO reports (STREET_ADDR,CITY,STATE,PINCODE,DESCRIP,INFO_NAME,INFO_NUM,DATE_TIME)
	        VALUES (%s,%s,%s,%s,%s,%s,%s,%s);
	        ''',(street,city,state,pin,descrip,self.user[0],self.user[3],date))
		self.db.commit()
		self.statusBar().showMessage('Report Submitted')

		self.lineEdit_22.setText('')
		self.lineEdit_20.setText('')
		self.lineEdit_23.setText('')
		self.lineEdit_21.setText('')
		self.textEdit.setPlainText('')

	def add_clr(self):
		self.lineEdit_22.setText('')
		self.lineEdit_20.setText('')
		self.lineEdit_23.setText('')
		self.lineEdit_21.setText('')
		self.textEdit.setPlainText('')


	###########################
	###### User Settings ######
	def update_user(self):
		self.label_12.setText('')
		self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
		self.cur = self.db.cursor()
		nam = self.firstname.text()
		passw = self.cr_password.text()
		passw2 = self.cr_password_2.text()
		cont = self.contact_line.text()
		if passw == '' or passw2 == '':
			self.label_12.setText('Passwords cannot be empty')
		else:
			if passw == passw2:
				self.cur.execute(''' UPDATE users SET name=%s,password=%s,contact=%s
		    		WHERE username=%s;
		    		''',(nam,passw,cont,self.user[1]))
				self.db.commit()
				self.statusBar().showMessage('Details Updated')
			else:
				self.label_12.setText('Passwords do not match')

		self.cr_password.setText('')
		self.cr_password_2.setText('')

	def update_clr(self):
		self.cr_password.setText('')
		self.cr_password_2.setText('')



#################################################################
#################################################################
#################################################################



class MainApp(QMainWindow, ui):
	def __init__(self):
 		QMainWindow.__init__(self)
 		self.setupUi(self)
 		self.Handle_UI_Changes()
 		self.Handle_Buttons()
 		self.show_station()
 		self.show_designation()
 		self.show_vehicle_type()
 		self.station_combo()
 		self.vehicle_type_combo()
 		self.designation_combo()
	
	def Handle_UI_Changes(self):
		self.tabWidget.tabBar().setVisible(False)
		self.style_3()

	def Handle_Buttons(self):
		#----------------------------
		self.pushButton.clicked.connect(self.open_home)
		self.pushButton_2.clicked.connect(self.open_vehicle)
		self.pushButton_3.clicked.connect(self.open_staff)
		self.pushButton_4.clicked.connect(self.open_report)
		self.pushButton_5.clicked.connect(self.open_action)
		self.pushButton_30.clicked.connect(self.open_settings)

		self.pushButton_15.clicked.connect(self.logout)

		self.pushButton_32.clicked.connect(self.add_station)
		self.pushButton_31.clicked.connect(self.station_combo)
		self.pushButton_37.clicked.connect(self.add_designation)
		self.pushButton_36.clicked.connect(self.designation_combo)
		self.pushButton_38.clicked.connect(self.add_vehicle_type)
		self.pushButton_39.clicked.connect(self.vehicle_type_combo)

		self.pushButton_10.clicked.connect(self.add_vehicle)
		self.pushButton_6.clicked.connect(self.search_vehicle)
		self.pushButton_19.clicked.connect(self.update_vehicle)
		self.pushButton_20.clicked.connect(self.delete_vehicle)
		self.pushButton_11.clicked.connect(self.add_vehicle_clr)
		self.pushButton_13.clicked.connect(self.search_vehicle_clr)
		self.pushButton_41.clicked.connect(self.load_vehicle)
		self.pushButton_18.clicked.connect(self.export_vehicle)

		self.pushButton_8.clicked.connect(self.add_staff)
		self.pushButton_9.clicked.connect(self.search_staff)
		self.pushButton_23.clicked.connect(self.update_staff)
		self.pushButton_24.clicked.connect(self.delete_staff)
		self.pushButton_16.clicked.connect(self.add_staff_clr)
		self.pushButton_21.clicked.connect(self.search_staff_clr)
		self.pushButton_42.clicked.connect(self.load_staff)
		self.pushButton_28.clicked.connect(self.export_staff)
		
		self.pushButton_43.clicked.connect(self.load_report)
		self.pushButton_29.clicked.connect(self.export_report)

		self.pushButton_17.clicked.connect(self.add_action)
		self.pushButton_40.clicked.connect(self.search_action)
		self.pushButton_35.clicked.connect(self.update_action)
		self.pushButton_33.clicked.connect(self.delete_action)
		self.pushButton_22.clicked.connect(self.add_action_clr)
		self.pushButton_25.clicked.connect(self.search_action_clr)

	def style_3(self):
		style = open('Themes/style_3.css', 'r')
		style = style.read()
		self.setStyleSheet(style)


	###########################
	########### Tabs ##########
	def open_home(self):
	    self.tabWidget.setCurrentIndex(0)
	def open_vehicle(self):
	    self.tabWidget.setCurrentIndex(1)
	def open_staff(self):
	    self.tabWidget.setCurrentIndex(2)
	def open_report(self):
	    self.tabWidget.setCurrentIndex(3)
	def open_action(self):
	    self.tabWidget.setCurrentIndex(4)
	def open_settings(self):
	    self.tabWidget.setCurrentIndex(5)


	###########################
	########### Home ##########
	def logout(self):
		self.window = LoginPage()
		self.close()
		self.window.show()


	###########################
	######### Vehicles ########
	def add_vehicle(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()

	    vehicle_number = self.lineEdit_5.text()
	    station_id = self.comboBox_9.currentText()
	    vehicle_type = self.comboBox.currentText()
	    model_number = self.lineEdit_6.text()
	    status = self.comboBox_5.currentText()
	    water_cap = self.lineEdit_10.text()
	    purchase = self.lineEdit_7.text()

	    self.cur.execute('''INSERT INTO vehicles (VEHICLE_NUM,VEHICLE_STATION,VEHICLE_TYPE,MODEL_NO,VEHICLE_STATUS,WATER_CAP,PURCHASE)
	        VALUES (%s,%s,%s,%s,%s,%s,%s);
	        ''',(vehicle_number,station_id,vehicle_type,model_number,status,water_cap,purchase))
	    self.db.commit()
	    self.statusBar().showMessage('New Vehicle Added')

	    self.lineEdit_5.setText('')
	    self.comboBox_9.setCurrentIndex(0)
	    self.comboBox.setCurrentIndex(0)
	    self.lineEdit_6.setText('')
	    self.comboBox_5.setCurrentIndex(0)
	    self.lineEdit_10.setText('')
	    self.lineEdit_7.setText('')

	def search_vehicle(self):
		self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
		self.cur = self.db.cursor()
		id = self.lineEdit_12.text()

		sql = ''' SELECT * FROM vehicles WHERE VEHICLE_ID = %s;'''
		self.cur.execute(sql,[(id)])
		data = self.cur.fetchone()

		if data != None:
			self.lineEdit_26.setText(data[1])
			self.comboBox_8.setCurrentText(data[2])
			self.comboBox_3.setCurrentText(data[3])
			self.lineEdit_18.setText(data[4])
			self.comboBox_6.setCurrentText(data[5])
			self.lineEdit_11.setText(data[6])
			self.lineEdit_8.setText(data[7])
		else:
			QMessageBox.critical(self,'Error','Please Enter A Valid Vehicle ID')

	def update_vehicle(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()

	    vehicle_id = self.lineEdit_12.text()
	    vehicle_number = self.lineEdit_26.text()
	    station_id = self.comboBox_8.currentText()
	    vehicle_type = self.comboBox_3.currentText()
	    model_number = self.lineEdit_18.text()
	    status = self.comboBox_6.currentText()
	    water_cap = self.lineEdit_11.text()
	    purchase = self.lineEdit_8.text()

	    self.cur.execute('''UPDATE vehicles SET VEHICLE_NUM = %s,VEHICLE_STATION = %s,VEHICLE_TYPE = %s,MODEL_NO = %s,VEHICLE_STATUS = %s,WATER_CAP = %s,PURCHASE = %s 
			WHERE VEHICLE_ID = %s;
		    ''',(vehicle_number,station_id,vehicle_type,model_number,status,water_cap,purchase,vehicle_id))
	    self.db.commit()
	    self.statusBar().showMessage('Vehicle Data Updated')

	    self.lineEdit_12.setText('')
	    self.lineEdit_26.setText('')
	    self.comboBox_8.setCurrentIndex(0)
	    self.comboBox_3.setCurrentIndex(0)
	    self.lineEdit_18.setText('')
	    self.comboBox_6.setCurrentIndex(0)
	    self.lineEdit_11.setText('')
	    self.lineEdit_8.setText('')

	def delete_vehicle(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()
	    id = self.lineEdit_12.text()

	    warning = QMessageBox.warning(self, 'Delete Vehicle', 'Are you sure you want to delete this vehicle?', QMessageBox.Yes | QMessageBox.No)
	    if warning == QMessageBox.Yes :
	    	sql = ''' DELETE FROM vehicles WHERE VEHICLE_ID = %s;'''
	    	self.cur.execute(sql, [(id)])
	    	self.db.commit()
	    	self.statusBar().showMessage('Vehicle Deleted')

	    	self.lineEdit_12.setText('')
	    	self.lineEdit_26.setText('')
	    	self.comboBox_8.setCurrentIndex(0)
	    	self.comboBox_3.setCurrentIndex(0)
	    	self.lineEdit_18.setText('')
	    	self.comboBox_6.setCurrentIndex(0)
	    	self.lineEdit_11.setText('')
	    	self.lineEdit_8.setText('')

	def add_vehicle_clr(self):
	    self.lineEdit.setText('')
	    self.lineEdit_5.setText('')
	    self.comboBox_9.setCurrentIndex(0)
	    self.comboBox.setCurrentIndex(0)
	    self.lineEdit_6.setText('')
	    self.comboBox_5.setCurrentIndex(0)
	    self.lineEdit_10.setText('')
	    self.lineEdit_7.setText('')

	def search_vehicle_clr(self):
	    self.lineEdit_12.setText('')
	    self.lineEdit_26.setText('')
	    self.comboBox_8.setCurrentIndex(0)
	    self.comboBox_3.setCurrentIndex(0)
	    self.lineEdit_18.setText('')
	    self.comboBox_6.setCurrentIndex(0)
	    self.lineEdit_11.setText('')
	    self.lineEdit_8.setText('')

	def load_vehicle(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()

	    self.cur.execute(''' SELECT * FROM vehicles ''')
	    data = self.cur.fetchall()

	    self.tableWidget.setRowCount(0)

	    for row, form in enumerate(data):
	    	row_pos = self.tableWidget.rowCount()
	    	self.tableWidget.insertRow(row_pos)

	    	for col, item in enumerate(form):
	    		self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))
	    		col += 1

	def export_vehicle(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()

	    self.cur.execute(''' SELECT * FROM vehicles ''')
	    data = self.cur.fetchall()

	    wb = Workbook('Vehicles.xlsx')
	    sheet1 = wb.add_worksheet()

	    sheet1.write(0,0,'Vehicle ID')
	    sheet1.write(0,1,'Vehicle No.')
	    sheet1.write(0,2,'Station ID')
	    sheet1.write(0,3,'Vehicle Type')
	    sheet1.write(0,4,'Model No.')
	    sheet1.write(0,5,'status')
	    sheet1.write(0,6,'Capacity')
	    sheet1.write(0,7,'Purchase Date')

	    row_num = 1
	    for row in data:
	    	col_num = 0
	    	for item in row:
	    		sheet1.write(row_num, col_num, str(item))
	    		col_num += 1
	    	row_num += 1

	    wb.close()
	    self.statusBar().showMessage('Vehicle Data Exported Successfully')


	###########################
	########## Staff ##########
	def add_staff(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()

	    f_name = self.lineEdit_2.text()
	    m_name = self.lineEdit_3.text()
	    l_name = self.lineEdit_4.text()
	    if self.radioButton.isChecked():
	    	gender = 'Male'
	    if self.radioButton_2.isChecked():
	    	gender = 'Female'
	    dob = self.lineEdit_9.text()
	    contact = self.lineEdit_15.text()
	    currad = self.textEdit.toPlainText()
	    desig = self.comboBox_2.currentText()
	    doj = self.lineEdit_33.text()
	    dol = self.lineEdit_35.text()
	    station = self.comboBox_11.currentText()
	    sal = self.lineEdit_14.text()

	    self.cur.execute('''INSERT INTO staff (F_NAME,M_NAME,L_NAME,GENDER,DOB,STAFF_CONTACT,STAFF_ADDR,STAFF_DESIG,DOJ,DOL,STAFF_STATION,SALARY)
	        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
	        ''',(f_name,m_name,l_name,gender,dob,contact,currad,desig,doj,dol,station,sal))
	    self.db.commit()
	    self.statusBar().showMessage('New Staff Added')

	    self.lineEdit_2.setText('')
	    self.lineEdit_3.setText('')
	    self.lineEdit_4.setText('')
	    self.radioButton.setChecked(True)
	    self.lineEdit_9.setText('')
	    self.lineEdit_15.setText('')
	    self.textEdit.setPlainText('')
	    self.comboBox_2.setCurrentIndex(0)
	    self.lineEdit_33.setText('')
	    self.lineEdit_35.setText('')
	    self.comboBox_11.setCurrentIndex(0)
	    self.lineEdit_14.setText('')

	def search_staff(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()
	    id = self.lineEdit_32.text()

	    sql = ''' SELECT * FROM staff WHERE STAFF_ID = %s;'''
	    self.cur.execute(sql,[(id)])
	    data = self.cur.fetchone()
	    print(data)

	    if data != None:
	    	self.lineEdit_36.setText(data[1])
	    	self.lineEdit_19.setText(data[2])
	    	self.lineEdit_34.setText(data[3])
	    	if data[4] == 'Male':
	    		self.radioButton_4.setChecked(True)
	    	if data[4] == 'Female':
	    		self.radioButton_3.setChecked(True)
	    	self.lineEdit_48.setText(data[5])
	    	self.lineEdit_38.setText(str(data[6]))
	    	self.textEdit_2.setPlainText(data[7])
	    	self.comboBox_4.setCurrentText(data[8])
	    	self.lineEdit_49.setText(data[9])
	    	self.lineEdit_52.setText(data[10])
	    	self.comboBox_10.setCurrentText(data[11])
	    	self.lineEdit_37.setText(str(data[12]))
	    else:
	    	QMessageBox.critical(self,'Error','Please Enter A Valid Staff ID')

	def update_staff(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()

	    staff_id = self.lineEdit_32.text()
	    f_name = self.lineEdit_36.text()
	    m_name = self.lineEdit_19.text()
	    l_name = self.lineEdit_34.text()
	    if self.radioButton_4.isChecked():
	    	gender = 'Male'
	    if self.radioButton_3.isChecked():
	    	gender = 'Female'
	    dob = self.lineEdit_48.text()
	    contact = self.lineEdit_38.text()
	    currad = self.textEdit_2.toPlainText()
	    desig = self.comboBox_4.currentText()
	    doj = self.lineEdit_49.text()
	    dol = self.lineEdit_52.text()
	    station = self.comboBox_10.currentText()
	    sal = self.lineEdit_37.text()

	    self.cur.execute('''UPDATE staff SET F_NAME = %s,M_NAME = %s,L_NAME = %s,GENDER = %s,DOB = %s,STAFF_CONTACT = %s,STAFF_ADDR = %s,STAFF_DESIG = %s,DOJ = %s,DOL = %s,STAFF_STATION = %s,SALARY = %s 
			WHERE STAFF_ID = %s;
		    ''',(f_name,m_name,l_name,gender,dob,contact,currad,desig,doj,dol,station,sal,staff_id))
	    self.db.commit()
	    self.statusBar().showMessage('Staff Data Updated')

	    self.lineEdit_36.setText('')
	    self.lineEdit_19.setText('')
	    self.lineEdit_34.setText('')
	    self.radioButton_4.setChecked(True)
	    self.lineEdit_48.setText('')
	    self.lineEdit_38.setText('')
	    self.textEdit_2.setPlainText('')
	    self.comboBox_4.setCurrentIndex(0)
	    self.lineEdit_49.setText('')
	    self.lineEdit_52.setText('')
	    self.comboBox_10.setCurrentIndex(0)
	    self.lineEdit_37.setText('')

	def delete_staff(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()
	    id = self.lineEdit_37.text()

	    warning = QMessageBox.warning(self, 'Delete Staff', 'Are you sure you want to delete this staff?', QMessageBox.Yes | QMessageBox.No)
	    if warning == QMessageBox.Yes :
	    	sql = ''' DELETE FROM staff WHERE STAFF_ID = %s;'''
	    	self.cur.execute(sql, [(id)])
	    	self.db.commit()
	    	self.statusBar().showMessage('Staff Deleted')

	    	self.lineEdit_36.setText('')
	    	self.lineEdit_19.setText('')
	    	self.lineEdit_34.setText('')
	    	self.radioButton_4.setChecked(True)
	    	self.lineEdit_48.setText('')
	    	self.lineEdit_38.setText('')
	    	self.textEdit_2.setPlainText('')
	    	self.comboBox_4.setCurrentIndex(0)
	    	self.lineEdit_49.setText('')
	    	self.lineEdit_52.setText('')
	    	self.comboBox_10.setCurrentIndex(0)
	    	self.lineEdit_37.setText('')

	def add_staff_clr(self):
	    self.lineEdit_13.setText('')
	    self.lineEdit_2.setText('')
	    self.lineEdit_3.setText('')
	    self.lineEdit_4.setText('')
	    self.radioButton.setChecked(True)
	    self.lineEdit_9.setText('')
	    self.lineEdit_15.setText('')
	    self.textEdit.setPlainText('')
	    self.comboBox_2.setCurrentIndex(0)
	    self.lineEdit_33.setText('')
	    self.lineEdit_35.setText('')
	    self.comboBox_11.setCurrentIndex(0)
	    self.lineEdit_14.setText('')
	
	def search_staff_clr(self):
	    self.lineEdit_36.setText('')
	    self.lineEdit_19.setText('')
	    self.lineEdit_34.setText('')
	    self.radioButton_4.setChecked(True)
	    self.lineEdit_48.setText('')
	    self.lineEdit_38.setText('')
	    self.textEdit_2.setPlainText('')
	    self.comboBox_4.setCurrentIndex(0)
	    self.lineEdit_49.setText('')
	    self.lineEdit_52.setText('')
	    self.comboBox_10.setCurrentIndex(0)
	    self.lineEdit_37.setText('')
	
	def load_staff(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()

	    self.cur.execute(''' SELECT * FROM staff ''')
	    data = self.cur.fetchall()

	    self.tableWidget_2.setRowCount(0)

	    for row, form in enumerate(data):
	    	row_pos = self.tableWidget_2.rowCount()
	    	self.tableWidget_2.insertRow(row_pos)

	    	for col, item in enumerate(form):
	    		self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(item)))
	    		col += 1

	def export_staff(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()

	    self.cur.execute(''' SELECT * FROM staff ''')
	    data = self.cur.fetchall()

	    wb = Workbook('Staff.xlsx')
	    sheet1 = wb.add_worksheet()

	    sheet1.write(0,0,'Staff ID')
	    sheet1.write(0,1,'First Name')
	    sheet1.write(0,2,'Middle Name')
	    sheet1.write(0,3,'Last Name')
	    sheet1.write(0,4,'Gender')
	    sheet1.write(0,5,'Date of Birth')
	    sheet1.write(0,6,'Contact No.')
	    sheet1.write(0,7,'Designation')
	    sheet1.write(0,8,'Date of Joining')
	    sheet1.write(0,9,'Date of Leaving')
	    sheet1.write(0,10,'Station ID')
	    sheet1.write(0,11,'Salary')

	    row_num = 1
	    for row in data:
	    	col_num = 0
	    	for item in row:
	    		sheet1.write(row_num, col_num, str(item))
	    		col_num += 1
	    	row_num += 1

	    wb.close()
	    self.statusBar().showMessage('Staff Data Exported Successfully')


	###########################
	######### Reports #########
	def load_report(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()

	    self.cur.execute(''' SELECT * FROM reports ''')
	    data = self.cur.fetchall()

	    self.tableWidget_3.setRowCount(0)

	    for row, form in enumerate(data):
	    	row_pos = self.tableWidget_3.rowCount()
	    	self.tableWidget_3.insertRow(row_pos)

	    	for col, item in enumerate(form):
	    		self.tableWidget_3.setItem(row, col, QTableWidgetItem(str(item)))
	    		col += 1
	
	def export_report(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()

	    self.cur.execute(''' SELECT * FROM reports ''')
	    data = self.cur.fetchall()

	    wb = Workbook('Reports.xlsx')
	    sheet1 = wb.add_worksheet()

	    sheet1.write(0,0,'Report ID')
	    sheet1.write(0,1,'Street Address')
	    sheet1.write(0,2,'City')
	    sheet1.write(0,3,'State')
	    sheet1.write(0,4,'Pincode')
	    sheet1.write(0,5,'Description')
	    sheet1.write(0,6,'Informant Name')
	    sheet1.write(0,7,'Informant Contact')
	    sheet1.write(0,8,'Date and Time')

	    row_num = 1
	    for row in data:
	    	col_num = 0
	    	for item in row:
	    		sheet1.write(row_num, col_num, str(item))
	    		col_num += 1
	    	row_num += 1

	    wb.close()
	    self.statusBar().showMessage('Reports Exported Successfully')


	###########################
	######### Actions #########
	def add_action(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()

	    ac_id = self.lineEdit_17.text()
	    head_id = self.lineEdit_46.text()
	    reach = self.lineEdit_57.text()
	    leave = self.lineEdit_58.text()
	    veh_id = self.lineEdit_47.text()
	    status = self.comboBox_7.currentText()
	    descrip = self.textEdit_3.toPlainText()

	    self.cur.execute('''INSERT INTO action (FOR_REPORT_ID,HEAD_ID,TIME_REACH,TIME_LEAVE,ACTION_VEHICLE_IDS,STATUS,DESCRIPTION)
	        VALUES (%s,%s,%s,%s,%s,%s,%s);
	        ''',(ac_id,head_id,reach,leave,veh_id,status,descrip))
	    self.db.commit()
	    self.statusBar().showMessage('New Action Added')

	    self.lineEdit_17.setText('')
	    self.lineEdit_46.setText('')
	    self.lineEdit_57.setText('')
	    self.lineEdit_58.setText('')
	    self.lineEdit_47.setText('')
	    self.comboBox_7.setCurrentIndex(0)
	    self.textEdit_3.setPlainText('')

	def search_action(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()
	    id = self.lineEdit_28.text()

	    sql = ''' SELECT * FROM action WHERE FOR_REPORT_ID = %s;'''
	    self.cur.execute(sql,[(id)])
	    data = self.cur.fetchone()
	    print(data)

	    if data != None:
	    	self.lineEdit_50.setText(str(data[1]))
	    	self.lineEdit_59.setText(data[2])
	    	self.lineEdit_60.setText(data[3])
	    	self.lineEdit_51.setText(data[4])
	    	self.comboBox_13.setCurrentText(data[5])
	    	self.textEdit_4.setPlainText(data[6])
	    else:
	    	QMessageBox.critical(self,'Error','No Action exists for that Report ID')

	def update_action(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()

	    ac_id = self.lineEdit_28.text()
	    head_id = self.lineEdit_50.text()
	    reach = self.lineEdit_59.text()
	    leave = self.lineEdit_60.text()
	    veh_id = self.lineEdit_51.text()
	    status = self.comboBox_13.currentText()
	    descrip = self.textEdit_4.toPlainText()

	    self.cur.execute('''UPDATE action SET HEAD_ID = %s,TIME_REACH = %s,TIME_LEAVE = %s,ACTION_VEHICLE_IDS = %s,STATUS = %s,DESCRIPTION = %s
	    	WHERE FOR_REPORT_ID = %s;
	        ''',(head_id,reach,leave,veh_id,status,descrip,ac_id))
	    self.db.commit()
	    self.statusBar().showMessage('Action Updated')

	    self.lineEdit_28.setText('')
	    self.lineEdit_50.setText('')
	    self.lineEdit_59.setText('')
	    self.lineEdit_60.setText('')
	    self.lineEdit_51.setText('')
	    self.comboBox_13.setCurrentIndex(0)
	    self.textEdit_4.setPlainText('')

	def delete_action(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()
	    id = self.lineEdit_28.text()

	    warning = QMessageBox.warning(self, 'Delete Action', 'Are you sure you want to delete this action?', QMessageBox.Yes | QMessageBox.No)
	    if warning == QMessageBox.Yes :
	    	sql = ''' DELETE FROM action WHERE FOR_REPORT_ID = %s;'''
	    	self.cur.execute(sql, [(id)])
	    	self.db.commit()
	    	self.statusBar().showMessage('Action Deleted')

	    	self.lineEdit_28.setText('')
	    	self.lineEdit_50.setText('')
	    	self.lineEdit_59.setText('')
	    	self.lineEdit_60.setText('')
	    	self.lineEdit_51.setText('')
	    	self.comboBox_13.setCurrentIndex(0)
	    	self.textEdit_4.setPlainText('')

	def add_action_clr(self):
	    self.lineEdit_17.setText('')
	    self.lineEdit_46.setText('')
	    self.lineEdit_57.setText('')
	    self.lineEdit_58.setText('')
	    self.lineEdit_47.setText('')
	    self.comboBox_7.setCurrentIndex(0)
	    self.textEdit_3.setPlainText('')

	def search_action_clr(self):
	    self.lineEdit_28.setText('')
	    self.lineEdit_50.setText('')
	    self.lineEdit_59.setText('')
	    self.lineEdit_60.setText('')
	    self.lineEdit_51.setText('')
	    self.comboBox_13.setCurrentIndex(0)
	    self.textEdit_4.setPlainText('')


	###########################
	######### Settings ########
	def add_station(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()

	    station_id = self.lineEdit_27.text()
	    station_num = self.lineEdit_29.text()
	    station_addr = self.plainTextEdit_5.toPlainText()

	    self.cur.execute('''
	        INSERT INTO stations (STATION_ID,STATION_CONTACT,STATION_ADDR) VALUES (%s,%s,%s)
	    ''', (station_id,station_num,station_addr) )

	    self.db.commit()
	    self.lineEdit_27.setText('')
	    self.lineEdit_29.setText('')
	    self.plainTextEdit_5.setPlainText('')
	    self.show_station()
	    self.statusBar().showMessage('New Station Added')

	def show_station(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()

	    self.cur.execute('''
	        SELECT * FROM stations''')
	    data = self.cur.fetchall()

	    if data:
	        self.tableWidget_4.setRowCount(0)
	        for row, form in enumerate(data):
	        	row_pos = self.tableWidget_4.rowCount()
	        	self.tableWidget_4.insertRow(row_pos)
	        	for col, item in enumerate(form):
	        		self.tableWidget_4.setItem(row,col,QTableWidgetItem(str(item)))
	        		col +=1

	def add_designation(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()

	    desig = self.lineEdit_30.text()

	    self.cur.execute('''
	        INSERT INTO designation (DESIG_NAME) VALUES (%s)
	    ''', (desig,) )

	    self.db.commit()
	    self.lineEdit_30.setText('')
	    self.show_designation()
	    self.statusBar().showMessage('New Designation Added')
	
	def show_designation(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()

	    self.cur.execute('''
	        SELECT DESIG_NAME FROM designation''')
	    data = self.cur.fetchall()

	    if data:
	        self.tableWidget_5.setRowCount(0)

	        for row, form in enumerate(data):
	        	row_pos = self.tableWidget_5.rowCount()
	        	self.tableWidget_5.insertRow(row_pos)
	        	for col, item in enumerate(form):
	        		self.tableWidget_5.setItem(row,col,QTableWidgetItem(str(item)))
	        		col +=1

	def add_vehicle_type(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()

	    veh_type = self.lineEdit_31.text()

	    self.cur.execute('''
	        INSERT INTO vehicle_type (TYPE_NAME) VALUES (%s)
	    ''', (veh_type,) )

	    self.db.commit()
	    self.lineEdit_31.setText('')
	    self.show_vehicle_type()
	    self.statusBar().showMessage('New Vehicle Type Added')
	
	def show_vehicle_type(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()

	    self.cur.execute('''
	        SELECT TYPE_NAME FROM vehicle_type''')
	    data = self.cur.fetchall()

	    if data:
	        self.tableWidget_6.setRowCount(0)
	        for row, form in enumerate(data):
	        	row_pos = self.tableWidget_6.rowCount()
	        	self.tableWidget_6.insertRow(row_pos)
	        	for col, item in enumerate(form):
	        		self.tableWidget_6.setItem(row,col,QTableWidgetItem(str(item)))
	        		col +=1


	###########################
	## Settings to ComboBox ###
	def station_combo(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()

	    self.cur.execute(''' SELECT STATION_ID FROM stations ''')
	    data = self.cur.fetchall()

	    self.comboBox_9.clear()
	    self.comboBox_8.clear()
	    self.comboBox_11.clear()
	    self.comboBox_10.clear()
	    
	    for station in data:
	        self.comboBox_9.addItem(str(station[0]))
	        self.comboBox_8.addItem(str(station[0]))
	        self.comboBox_11.addItem(str(station[0]))
	        self.comboBox_10.addItem(str(station[0]))

	def designation_combo(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()

	    self.cur.execute(''' SELECT DESIG_NAME FROM designation ''')
	    data = self.cur.fetchall()

	    self.comboBox_2.clear()
	    self.comboBox_4.clear()
	    
	    for desig in data:
	        self.comboBox_2.addItem(str(desig[0]))
	        self.comboBox_4.addItem(str(desig[0]))

	def vehicle_type_combo(self):
	    self.db = pymysql.connect(host='localhost', user= 'root', password= 'admin', db='firestation')
	    self.cur = self.db.cursor()

	    self.cur.execute(''' SELECT TYPE_NAME FROM vehicle_type ''')
	    data = self.cur.fetchall()

	    self.comboBox.clear()
	    self.comboBox_3.clear()

	    for vehi in data:
	        self.comboBox.addItem(str(vehi[0]))
	        self.comboBox_3.addItem(str(vehi[0]))


def main():
 	app = QApplication(sys.argv)
 	window = LoginPage()
 	window.show()
 	app.exec_()

if __name__ == '__main__':
 	main() 	
