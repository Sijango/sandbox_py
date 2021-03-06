#Задача заключается в том, что нужно реализовать функцию enlarge, которая увеличивает переданное "изображение"
#в два раза: каждый "пиксель" удваивается по горизонтали и вертикали. Изображением служит список строк, а пиксели в нём — символы строк.

curry = lambda f: lambda x: lambda y: f(x, y) 
compose = lambda f: lambda g: lambda x: f(g(x))  

pair = lambda x: [x, x] 
dup = lambda x: x + x  

# BEGIN (write your solution here)
from functools import reduce


def enlarge(image):
	image = list(map(dup, image))
	return image
# END

if __name__ == '__main__':
    display = compose(print)('\n'.join)
    display(enlarge([
        '+--+',
        '|x |',
        '| o|',
        '+--+',
    ]))