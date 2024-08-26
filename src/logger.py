import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # Setting Up the Log Filename

# Creating the Logs Directory
logs_path = os.path.join(os.getcwd(),"logs")
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE) # Setting Up the Full Log File Path

# Configuring the Logging
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)
# %(asctime)s: Inserts the date and time when the log message was generated
# %(lineno)d: Inserts the line number in the source code where the logging call was made.
# %(name)s: Inserts the name of the logger that logged the message.
# %(levelname)s: Inserts the level of the message (e.g., INFO, DEBUG, WARNING).
# %(message)s: Inserts the actual log message.
#This format string ensures that every log message will include a timestamp, the line number in the code, the logger's name, the severity level of the message, and the actual message itself.
# level=logging.INFO: This sets the logging level to INFO. Only events with a severity of INFO or higher (e.g., WARNING, ERROR, CRITICAL) will be logged. Lower-severity messages (like DEBUG) will be ignored.


# if __name__ == "__main__":
#     logging.info("Logging has started")