import os
from PyQt5 import QtGui, QtWidgets
import sys

from primary import FirstWindow
from secondary import SecondWindow
from third import ThirdWindow

from people_data import Person


def submit_form():
    person = Person()

    if ui_two.male_radio.isChecked():
        person.gender = "male"
        person.chart_path = "male_bmi_chart.png"
    elif ui_two.female_radio.isChecked():
        person.gender = "female"
        person.chart_path = "female_bmi_chart.jpg"
    else:
        person.gender = "none"

    person.age = ui_two.age_input.value()
    person.weight = ui_two.weight_input.value()
    person.height = ui_two.height_input.value() / 100
    person.workout_hours = ui_two.workout_hours_input.value()
    person.recent_meals = ui_two.meal_input.toPlainText().split("\n")

    ui_three.bmi_label.setText(str(person.calculate_bmi()))
    ui_three.bmi_note.setText(str(person.health_indicator()))

    ui_three.label_3.setPixmap(QtGui.QPixmap(
        os.path.join(os.path.dirname(__file__), person.chart_path)))

    ui_three.chart_label.setPixmap(QtGui.QPixmap(
        os.path.join(os.path.dirname(__file__), "my_barchart.png")))

    from people_data import Meal
    meal = Meal(person)
    meal.display_data()

    # Dialog2.hide()
    Dialog3.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    Dialog2 = QtWidgets.QDialog()
    Dialog3 = QtWidgets.QDialog()

    ui_one = FirstWindow()
    ui_two = SecondWindow()
    ui_three = ThirdWindow()

    ui_one.setupUi(Dialog)
    ui_two.setupUi(Dialog2)
    ui_three.setupUi(Dialog3)

    Dialog.show()
    ui_one.start_test_button.clicked.connect(
        lambda: ui_one.handle_click(Dialog, Dialog2))
    ui_two.submit_form_button.clicked.connect(submit_form)
    ui_three.exit_button.clicked.connect(app.exit)

    sys.exit(app.exec_())
