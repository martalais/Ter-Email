# coding: utf-8
# Marta Laís (c)
# Envio automático de e-mails com anexos via terminal.
# Após a implementação, basta criar uma rotina no crontab para a sua execução.

from email import Encoders
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.Utils import COMMASPACE, formatdate
import smtplib


# Funcao de envio do e-mail.
def enviaEmail(servidor, porta, FROM, PASS, TO, subject, texto, anexo=[]):
	global saida
	servidor = servidor
	porta = porta
	FROM = FROM
	PASS = PASS
	TO = TO
	subject = subject
	texto = texto
	msg = MIMEMultipart()
	msg['From'] = FROM
	msg['To'] = TO
	msg['Subject'] = subject
	msg.attach(MIMEText(texto))

	  # Anexa os arquivos.
	  for i in anexo:
		part = MIMEBase('application', 'octet-stream')
		part.set_payload(open(i, 'rb').read())
		Encoders.encode_base64(part)
		part.add_header('Content-Disposition','attachment;filename="%s"'% os.path.basename(i))
		msg.attach(part)

	  try:
		gm = smtplib.SMTP(servidor,porta)
		gm.ehlo()
		gm.starttls()
		gm.ehlo()
		gm.login(FROM, PASS)
		gm.sendmail(FROM, TO, msg.as_string())
		gm.close()

	  except Exception,e:
		mensagemErro = "Erro ao enviar o e-mail." % str(e)
		print '%s' % mensagemErro

# Destinatario do e-mail.
destinatario = ''

# Assunto do e-mail.
assunto = ''

# Mensagem do e-mail.
mensagem = ''

# Endereco do servidor smtp que sera utilizado.
# Um exemplo e: smtp.gmail.com 
servidor= ''

# Porta do servidor smtp.
# Um exemplo e: 587 (gmail)
porta =

# Endereco de e-mail e senha do remetente.
remetente = ''
senha = ''

# Chamada de funcao de envio do e=mail.
# Note que em [""] deve ser referenciado o caminho exato do anexo. 
enviaEmail(servidor, porta, remetente, senha, destinatario, assunto, mensagem, [""]) 
