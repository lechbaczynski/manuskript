#!/usr/bin/env python
# --!-- coding: utf8 --!--
import random

from PyQt5.QtCore import QUrl
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtWidgets import qApp

from manuskript.exporter.pandoc.abstractOutput import abstractOutput
from manuskript.functions import tempFile
from manuskript.ui.views.PDFViewer import PDFViewer


class PDF(abstractOutput):
    """PDF Viewer using PDS.js. Cf. https://github.com/mozilla/pdf.js/wiki/Setup-PDF.js-in-a-website"""

    name = "PDF"
    description = qApp.translate("Export", "Needs latex to be installed.")
    icon = "application-pdf"

    exportVarName = "lastPandocPDF"
    toFormat = "pdf"
    exportFilter = "PDF files (*.pdf);; Any files (*)"
    requires = {
        "Settings": True,
        "Preview": True,
    }

    def output(self, settingsWidget, outputfile=None):
        args = settingsWidget.runnableSettings()
        args.remove("--to=pdf")
        args.append("--to=latex")
        src = self.src(settingsWidget)
        return self.exporter.convert(src, args, outputfile)

    def previewWidget(self):
        return PDFViewer()

    def preview(self, settingsWidget, previewWidget):
        filename = tempFile("msk_pdfpreview.pdf")

        settingsWidget.writeSettings()
        content = self.output(settingsWidget, outputfile=filename)

        previewWidget.loadPDF(filename)