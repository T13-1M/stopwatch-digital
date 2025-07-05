import time
import keyboard
import os

os.system("cls")



def start():
    running = False
    start_time = 0
    elapsed = 0

    print('''
---- Stopwatch Digital ----
s = Start/Stop
r = Reset
q = Quit
''')
    

    while True:
        if running:
            current = time.time()
            total = elapsed + (current - start_time)
        else:
            total = elapsed

        menit, detik = divmod(int(total), 60)
        jam, menit = divmod(menit, 60)
        timer = f"{jam:02d}:{menit:02d}:{detik:02d}"

        print(f"\rWaktu: {timer}", end="")

        if keyboard.is_pressed('s'):
            if not running:
                running = True
                start_time = time.time()
            else:
                running = False
                elapsed += time.time() - start_time
            time.sleep(0.5)
        elif keyboard.is_pressed('r'):
            running = False
            elapsed = 0
            start_time = time.time()
            time.sleep(0.5)
        elif keyboard.is_pressed('q'):
            print("\nKeluar . . .")
            break

        time.sleep(0.1)

if __name__ == "__main__":
    start()