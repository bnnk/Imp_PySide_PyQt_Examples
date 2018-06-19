import sys
from Qt import QtWidgets

# CREATE WIZARD, WATERMARK, LOGO, BANNER
app = QtWidgets.QApplication(sys.argv)
wizard = QtWidgets.QWizard()
wizard.setWizardStyle(QtWidgets.QWizard.ModernStyle)
wizard.setPixmap(QtWidgets.QWizard.WatermarkPixmap,
                'Watermark.png')
wizard.setPixmap(QtWidgets.QWizard.LogoPixmap,
                'Logo.png')
wizard.setPixmap(QtWidgets.QWizard.BannerPixmap,
                'Banner.png')

# CREATE PAGE 1, LINE EDIT, TITLES
page1 = QtWidgets.QWizardPage()
page1.setTitle('Page 1 is best!')
page1.setSubTitle('1111111111')
lineEdit = QtWidgets.QLineEdit()
hLayout1 = QtWidgets.QHBoxLayout(page1)
hLayout1.addWidget(lineEdit)
page1.registerField('myField*', 
    lineEdit,
    lineEdit.text(),
    'textChanged')

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