#! /usr/local/bin/python3

from PIL import Image
import argparse
char_list = list("qwertyuiopasdfghjklzxcvbnm,./;'[]")
def get_char(r,g,b,alpha = 256):
	if alpha == 0:
		return ' '
	length = len(char_list)
	gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
	unit = (256+1)/length
	return char_list[int(gray/unit)]



#命令行输入参数处理
parser = argparse.ArgumentParser()

parser.add_argument('file')    #输入文件
parser.add_argument('-o', '--output')  #输出文件
parser.add_argument('--width', type = int, default = 80) #输出字符画宽
parser.add_argument('--height', type = int, default = 80) #输出字符画高

#获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

if __name__ == '__main__':
	im = Image.open(IMG)
	im = im.resize((WIDTH,HEIGHT),Image.NEAREST)

	txt = ""
	for i in range(HEIGHT):
		for j in range(WIDTH):
			txt += get_char(*im.getpixel((j,i)))
		txt += '\n'

	print(txt)
	if OUTPUT:	
		f = open(OUTPUT,'w')
	else:
		f = open('OUTPUT.txt','w')	
	f.write(txt)
