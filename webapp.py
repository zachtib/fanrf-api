from flask import jsonify
from flask.app import Flask

from fancontrol import FanController, FanControlError

app = Flask(__name__)
controller = FanController()


@app.route('/status/')
def status():
    return jsonify(controller.get_status())


@app.route('/fan/<int:fan_speed>/')
def fan_control(fan_speed: int):
    try:
        return jsonify(controller.set_fan_speed(fan_speed))
    except FanControlError as error:
        return jsonify(error.to_result())


@app.route('/light/<int:brightness>/')
def brightness_control(brightness: int):
    try:
        return jsonify(controller.set_brightness(brightness))
    except FanControlError as error:
        return jsonify(error.to_result())


if __name__ == '__main__':
    app.run()
