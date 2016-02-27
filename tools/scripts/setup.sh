#!/bin/bash
# heroku create
ACTIVATE_VIRT=""
OS=$1
if [ $OS != "Win" ] && [ $OS != "Linux" ] && [ $OS != "OSX" ]
then
    printf  "Please, type name of your OS from one of the following: OSX, Win or Linux \n NOTE: input argument is case-sensitive!"
    exit
fi	


DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT_APP_DIR="$( cd "$( cd ../..)" && pwd )"

RESULT=$( virtualenv --version)
echo "Virtualenv has $RESULT version"
if [ $RESULT ]
then
    virtualenv venv;
    case "$OS" in
    "OSX" ) $( source venv/bin/activate );;
    "Linux" ) $( source venv/bin/activate );;
    "Win" ) $( venv/Scripts/activate.bat );;
    esac
else
    echo "Install virtualenv please"
fi

pip install -r requirements.txt;

printf "Setup of evnironment is finished"
