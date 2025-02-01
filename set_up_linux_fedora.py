from pyinfra.operations import files, git, server,dnf

from common import (cwd_path, home_path_str,
                    personal_projects_path_str, projects_path_str,
                    work_projects_path_str, zshrc_path_str)


def setup_mac_using_brew():
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







def setup_zshrc():
    """
    Put all my settin in .zshrc.
    """

    files.file(path=zshrc_path_str)

    files.line(path=zshrc_path_str,
               line='export EDITOR=nvim')
    files.line(path=zshrc_path_str,
               line='alias mnvim="NVIM_APPNAME=nvim-minimal nvim"')
    files.line(path=zshrc_path_str,
               line='alias nvims="nvim -S"')
    files.line(path=zshrc_path_str,
               line='alias vimconfig="vim ~/.vimrc"')
    files.line(path=zshrc_path_str,
               line='alias nvimconfig="nvim ~/.config/nvim/init.lua"')
    files.line(path=zshrc_path_str,
               line='alias mnvim="NVIM_APPNAME=nvim-minimal nvim"')
    files.line(path=zshrc_path_str,
               line='alias cdfzf=\'cd "$(find . -type d | fzf )"\'')
    files.line(path=zshrc_path_str,
               line='alias cdfzfgit=\'cd "$(find . -name .git -type d -prune | fzf)/.."\'')
    files.line(path=zshrc_path_str,
               line=f'export ILYASYOY_DOTFILES_DIR="{cwd_path}"')
    files.line(path=zshrc_path_str,
               line='export PATH="${ILYASYOY_DOTFILES_DIR}/bin:$PATH"')
    files.line(path=zshrc_path_str,
               line='alias ilyasyoy-dotfiles="cd ${ILYASYOY_DOTFILES_DIR}"')
    files.line(path=zshrc_path_str,
               line='alias ilyasyoy-notes="cd ~/vimwiki"')
    files.line(path=zshrc_path_str,
               line='export PATH="$HOME/go/bin:$PATH"')




def setup_ohmyzsh():
    """
    No comments here, everybody knows this.
    """
    server.shell(commands=[
                 'sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" | grep -e "already exists" -e "is now installed"'])



setup_mac_using_brew()
setup_basic_directories()
setup_zshrc()
setup_ohmyzsh()
