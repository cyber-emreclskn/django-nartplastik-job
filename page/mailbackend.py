from django.core import mail
from django.core.mail.backends.smtp import EmailBackend
from page.models import SiteSettings

def send_mail(subject, contact_list, body):

    try:
        mail_setting = SiteSettings.objects.get(site_ismi = 'Nart Plastik')
        
        host = mail_setting.smtp_mail_server
        host_user = mail_setting.smtp_mail_name
        host_pass = mail_setting.smtp_mail_password
        host_port = mail_setting.smtp_port
        
        con = mail.get_connection(
            host = mail_setting.smtp_mail_server,
            username = mail_setting.smtp_mail_name,
            password = mail_setting.smtp_mail_password,
            port = mail_setting.smtp_port,
        )
        
        print('Django connected to the SMTP server')

        
        

        mail_obj = EmailBackend(
            host=host,
            port=host_port,
            password=host_pass,
            username=host_user,
            use_tls=True,
            timeout=10
        )

        msg = mail.EmailMessage(
            subject=subject,
            body=body,
            from_email=host_user,
            to=[contact_list],
            connection=con,
        )
        mail_obj.send_messages([msg])
        print('Message has been sent.')

        mail_obj.close()
        print('SMTP server closed')
        return True

    except Exception as _error:
        print('Error in sending mail >> {}'.format(_error))
        return False