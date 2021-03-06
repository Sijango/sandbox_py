def enlarge(image):
    result_image = []
    for line in image:
        temporary_line = ''
        for item in line:
            temporary_line += item + item
        result_image.append(temporary_line)
        result_image.append(temporary_line)
    return result_image 

#Реализуйте функцию enlarge, которая принимает изображение
# в виде двумерного списка строк и увеличивает его в два раза, 
# то есть удваивает каждый символ по горизонтали и вертикали.