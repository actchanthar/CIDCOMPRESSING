import logging
import subprocess
from os import path as ospath
from os import execl as osexecl
from sys import executable

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO
)

# Define the upstream repository and branch
UPSTREAM_REPO = 'https://github.com/actchanthar/CIDCOMPRESSING'
UPSTREAM_BRANCH = 'main'

if UPSTREAM_REPO:
    if ospath.exists('.git'):
        subprocess.run(["rm", "-rf", ".git"])
    
    # Run the git commands to update the repository
    update = subprocess.run(
        [
            f"git init -q && git add . && git commit -sm update -q && "
            f"git remote add origin {UPSTREAM_REPO} && git fetch origin -q && "
            f"git reset --hard origin/{UPSTREAM_BRANCH} -q"
        ],
        shell=True
    )
    
    # Check if the update was successful
    if update.returncode == 0:
        logging.info('Successfully upgraded with latest commit from UPSTREAM_REPO')
        osexecl(executable, executable, "-m", "BindhuEncoder")
    else:
        logging.error('Something went wrong while upgrading, check UPSTREAM_REPO if valid or not!')

# Restart the script
osexecl(executable, executable, "-m", "BindhuEncoder")
