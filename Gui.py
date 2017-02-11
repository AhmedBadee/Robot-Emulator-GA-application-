from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


Gui_app = QApplication(sys.argv)    # create application
main_gui = QWidget()                 # main window


main_gui.setWindowIcon(QIcon('img/robotic2.jpg'))    # set icon

main_gui.setWindowTitle("Robot Emulator")            # set title

# The background set
bc = QPalette()
main_gui.setPalette(bc)


# set window size
main_gui.resize(1200, 700)   # set size
main_gui.move(500, 200)      # set position

# set choose label
choose_label = QLabel(main_gui)                             # Create label
choose_label.setText("<h1> Choose The Environment </h1> ")
choose_label.move(750, 20)                                  # Set its position

# radio boxes
water_radio = QRadioButton(main_gui, text="Water")
water_radio.move(750, 90)

sand_radio = QRadioButton(main_gui, text="Sand")
sand_radio.move(1000, 90)

dark_radio = QRadioButton(main_gui, text="Dark")
dark_radio.move(750, 140)

mountain_radio = QRadioButton(main_gui, text="Mountain")
mountain_radio.move(1000, 140)

light_radio = QRadioButton(main_gui, text="Light")
light_radio.move(750, 190)

obstacles_radio = QRadioButton(main_gui, text="Obstacles")
obstacles_radio.move(1000, 190)

rocks_radio = QRadioButton(main_gui, text="Rocks")
rocks_radio.move(750, 240)

rubble_radio = QRadioButton(main_gui, text="Rubble")
rubble_radio.move(1000, 240)

wind_radio = QRadioButton(main_gui, text="Wind")
wind_radio.move(750, 290)

waterfalls_radio = QRadioButton(main_gui, text="Waterfalls")
waterfalls_radio.move(1000, 290)

rain_radio = QRadioButton(main_gui, text="Rain")
rain_radio.move(750, 340)

collapses_radio = QRadioButton(main_gui, text="Collapses")
collapses_radio.move(1000, 340)

glass_radio = QRadioButton(main_gui, text="Glass")
glass_radio.move(750, 390)

temperature_radio = QRadioButton(main_gui, text="Temperature")
temperature_radio.move(1000, 390)

fire_radio = QRadioButton(main_gui, text="Fire")
fire_radio.move(750, 440)

forest_radio = QRadioButton(main_gui, text="Forest")
forest_radio.move(1000, 440)

# set result label
result_label = QLabel(main_gui)
result_label.setText("<h1><b> The robot Characteristics  <b></h1> ")
result_label.move(10, 20)


height_label = QLabel(main_gui)
height_label.setText("<h3>  Height <h3> ")
height_label.move(20, 100)

height_result = QLineEdit(main_gui)
height_result.move(200, 90)
height_result.resize(120, 40)

width_label = QLabel(main_gui)
width_label.setText("<h3> Width <h3> ")
width_label.move(20, 170)

width_result = QLineEdit(main_gui)
width_result.move(200, 160)
width_result.resize(120, 40)

speed_label = QLabel(main_gui)
speed_label.setText("<h3> Speed <h3> ")
speed_label.move(20, 240)

speed_result = QLineEdit(main_gui)
speed_result.move(200, 230)
speed_result.resize(120, 40)

weight_label = QLabel(main_gui)
weight_label.setText("<h3>  Weight <h3> ")
weight_label.move(20, 310)

weight_result = QLineEdit(main_gui)
weight_result.move(200, 300)
weight_result.resize(120, 40)

material_label = QLabel(main_gui)
material_label.setText("<h3>  Material <h3> ")
material_label.move(20, 380)

material_result = QLineEdit(main_gui)
material_result.move(200, 370)
material_result.resize(120, 40)

wheelnum_label = QLabel(main_gui)
wheelnum_label.setText("<h3>  No of wheels  <h3> ")
wheelnum_label.move(20, 450)

wheelnum_result = QLineEdit(main_gui)
wheelnum_result.move(200, 440)
wheelnum_result.resize(120, 40)

legnum_label = QLabel(main_gui)
legnum_label.setText("<h3>  No of legs <h3> ")
legnum_label.move(20, 520)

legnum_result = QLineEdit(main_gui)
legnum_result.move(200, 510)
legnum_result.resize(120, 40)

cost_label = QLabel(main_gui, text=" <h3> Implementation Cost<h3>")
cost_label.move(20, 590)

cost_result = QLineEdit(main_gui)
cost_result.move(200,580)
cost_result.resize(120,40)

time_label = QLabel(main_gui)
time_label.setText("<h4>  Time of Execution <h4> ")
time_label.move(460,555)

time_result = QLineEdit(main_gui)
time_result.move(450,580)
time_result.resize(150,40)

gen_num_label = QLabel(main_gui)
gen_num_label.setText("<h4>    No. of Generations  <h4> ")
gen_num_label.move(460, 460)

gen_num_result = QLineEdit(main_gui)
gen_num_result.move(450, 485)
gen_num_result.resize(150, 40)

# GUI buttons
start_btn = QPushButton("Start", main_gui)
start_btn.setGeometry(700, 550, 100, 50)
start_btn.setToolTip("click to run")

draw_btn = QPushButton("Draw", main_gui)
draw_btn.setGeometry(900, 550, 100, 50)
draw_btn.setToolTip("click to draw")

# Exit button
exit_btn = QPushButton("Exit", main_gui)
exit_btn.setGeometry(1100, 550, 100, 50)
exit_btn.clicked.connect(exit)
exit_btn.setToolTip("click to exit")
