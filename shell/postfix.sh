rpm -qa | grep postfix # to check the existence of postfix
yum install postfix
yum install s-nail # mailx is replaced by s-nail
/etc/postfix/main.cf
vim main.cf
    relayhost= [smtp.gmail.com]:587
    myhostname=ip-172-31-29-111.ec2.internal
    # add below lines in the bottom of main.cf "shift+g to go scroll down to bottom"
    smtp_sasl_password_maps = hash:/etc/postfix/sasl/sasl_passwd
    smtp_sasl_auth_enable = yes
    smtp_tls_security_level = encrypt
    smtp_sasl_security_options = noanonymous
cd /etc/postfix
mkdir sasl
cd sasl
touch sasl_passwd
vim sasl_passwd
    [smtp.gmail.com]:587 pfirdose1988@gmail.com:mxabzvcsrblljtlw
postmap sasl_passwd
chmod 600 sasl_passwd.db

systemctl start postfix.service

echo "test mail" | mail -s "postfix test" pfirdose1988@gmail.com





