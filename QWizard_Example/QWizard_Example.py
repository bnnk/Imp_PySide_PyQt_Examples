import sys
import Qt
from Qt import QtWidgets, QtGui

print ('Qt Version: ' + Qt.__qt_version__)
print ('Binding Version: ' + Qt.__binding_version__)
print ('Is this PySide2? ', Qt.IsPySide2)
print ('Is this PyQt5? ', Qt.IsPyQt5)
print ('Is this PySide? ', Qt.IsPySide)
print ('Is this PyQt4? ', Qt.IsPyQt4)

# CREATE WIZARD, WATERMARK, LOGO, BANNER
app = QtWidgets.QApplication(sys.argv)
wizard = QtWidgets.QWizard()
wizard.setWizardStyle(QtWidgets.QWizard.ModernStyle)

try: # PYSIDE
    wizard.setPixmap(QtWidgets.QWizard.WatermarkPixmap,
                    'Watermark.png')
    wizard.setPixmap(QtWidgets.QWizard.LogoPixmap,
                    'Logo.png')
    wizard.setPixmap(QtWidgets.QWizard.BannerPixmap,
                    'Banner.png')
except TypeError: # PYQT5
    wizard.setPixmap(QtWidgets.QWizard.WatermarkPixmap,
            QtGui.QPixmap('Watermark.png'))
    wizard.setPixmap(QtWidgets.QWizard.LogoPixmap,
            QtGui.QPixmap('Logo.png'))
    wizard.setPixmap(QtWidgets.QWizard.BannerPixmap,
            QtGui.QPixmap('Banner.png'))


# CREATE PAGE 1, LINE EDIT, TITLES
page1 = QtWidgets.QWizardPage()
page1.setTitle('Page 1 is best!')
page1.setSubTitle('1111111111')
lineEdit = QtWidgets.QLineEdit()
hLayout1 = QtWidgets.QHBoxLayout(page1)
hLayout1.addWidget(lineEdit)

try: # PYSIDE
    page1.registerField('myField*', 
        lineEdit,
        lineEdit.text(),
        'textChanged')
except TypeError: # PYQT
    page1.registerField('myField*', 
        lineEdit,
        lineEdit.text(),
        lineEdit.textChanged)


# CREATE PAGE 2, LABEL, TITLES
page2 = QtWidgets.QWizardPage()
page2.setFinalPage(True)
page2.setTitle('Page 2 is better!')
page2.setSubTitle('Lies!')
label = QtWidgets.QLabel()
hLayout2 = QtWidgets.QHBoxLayout(page2)
hLayout2.addWidget(label)

# CONNECT SIGNALS AND PAGES
# lineEdit.textChanged.connect(lambda:label.setText(lineEdit.text()))
nxt = wizard.button(QtWidgets.QWizard.NextButton)
func = lambda:label.setText(page1.field('myField'))
nxt.clicked.connect(func)
wizard.addPage(page1)
wizard.addPage(page2)

# WHAT'S THIS SETUP
wizard.setWhatsThis('You DumbleDork!')
page1.setWhatsThis('This is page 1 of course!')
page2.setWhatsThis('22222!')
lineEdit.setWhatsThis('You Shall Not Pass!')

wizard.show()
sys.exit(app.exec_())