#bin/bash

### Python virtual enviroment version to install, 3.8 required
### Installs and checks for Ubuntu packages required to install python virtual environments
py_ver=3.8
deps=("git" "virtualenv" "python3-dev")
echo "Preparing to install the following local dependancies for Datertots"
for d in ${deps[@]};
    do
    echo $d
done
echo $'\n& these python virutal-env pip packages ⮷⮷⮷'
echo "$(cat requirements.pip)"
echo $'\nIs this okay(y/n)?'
read yn
if [ $yn != "y" ]
    then
    echo Exiting...
    exit 
    else
    echo "Fetching and installing required Ubuntu packages..."
    sudo apt-get -y install ${deps[@]}
    ### Installs virtual enviroment into current working directory
    echo 'Installing Python$py_ver virtual environment in $PWD'
    virtualenv --python=python$py_ver $PWD
    echo 'Activating python virtualenv...'

    activate (){
        source ./bin/activate
        }

    activate
    ### Activates the virtual enviroment by default use "source bin/activate"
    ### inside enviroment directory.
    echo "Installing python pip packages..."
    pip install -r $PWD/requirements.pip
    deactivate
    echo "Deactivating python virtualenv..."
    echo "All packages have been successfully installed!"
    echo "Try typing "\"" source bin/activate "\"" to activate your python virtualenv, then "\"" deactivate "\"" to exit from it at anytime."
    echo "From within the virtualenv to start Jupyter Notebook type: "\"" jupyter notebook "\"
    exit 1
fi
