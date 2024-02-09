from datetime import datetime
import sys


class Logger:
    def __init__(self):
        self.logger_file = None

    def log(self, message: str):
        """
        Logs a message to the logger file
        :param message: Message to log, need str.
        :return:
        """
        message = message + " "
        self.logger_file = open("log.log", "a")
        status_message = "[Line {} at {}]".format(sys._getframe().f_back.f_lineno, sys.argv[0])
        if len(message) < 91:
            if len(message + status_message) > 91:
                self.logger_file.write(
                    "[{}] {}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"), message)
                )
                self.logger_file.write("{}{}\n".format(" " * (120 - len(status_message)), status_message))
            else:
                self.logger_file.write(
                    "[{}] {}{}{}\n".format(
                        datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
                        message,
                        " " * (91 - len(status_message) - len(message)),
                        status_message
                    )
                )
        elif len(message + status_message) < 182:
            self.logger_file.write(
                "[{}] {}\n{}{}{}{}\n".format(
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
                    message[0:91],
                    " " * 29,
                    message[91:],
                    " " * (91 - len(message[91:]) - len(status_message)),
                    status_message
                )
            )
        else:
            self.logger_file.write(
                "[{}] {}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"), message[0:91])
            )
            for i in [(i + 1) * 91 for i in range(int(len(message) / 91) - 1)]:
                self.logger_file.write("{}{}\n".format(" " * 29, message[i:i + 91]))
            if len(message[(int(len(message) / 91)) * 91:]) < 91:
                if len(message[(int(len(message) / 91)) * 91:] + status_message) > 91:
                    self.logger_file.write(
                        "{}{}\n".format(" " * 29, message[(int(len(message) / 91)) * 91:])
                    )
                    self.logger_file.write("{}{}\n".format(" " * (120 - len(status_message)), status_message))
                else:
                    self.logger_file.write(
                        "{}{}{}{}\n".format(
                            " " * 29,
                            message[(int(len(message) / 91)) * 91:],
                            " " * (91 - len(status_message) - len(message[(int(len(message) / 91)) * 91:])),
                            status_message
                        )
                    )
        self.logger_file.write("{}\n".format("=" * 120))
        self.logger_file.close()


if __name__ == "__main__":
    logger = Logger()
    logger.log("Hello World")
