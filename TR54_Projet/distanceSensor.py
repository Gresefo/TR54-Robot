from pybricks.ev3devices import InfraredSensor

class distanceSensor:
    """ Defines a sensor that reads distance from a specific sensor. """

    def __init__(self, sensor_input):
        """
        Initializes the ultrasonic sensor component.
        :param sensor_input: the input pin of the sensor
        """
        self._sensor = InfraredSensor(sensor_input)

    def read_distance(self):
        """
        Reads the measured distance.
        :return: the distance in centimeters
        """
        return self._sensor.distance()*1.0356 - 4.3746