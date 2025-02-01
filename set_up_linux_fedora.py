from pyinfra.operations import files, git, server,dnf

from common import (cwd_path, home_path_str,
                    personal_projects_path_str, projects_path_str,
                    work_projects_path_str, zshrc_path_str)


def setup_linux_using_dnf():
    """
    Install must-have packages I use almost every day.
    """

    dnf.packages(
        packages=[
           "docker",
            "go",
            "nmap",

        ],
        _sudo=True
    )



def setup_basic_directories():
    """
    Here I craate basic directories I use every day.
    """
    for path in [
        projects_path_str,
        personal_projects_path_str,
        work_projects_path_str
    ]:
        files.directory(
            path=path,
            present=True,
        )




def setup_ohmyzsh():
    """
    No comments here, everybody knows this.
    """
    server.shell(commands=[
                 'sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" | grep -e "already exists" -e "is now installed"'])

setup_linux_using_dnf()
setup_basic_directories()

setup_ohmyzsh()
