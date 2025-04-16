from pyinfra.operations import files, server, dnf

from common import (personal_projects_path_str, projects_path_str,
                    work_projects_path_str)


def setup_linux_using_dnf() :
    """
    Install must-have packages I use almost every day.
    """
    dnf.packages(
        packages=[
            "docker",
            "go",
            "nmap",
            "postgresql-server",
            "mysql-server",
            "nmap",
            "bat",
            "qbittorrent",
            "htop",
            "gnome-shell-extension-tool"


        ],

    )

    server.shell(commands=[
        "sudo systemctl enable --now docker",
        "sudo systemctl enable --now postgresql"
    ])


def setup_basic_directories() :
    """
    Here I create basic directories I use every day.
    """
    for path in [
        projects_path_str,
        personal_projects_path_str,
        work_projects_path_str
    ] :
        files.directory(
            path=path,
            present=False,
            _sudo=False
        )


def setup_snap_and_flatpak_packages() :
    """
    Install must-have packages using Snap.
    """
    server.shell(commands=[
        "sudo snap install --classic code",
        "sudo snap install --classic telegram-desktop"
        "flatpak install flathub dev.vencord.Vesktop"
        "sudo snap install obsidian --classic"
        "flatpak install flathub ru.yandex.Browser"
    ])

def setup_zed() :
    """
    Install Zed
    """

    server.shell(commands=[
        "sudo curl -f https://zed.dev/install.sh | sh"
    ])

def setup_ohmyzsh() :
    """
    Install Oh My Zsh non-interactively.
    """
    server.shell(commands=[
        'ZSH=${HOME}/.oh-my-zsh sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" --unattended'
    ])


setup_linux_using_dnf()
setup_zed()
setup_basic_directories()
setup_ohmyzsh()
