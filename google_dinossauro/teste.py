import pyautogui as teclado
teclado.sleep(1)
for p in range(100):
    print("pre",p)
    teclado.keyDown("up")
    teclado.keyUp("up")
print("fim")