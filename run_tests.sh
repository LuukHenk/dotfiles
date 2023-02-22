MY_PATH="`dirname \"$0\"`"

pip install $MY_PATH && pytest $MY_PATH

