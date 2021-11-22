#!/bin/bash
currentFile = realpath "$0"
echo currentFile
PS3='What kind of startup you would like to install?: '
options=("lxde" "crontab" "bashrc" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "lxde")
            echo "Exec=lxterminal --command”/bin/bash -c ‘sudo python3 /home/pi/DogPushbuttons/main_pi.py; /bin/bash’”" > ~/.config/autostart/DogPushbuttons.desktop
            echo "startup for lxde is installed."
            ;;
        "crontab")
            echo "you chose choice 2"
            ;;
        "bashrc")
            echo "you chose choice $REPLY which is $opt"
            ;;
        "Quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done

