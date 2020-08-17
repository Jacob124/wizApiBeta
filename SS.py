import wizAPI
import time

n_windows = wizAPI.count_windows()
print(f"{n_windows} windows detected")

player = wizAPI.Client().register_window()

player.screenshot('ss.png')
# while True:
#   print(player.is_loading())
#   time.sleep(1)