# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_metadata.ui'
#
# Created: Wed Jul 30 12:13:52 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MetatoolsEditor(object):
    def setupUi(self, MetatoolsEditor):
        MetatoolsEditor.setObjectName(_fromUtf8("MetatoolsEditor"))
        MetatoolsEditor.resize(808, 559)
        self.centralwidget = QtGui.QWidget(MetatoolsEditor)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(self.tab)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.filterBox = QtGui.QLineEdit(self.widget)
        self.filterBox.setObjectName(_fromUtf8("filterBox"))
        self.horizontalLayout.addWidget(self.filterBox)
        self.buttonExpand = QtGui.QToolButton(self.widget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonExpand.setIcon(icon)
        self.buttonExpand.setAutoRaise(True)
        self.buttonExpand.setObjectName(_fromUtf8("buttonExpand"))
        self.horizontalLayout.addWidget(self.buttonExpand)
        self.buttonCollapse = QtGui.QToolButton(self.widget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/minus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonCollapse.setIcon(icon1)
        self.buttonCollapse.setAutoRaise(True)
        self.buttonCollapse.setObjectName(_fromUtf8("buttonCollapse"))
        self.horizontalLayout.addWidget(self.buttonCollapse)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.treeFull = QtGui.QTreeWidget(self.widget)
        self.treeFull.setHeaderHidden(True)
        self.treeFull.setObjectName(_fromUtf8("treeFull"))
        self.treeFull.headerItem().setText(0, _fromUtf8("1"))
        self.verticalLayout_2.addWidget(self.treeFull)
        self.groupBox = QtGui.QGroupBox(self.splitter)
        self.groupBox.setEnabled(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.lblNodePath = QtGui.QLabel(self.groupBox)
        self.lblNodePath.setWordWrap(True)
        self.lblNodePath.setObjectName(_fromUtf8("lblNodePath"))
        self.verticalLayout_4.addWidget(self.lblNodePath)
        self.widgetValue = QtGui.QWidget(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetValue.sizePolicy().hasHeightForWidth())
        self.widgetValue.setSizePolicy(sizePolicy)
        self.widgetValue.setObjectName(_fromUtf8("widgetValue"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widgetValue)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.textValue = QtGui.QPlainTextEdit(self.widgetValue)
        self.textValue.setObjectName(_fromUtf8("textValue"))
        self.verticalLayout_3.addWidget(self.textValue)
        self.numberValue = QtGui.QLineEdit(self.widgetValue)
        self.numberValue.setObjectName(_fromUtf8("numberValue"))
        self.verticalLayout_3.addWidget(self.numberValue)
        self.dateValue = QtGui.QCalendarWidget(self.widgetValue)
        self.dateValue.setObjectName(_fromUtf8("dateValue"))
        self.verticalLayout_3.addWidget(self.dateValue)
        self.comboValue = QtGui.QComboBox(self.widgetValue)
        self.comboValue.setObjectName(_fromUtf8("comboValue"))
        self.verticalLayout_3.addWidget(self.comboValue)
        self.verticalLayout_4.addWidget(self.widgetValue)
        self.verticalLayout.addWidget(self.splitter)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.webView = QtWebKit.QWebView(self.tab_2)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout_5.addWidget(self.webView)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.tabWidget)
        MetatoolsEditor.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MetatoolsEditor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuNew = QtGui.QMenu(self.menuFile)
        self.menuNew.setObjectName(_fromUtf8("menuNew"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        MetatoolsEditor.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MetatoolsEditor)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MetatoolsEditor.setStatusBar(self.statusbar)
        self.actionFGDC = QtGui.QAction(MetatoolsEditor)
        self.actionFGDC.setObjectName(_fromUtf8("actionFGDC"))
        self.actionISO = QtGui.QAction(MetatoolsEditor)
        self.actionISO.setObjectName(_fromUtf8("actionISO"))
        self.actionSave = QtGui.QAction(MetatoolsEditor)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionClose = QtGui.QAction(MetatoolsEditor)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionFillFromLayer = QtGui.QAction(MetatoolsEditor)
        self.actionFillFromLayer.setObjectName(_fromUtf8("actionFillFromLayer"))
        self.actionHighlightEmpty = QtGui.QAction(MetatoolsEditor)
        self.actionHighlightEmpty.setCheckable(True)
        self.actionHighlightEmpty.setChecked(True)
        self.actionHighlightEmpty.setObjectName(_fromUtf8("actionHighlightEmpty"))
        self.actionShowOptional = QtGui.QAction(MetatoolsEditor)
        self.actionShowOptional.setCheckable(True)
        self.actionShowOptional.setChecked(True)
        self.actionShowOptional.setObjectName(_fromUtf8("actionShowOptional"))
        self.actionShowConditional = QtGui.QAction(MetatoolsEditor)
        self.actionShowConditional.setCheckable(True)
        self.actionShowConditional.setChecked(True)
        self.actionShowConditional.setObjectName(_fromUtf8("actionShowConditional"))
        self.actionCopyPath = QtGui.QAction(MetatoolsEditor)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/metatools/icons/menu_copy.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopyPath.setIcon(icon2)
        self.actionCopyPath.setObjectName(_fromUtf8("actionCopyPath"))
        self.actionImport = QtGui.QAction(MetatoolsEditor)
        self.actionImport.setObjectName(_fromUtf8("actionImport"))
        self.menuNew.addAction(self.actionFGDC)
        self.menuNew.addAction(self.actionISO)
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuTools.addAction(self.actionFillFromLayer)
        self.menuView.addAction(self.actionHighlightEmpty)
        self.menuView.addAction(self.actionShowOptional)
        self.menuView.addAction(self.actionShowConditional)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MetatoolsEditor)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MetatoolsEditor)

    def retranslateUi(self, MetatoolsEditor):
        MetatoolsEditor.setWindowTitle(_translate("MetatoolsEditor", "Metadata editor", None))
        self.filterBox.setPlaceholderText(_translate("MetatoolsEditor", "[Enter text to filter element list]", None))
        self.buttonExpand.setText(_translate("MetatoolsEditor", "...", None))
        self.buttonCollapse.setText(_translate("MetatoolsEditor", "...", None))
        self.groupBox.setTitle(_translate("MetatoolsEditor", "Edit value", None))
        self.lblNodePath.setText(_translate("MetatoolsEditor", "TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MetatoolsEditor", "Edit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MetatoolsEditor", "HTML View", None))
        self.menuFile.setTitle(_translate("MetatoolsEditor", "File", None))
        self.menuNew.setTitle(_translate("MetatoolsEditor", "New", None))
        self.menuTools.setTitle(_translate("MetatoolsEditor", "Tools", None))
        self.menuView.setTitle(_translate("MetatoolsEditor", "View", None))
        self.actionFGDC.setText(_translate("MetatoolsEditor", "FGDC", None))
        self.actionISO.setText(_translate("MetatoolsEditor", "ISO -19115", None))
        self.actionSave.setText(_translate("MetatoolsEditor", "Save", None))
        self.actionClose.setText(_translate("MetatoolsEditor", "Close", None))
        self.actionFillFromLayer.setText(_translate("MetatoolsEditor", "Fill metadata from layer", None))
        self.actionHighlightEmpty.setText(_translate("MetatoolsEditor", "Highlight empty fields", None))
        self.actionShowOptional.setText(_translate("MetatoolsEditor", "Show optional fields", None))
        self.actionShowConditional.setText(_translate("MetatoolsEditor", "Show conditional fields", None))
        self.actionCopyPath.setText(_translate("MetatoolsEditor", "Copy path", None))
        self.actionCopyPath.setToolTip(_translate("MetatoolsEditor", "Copy node path to clipboard", None))
        self.actionImport.setText(_translate("MetatoolsEditor", "Import...", None))

from PyQt4 import QtWebKit
import resources_rc
