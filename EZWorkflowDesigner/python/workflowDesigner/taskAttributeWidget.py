from PyQt5 import QtCore, QtGui, QtWidgets, Qt, uic

from tasks.task import Task, TaskAttribute
import inspect

class TaskAttributeWidget(QtWidgets.QWidget):

	def __init__(self, name, taskAttribute, *args, **kwargs):
		super().__init__(*args, **kwargs)
		uic.loadUi('python/workflowDesigner/UI/taskAttributeWidget.ui', self)
		self.name = name
		self.taskAttribute = taskAttribute
		#self.setStyleSheet("background-color: yellow")
		self.setupUI()

	def setupUI(self):
		
		self.attributeNameLbl.setText(self.name)
		if self.taskAttribute.attributeType == str:
			pass
		elif self.taskAttribute.attributeType == list:
			extraLineEdit = QtWidgets.QLineEdit(self)
			self.gridLayout.addWidget(extraLineEdit, 1, 1)