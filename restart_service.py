# restart_service.py

import win32serviceutil
import win32service
import win32event
import servicemanager
import logging
import os
import sys
import time
from datetime import datetime, timezone
import psutil

# Import your existing functions
import riotliblite

# Configure logging
logging.basicConfig(
    filename='C:\\Program Files\\RestartService\\restart_service.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

class RestartPCService(win32serviceutil.ServiceFramework):
    _svc_name_ = 'RestartPCService'
    _svc_display_name_ = 'Restart PC Service'
    _svc_description_ = 'Monitors game results and restarts PC upon loss.'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)
        self.running = True

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        logging.info('Service is stopping...')
        self.running = False
        win32event.SetEvent(self.stop_event)

    def SvcDoRun(self):
        logging.info('Service is starting...')
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, '')
        )
        self.main()

    def main(self):
        # Your existing code starts here
        game_name = "agis feet"
        tag_line = "love"

        accounts = [("agis feet","love"),("Dog Yangler","FFit"),("Alahh Akbarr","911")]

        processed_games = set()

        while self.running:
            for acc in accounts:
                game_name = acc[0]
                tag_line = acc[1]

                try:
                    lg = self.get_last_game(game_name, tag_line)
                    logging.info(f"Checking game: {lg.match_id}")

                    if lg.match_id not in processed_games:
                        if self.game_ended_recently(lg):
                            if not self.did_i_win(lg):
                                logging.info("You lost the last game. Restarting PC.")
                                self.restart_pc()
                            else:
                                logging.info("You won the last game. No action needed.")
                        else:
                            logging.info("Last game did not end within the last 2 minutes.")
                        processed_games.add(lg.match_id)
                    else:
                        logging.info("No new games to process.")

                    # Wait for 60 seconds before checking again
                    for _ in range(10):
                        if not self.running:
                            break
                        time.sleep(1)
                except Exception as e:
                    logging.error(f"An error occurred: {e}", exc_info=True)
                    time.sleep(10)

    # Define your methods within the class
    def get_last_game(self, game_name, tag_line):
        puuid = riotliblite.getPuuid(game_name, tag_line)
        lastGame, status = riotliblite.last_game(puuid)
        LASTGAME = riotliblite.Game(puuid, lastGame['metadata']['matchId'])
        return LASTGAME

    def did_i_win(self, game):
        win = game.me.win
        logging.info(f"Win status: {win}")
        return win

    def restart_pc(self):
        logging.info("Restarting the PC...")
        os.system("shutdown /r /t 1")

    def game_ended_recently(self, game):
        # Get game start time in milliseconds
        game_start_timestamp = game.match.info.game_start_timestamp  # In milliseconds

        # Get game duration in seconds
        game_duration = game.match.info.game_duration  # In seconds

        # Calculate game end timestamp in milliseconds
        game_end_timestamp = game_start_timestamp + (game_duration * 1000)

        # Convert to datetime
        game_end_datetime = datetime.fromtimestamp(game_end_timestamp / 1000, tz=timezone.utc)

        # Get current time
        current_time = datetime.now(timezone.utc)

        # Calculate time difference
        time_diff = current_time - game_end_datetime

        logging.info(f"game ended {time_diff} seconds ago")

        # Check if the game ended within the last 2 minutes
        if 0 <= time_diff.total_seconds() <= 120:
            logging.info("The game ended within the last 2 minutes.")
            return True
        else:
            logging.info("The game did not end within the last 2 minutes.")
            return False

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(RestartPCService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(RestartPCService)
