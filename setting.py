import os
import time

TOKEN_FILE_PATH = 'chatgpt_token.txt'

def save_token(token):
    with open(TOKEN_FILE_PATH, 'w') as file:
        file.write(token)

def load_token():
    try:
        with open(TOKEN_FILE_PATH, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def check_jq_installed():
    try:
        result = os.system('which jq > /dev/null 2>&1')
        return result == 0
    except Exception as e:
        print(f"Error checking jq installation: {str(e)}")
        return False

print("\033[96m" + """
                                              ██████████████████                                
                                        ▓▓▓▓██░░░░▒▒░░▒▒▒▒▒▒▓▓▒▒██▓▓                            
                                    ████░░░░░░▓▓░░░░░░░░░░░░▓▓░░░░░░██▓▓                        
                                ████░░░░░░░░░░▓▓░░░░░░░░░░░░░░▓▓░░░░░░░░██                      
                              ██░░░░░░░░░░░░░░░░▓▓░░░░░░░░░░░░▓▓░░░░░░░░░░██                    
                            ██░░▓▓▓▓░░░░░░░░░░░░▓▓░░░░░░░░░░░░▓▓░░░░░░░░░░░░██                  
        ▒▒                  ██░░░░░░▒▒░░░░░░░░░░▓▓░░░░░░░░░░▓▓░░░░░░░░░░░░▓▓░░██                
▒▒        ▒▒              ██░░░░░░░░░░▓▓░░░░░░░░▓▓░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░▓▓░░██                
  ▓▓      ▒▒              ██░░░░░░░░░░░░▓▓░░░░▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓░░░░░░░░░░▓▓░░░░░░██              
    ▒▒    ▓▓              ██░░░░░░░░░░░░▓▓░░▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▓▓░░░░░░██              
    ▓▓      ▓▓            ██░░░░░░░░░░░░░░▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒░░▓▓░░░░░░░░░░██            
      ▓▓    ▒▒          ▓▓░░▒▒▒▒░░░░░░░░░░▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒██            
      ▓▓    ▒▒          ██░░░░░░▓▓▓▓░░░░▒▒▒▒▓▓▒▒▒▒████████▒▒▒▒▒▒▓▓▓▓▒▒░░░░░░░░▓▓░░██            
      ▓▓    ▒▒          ██░░░░░░░░░░▓▓░░▒▒▒▒▓▓▒▒██        ██▓▓▓▓▒▒▒▒▒▒░░░░░░▓▓░░░░██            
        ▓▓▓▓██▓▓        ██░░░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓            ██▒▒▒▒▒▒▒▒░░▒▒▒▒░░░░░░░░▓▓          
    ████░░░░░░░░████████░░▓▓░░░░░░░░░░▓▓▒▒▒▒██                ██▒▒▒▒▓▓▓▓░░░░░░░░░░░░██          
  ██░░░░░░░░░░░░░░██░░░░░░░░▓▓░░░░░░░░▒▒▓▓▒▒██                ██▓▓▓▓▒▒▒▒░░░░░░░░░░▓▓██          
  ██░░██░░░░░░██░░██░░░░░░░░▓▓░░░░░░░░▒▒▓▓██                    ██▒▒▒▒▒▒░░░░░░░░▓▓░░░░██        
▓▓░░██░░██░░██░░██░░██░░░░░░░░▓▓░░░░▒▒▒▒▒▒██                    ██▒▒▒▒▒▒▒▒░░▓▓▓▓░░░░░░░░████    
██░░░░░░░░░░░░░░░░░░██░░░░░░░░▓▓░░░░▒▒▒▒▒▒██                    ▓▓▒▒▒▒▒▒▓▓▓▓░░░░░░░░░░░░▓▓░░██  
██░░░░░░░░░░░░░░░░░░██░░░░░░░░▓▓░░░░▒▒▒▒██                      ██▓▓▓▓▓▓▒▒▒▒░░░░░░░░░░░░▒▒░░░░██
██░░▓▓▓▓░░░░████░░░░██░░░░░░▒▒▒▒▓▓░░░░▒▒██                      ██▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▓▓░░░░░░██
██░░██▓▓████▓▓██░░░░██▒▒▒▒▒▒▒▒▒▒▓▓░░▒▒▒▒██                        ██▒▒▒▒▒▒▒▒▒▒░░░░░░▓▓░░░░░░▒▒██
██░░██▒▒▓▓▓▓▒▒██░░▒▒██▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒██                          ██▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓░░░░░░░░▒▒██
██▒▒▒▒▓▓██████▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▓▓████                            ██▓▓▒▒▒▒▓▓▓▓▓▓░░░░░░░░▒▒▒▒▒▒██
  ██▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██████                                  ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██  
    ██▒▒▒▒▒▒▒▒██████████████                                          ████▒▒▒▒▒▒▒▒▒▒▒▒▒▒████    
      ████████                                                            ██████████████        

                          
                       Other Tools Check t.me/garudasec4
                                   or Check
                GarudaSecurity Website https://magicgreen.com.tr/
                          WormGpt By GarudaSecurity 
\033[0m""")
# Cek apakah token sudah tersimpan
saved_token = load_token()
if saved_token:
    print(f'\033[36mToken yang tersimpan: {saved_token}')
    masuk = input('\033[38mApakah ingin menggunakan token yang tersimpan? (yes/no): \033[35m')
    if masuk.lower() == 'yes':
        os.system(f'export CHATGPT_TOKEN={saved_token}')
    else:
        masuk = input('\033[38mMasukkan token baru: \033[35m')
        os.system(f'export CHATGPT_TOKEN={masuk}')
        save_token(masuk)
else:
    masuk = input('\033[38mMasukkan token lu bang: \033[35m')
    os.system(f'export CHATGPT_TOKEN={masuk}')
    save_token(masuk)

# Cek apakah jq sudah diinstal
if not check_jq_installed():
    print('\033[36mSukses memasukkan token, sedang menginstall jq')
    time.sleep(2.5)
    os.system('clear')
    os.system('apt install jq')
else:
    print('\033[36mjq sudah terinstal. Tidak perlu menginstal lagi.')

exit_choice = input('\033[37mYakin ingin keluar? (yes/no): \033[37m')

if exit_choice.lower() == 'yes':
    print('\033[31mSedang keluar mohon tunggu')
else:
    print('\033[32mTerima kasih! Tetap semangat!\033[0m')
