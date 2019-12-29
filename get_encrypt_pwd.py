# Run passed with Python 3.7.5, this is used for anaconda kickstart file option rootpw --iscrypted
python -c 'import crypt,getpass;pw=getpass.getpass();print(crypt.crypt(pw) if (pw==getpass.getpass("Confirm: ")) else print("Password not matched!"))'
