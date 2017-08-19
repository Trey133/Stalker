import gnupg
gpg = gnupg.GPG(homedir='~/.gnupg')
recipient = 'terminal'
data = 'This is a test'
encrypt = gpg.encrypt(data, recipient, output='/usr/share/stalker/gpgoutput.txt.gpg')
stream = open('/usr/share/stalker/gpgoutput.txt.gpg','rb')
decrypt = gpg.decrypt_file(stream)
print str(decrypt)
