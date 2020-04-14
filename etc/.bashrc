### Settings ###

# Case-insensitive globbing (used in pathname expansion)
shopt -s nocaseglob;
#
# Append to the Bash history file, rather than overwriting it
shopt -s histappend;
#
# Autocorrect typos in path names when using `cd`
shopt -s cdspell;
#
# * `autocd`, e.g. `**/qux` will enter `./foo/bar/baz/qux`
# * Recursive globbing, e.g. `echo **/*.txt`
for option in autocd globstar; do
  shopt -s "$option" 2> /dev/null;
done;
#
# Add tab completion for many Bash commands
if which brew &> /dev/null && [ -f "$(brew --prefix)/share/bash-completion/bash_completi
on" ]; then
  source "$(brew --prefix)/share/bash-completion/bash_completion";
elif [ -f /etc/bash_completion ]; then
  source /etc/bash_completion;
fi;
#
#

### Colors ###

# Set colorcode
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac
#
# Determine if the color prompt is availible
if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
  # We have color support; assume it's compliant with Ecma-48
  # (ISO/IEC-6429). (Lack of such support is extremely rare, and such
  # a case would tend to support setf rather than setaf.)
  color_prompt=yes
    else
  color_prompt=
    fi
fi
#
# ANSI color codes
RS="\[\033[0m\]"    # reset
HC="\[\033[1m\]"    # hicolor
UL="\[\033[4m\]"    # underline
INV="\[\033[7m\]"   # inverse background and foreground
FBLK="\[\033[30m\]" # foreground black
FRED="\[\033[31m\]" # foreground red
FGRN="\[\033[32m\]" # foreground green
FYEL="\[\033[33m\]" # foreground yellow
FBLE="\[\033[34m\]" # foreground blue
FMAG="\[\033[35m\]" # foreground magenta
FCYN="\[\033[36m\]" # foreground cyan
FWHT="\[\033[37m\]" # foreground white
BBLK="\[\033[40m\]" # background black
BRED="\[\033[41m\]" # background red
BGRN="\[\033[42m\]" # background green
BYEL="\[\033[43m\]" # background yellow
BBLE="\[\033[44m\]" # background blue
BMAG="\[\033[45m\]" # background magenta
BCYN="\[\033[46m\]" # background cyan
BWHT="\[\033[47m\]" # background whiteS="\[\033[0m\]"    # reset
#
# Set shell colors
if [ "$color_prompt" = yes ]; then
    PS1="$HC$FYEL${debian_chroot:+($debian_chroot)}\u$FMAG@\h$FWHT: $FBLE\w$FWHT\$ $RS"
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
#
unset color_prompt force_color_prompt
#
#

### Aliases ###

# Bash statement shortcuts
alias qq='exit'
alias ls='ls --color=auto'
alias ll='ls -l -h -a --color=auto'
alias rmf='rm -f'
alias Rm='rm -r'
alias Rmf='rm -f -r'
#
# Easy navigation
alias home='cd ~/Dropbox/home'
alias sid='cd ~/Dropbox/home/sid'
alias github='cd ~/Dropbox/home/github'
#
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias .....='cd ../../../..'
#
# Program aliases
alias files='nautilus .'
alias storage='ncdu'
alias python=python3
