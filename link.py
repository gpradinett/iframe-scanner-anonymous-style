import threading, time, os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Frames ASCII estilo Anonymous (más detallados)
frames = [
r"""
      ███████████████████████
      ████░░░░░░░░░░░░░░░░░▀████
      ███│░░░░░░░░░░░░░░░░░│███
      ██▌│░░░░░░░░░░░░░░░░░│▐██
      ██░└┐░░░░░░░░░░░░░░░░┌┘░██
      ██░░└┐░░░░░░░░░░░░░░┌┘░░██
      ██░░┌┘▄▄▄▄▄░░░░▄▄▄▄▄└┐░░██
      ██▌░│██████▌░░░▐██████│░▐██
      ███░│▐███▀▀░░▄░░▀▀███▌│░███
      ██▀─┘░░░░░░░░░░░░░░▐█▌░░░░░└─▀██
      ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
      ████▄─┘██▌░░░░░░░▐██└─▄████
      █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
      ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
      █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
      ███████▄░░░░░░░░░░░▄███████
      ██████████▄▄▄▄▄▄▄██████████
      ███████████████████████████
""",
r"""
      ███████████████████████
      █████▀▀▀░░░░░░░▀▀▀███████
      ████│░░░░░░░░░░░░░░│████
      ██▌│░░░░░░░░░░░░░░░░│▐██
      ██░└┐░░░░░░░░░░░░░░░┌┘░██
      ██░░└┐░░░░░░░░░░░░░░┌┘░░██
      ██░░┌┘▄▄▄▄▄░░░░▄▄▄▄▄└┐░░██
      ██▌░│██████▌░░░▐██████│░▐██
      ███░│▐███▀▀░░▄░░▀▀███▌│░███
      ██▀─┘░░░░░░░░░░░░░░▐█▌░░░░└─▀██
      ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
      ████▄─┘██▌░░░░░░░▐██└─▄████
      █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
      ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
      █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
      ███████▄░░░░░░░░░░░▄███████
      ██████████▄▄▄▄▄▄▄██████████
      ███████████████████████████
""",
# ... incluyes al menos 6-8 frames variando pequeños detalles para efecto parpadeo
]

anim_running = True

def animar():
    i = 0
    while anim_running:
        os.system('cls' if os.name=='nt' else 'clear')
        print(frames[i % len(frames)])
        print("\n📝 Ingresa la URL a analizar (y presiona Enter):")
        i += 1
        time.sleep(0.2)

# Iniciar animación
t = threading.Thread(target=animar)
t.start()

# Leer URL mientras anima
try:
    url = input()
finally:
    anim_running = False
    t.join()

# Limpiar y continuar
os.system('cls' if os.name=='nt' else 'clear')
print("🚀 Analizando...\n")

# Configurar Selenium headless
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get(url)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.TAG_NAME,"iframe")))
    iframes = driver.find_elements(By.TAG_NAME,"iframe")
    print(f"✅ {len(iframes)} iframe(s) encontrados.\n")
    for iframe in iframes:
        src = iframe.get_attribute("src")
        if src:
            print("🎯 Primer iframe src:\n", src)
            break
    else:
        print("⚠️ No se encontró ningún src válido.")
except Exception as e:
    print("❌ Error:", e)
finally:
    driver.quit()
    print("\n✅ Fin.")
