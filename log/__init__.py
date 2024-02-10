from datetime import datetime
import sys
from BuildInClasses import RichText
import os
import json


class Logger:
    def __init__(self):
        self.logger_file = None
        self.log_header = """    Log from {project_name} with MINI Logger

    {project_name}: {project_description}
    Developed by {project_author} at {project_url}.
    Version: {project_version}

{time_during:>120}"""

    def log(self, message: str | RichText, status: str):
        """
        Logs a message to the logger file.
        There will 120 cols in log file.
        :param message: Message to log, need str.
        :param status: Recommend from QuickValues.Log, need 4 alphabets.
        :return:
        """
        message = message + " "
        if not "logs/{}.log".format(datetime.now().strftime("%Y-%m-%d %H")) in os.listdir("logs"):
            project_info = json.load(open("project_info.json", "r"))
            self.logger_file = open("logs/{}.log".format(datetime.now().strftime("%Y-%m-%d %H")), "w")
            self.logger_file.write(self.log_header.format(
                "?",
                project_name=project_info["name"],
                project_version=project_info["version"],
                project_description=project_info["description"],
                project_url=project_info["url"],
                project_author=project_info["author"],
                time_during="[Date {} {}:00 - {}:00]".format(datetime.now().strftime("%Y-%m-%d"),
                                                             str(datetime.now().hour),
                                                             str(datetime.now().hour + 1)),
            ) + "\n" + "=" * 120 + "\n")
        self.logger_file = open("logs/{}.log".format(datetime.now().strftime("%Y-%m-%d %H")), "a")
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


class Logs:
    def __init__(self):
        pass
