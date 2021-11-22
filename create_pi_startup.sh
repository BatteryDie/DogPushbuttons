#!/bin/bash
currentFile = realpath "$0"
echo currentFile
PS3='What kind of startup you would like to install?: '
options=("lxde" "crontab" "remove" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "lxde")
            echo "Exec=lxterminal --command”/bin/bash -c ‘sudo python3 $currentFile/main_pi.py; /bin/bash’”" > ~/.config/autostart/DogPushbuttons.desktop
            echo "Startup for lxde is installed. It will start in LXDE terminal when desktop is loaded."
            ;;
        "crontab")
            echo "Startup for crontab is installed. It will start during boot."
            ;;
        "remove")
            echo "Removing..."
            ;;
        "Quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done

