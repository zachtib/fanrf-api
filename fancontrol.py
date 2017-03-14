class FanControlError(Exception):
    def __init__(self, message):
        self.message = message

    def to_result(self):
        return dict(message=self.message, success=False)


class FanController:

    def __init__(self):
        self._fan_speed = 0
        self._brightness = 0

    def get_status(self):
        return dict(fan_speed=self._fan_speed, brightness=self._brightness)

    def set_fan_speed(self, fan_speed):
        if not (0 <= fan_speed <= 3):
            raise FanControlError("Fan speed out of range")
        self._fan_speed = fan_speed
        return self._send()

    def set_brightness(self, brightness):
        if not (0 <= brightness <= 100):
            raise FanControlError("Brightness out of range")
        self._brightness = brightness
        return self._send()

    def _send(self):
        print(self._encode())  # TODO: send the state to the RF module here
        return dict(fan_speed=self._fan_speed, brightness=self._brightness, success=True)

    def _encode(self):
        # TODO: Make this return the correct format
        return '{0:04b}'.format(self._fan_speed) + '{0:08b}'.format(self._brightness)
