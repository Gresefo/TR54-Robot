class basicPIDComponent:
    """ Defines a basic PID component. """

    def __init__(self, kp, ki, kd):
        """
        Initializes the PID parameters.
        :param kp: the proportional coefficient
        :param ki: the integral coefficient
        :param kd: the derivative coefficient
        """
        self._kp = kp
        self._ki = ki
        self._kd = kd
        self._error = 0
        self._sum_error = 0
        self._delta_error = 0
        self._last_error = 0

    def compute(self, error, delta_time):
        """
        Computes the steering value from the given parameters.
        :param error: the current error
        :param delta_time: the current delta time in seconds
        :return: the computed steering
        """
        self._sum_error += self._error
        self._delta_error = self._error - self._last_error
        self._last_error = self._error
        p = self._kp * error
        i = self._ki * self._sum_error * delta_time
        d = self._kd * (self._delta_error / delta_time)
        return p + i + d