from pkg_resources import resource_filename
from PyQt4 import Qt, QtCore
from toutvqt.downloads_itemdelegate import QDlItemDelegate


class QDownloadsTableView(Qt.QTreeView):
    cancel_download = QtCore.pyqtSignal(int)

    def __init__(self, model):
        super().__init__()

        self.setRootIsDecorated(False)
        self.setItemDelegate(QDlItemDelegate(model))
        self._setup(model)

    def _build_context_menu(self):
        self._context_menu = Qt.QMenu(parent=self)
        self._cancel_action = self._context_menu.addAction('&Cancel')

    def _setup_context_menu(self):
        self._build_context_menu()
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self._on_context_menu)

    def _setup(self, model):
        self.setModel(model)
        self._setup_context_menu()

    def _on_context_menu(self, pos):
        index = self.indexAt(pos)
        if not index.isValid():
            return

        action = self._context_menu.exec(Qt.QCursor.pos())

        if action is self._cancel_action:
            self.cancel_download.emit(index.row())

    def set_default_columns_widths(self):
        pass
