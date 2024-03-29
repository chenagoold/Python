# pip install qrcode pillow
import qrcode

def get_qrcode(url='https://google.com', name='default'):
	qr = qrcode.make(data=url)
	qr.save(stream=f'{name}.png')

	return f'QR code was created! Open the {name}.pnp'

def main():
	print(get_qrcode(url='https://www.instagram.com/dimobix/', name='Dimobix'))
	print(get_qrcode(url='https://www.instagram.com/juliya__genis/',name='Ylia'))

if __name__ == '__main__':
	main()
	