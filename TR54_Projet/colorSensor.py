from pybricks.ev3devices import ColorSensor

class colorSensor:
    """ Defines a color sensor component. """

    def __init__(self, sensor_input):
        """
        Initializes the sensor color component.
        :param sensor_input: the input pin of the sensor
        """
        self._sensor = ColorSensor(sensor_input)

    def read_intensity(self):
        """
        Reads the reflected light intensity from the color sensor.
        :return: the intensity in [0; 100]
        """
        return self._sensor.reflection()

    def read_color(self):
        """
        Reads the color from the color sensor.
        :return: the index of the found color
        """
        return self._sensor.rgb()