class GroupWidget(QWidget):
    InstallationRequestUpdate = Signal(PackageInfo)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__title_point_size = QFont().pointSize() * 2  # TODO: Move this to a style class

    def add_package(self, package_name: str, related_packages: List[PackageInfo]):
        package_layout = QVBoxLayout()
        package_layout.addWidget(self.__create_header(package_name))
        for package in related_packages:
            package_layout.addWidget(self.__create_package_checkbox(package))

    def __create_package_checkbox(self, package_info: PackageInfo) -> QCheckBox:
        checkbox = QCheckBox(generate_package_info_text(package_info))
        checkbox.clicked.connect(lambda: self.__on_package_checkbox_clicked(package_info))
        return checkbox

    def __create_header(self, text: str) -> QLabel:
        header = QLabel(text)
        header.setStyleSheet(f"font-size: {self.__title_point_size}; font-weight: bold;")
        return header

    def __on_package_checkbox_clicked(self, package_checkbox_name: PackageInfo) -> None:
        self.InstallationRequestUpdate.emit(package_checkbox_name)
