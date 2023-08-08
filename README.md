### Options

In this repository, we go through setting up infrastructure for the dealing with and analysis of options positions and strategies. In order to work with this repository, you need to set up a couple of things: 

1. Set up a `.env` file in the root of the directory like this: 
```text
ROBINHOOD_USERNAME={your email for robinhood account}
ROBINHOOD_PASSWORD={your password to robinhood account}
```
2. set up virtual environment and install requisite python packages

```bash
sudo apt update 
sudo apt upgrade 
sudo apt-get python3 

# Then after you have python3 installed, you can set up your environment 
git clone options

# Going into the directory that you just cloned
cd options 

python3 -m venv venv

# Activating the environment 
source venv/bin/activate 
pip install -r requirements.txt

```

Once this is setup, try to run the `robinhood/robinhood_account.py` file and see your options greeks report. 

If you have any questions, please feel free to contact me at `srerrie@gmail.com`. 