import subprocess
import sys
from colorama import Fore, init

init(autoreset=True)

def run_git_commands():
    try:
        print(f"{Fore.CYAN}🚀 Starting GitHub synchronization process...")
        
        # 1. Додаємо всі зміни
        subprocess.run(["git", "add", "."], check=True)
        
        # 2. Створюємо коміт з автоматичним повідомленням
        commit_message = "Update sites database and engine"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        # 3. Відправляємо на сервер
        subprocess.run(["git", "push", "origin", "main"], check=True)
        
        print(f"{Fore.GREEN}✅ Project successfully updated on GitHub!")
        
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}❌ Error during synchronization: {e}")
    except Exception as e:
        print(f"{Fore.RED}❌ Something went wrong: {e}")

if __name__ == "__main__":
    run_git_commands()