import wizAPI
import time

n_windows = wizAPI.count_windows()
print(f"{n_windows} windows detected")

player = wizAPI.Client().register_window()

# player.screenshot('ss.png')
while True:
  print("Is Loading?", player.is_loading())
  print("Is mana low?", player.is_mana_low())
  print("Is health low?", player.is_health_low())
  print("Is idle?", player.is_idle())
  time.sleep(2)