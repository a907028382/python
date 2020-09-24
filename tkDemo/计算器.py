# -*- coding: utf-8 -*-
# @Time : 2020/6/10 11:47
# @Author : Fan
import tkinter as tk
input_num_ls = []
first_num = None
calculator_method = None

#获取数字
def get_num(ls):
    new_ls =  [10 ** i * float(num) for i,num in enumerate(ls)]

    ls_sum = sum(new_ls)
    if int(ls_sum) == ls_sum:
        return int(ls_sum)
    else:
        return ls_sum

def append_num(num):
    global input_num_ls
    #只取前面10位
    if len(num) < 10:
        input_num_ls.append(num)
    else:
        input_num_ls.append(num[:10])
    current_value.set(get_num(input_num_ls))
    print(input_num_ls)

def append_calculator(method):
    global input_num_ls,first_num,calculator_method
    calculator_method = method
    first_num = get_num(input_num_ls)
    input_num_ls = []
    print('method',calculator_method)

def calculator_result():
    global first_num,input_num_ls,calculator_method
    second_num = get_num(input_num_ls)
    #清空
    input_num_ls.clear()

    if calculator_method == '+':
        current_value.set(second_num+first_num)
        input_num_ls.append(str(second_num + first_num))
    elif calculator_method =='-':
        current_value.set(first_num - second_num)
        input_num_ls.append(str(first_num - second_num))
    elif calculator_method == '*':
        current_value.set(second_num * first_num)
        input_num_ls.append(str(second_num * first_num))
    elif calculator_method == '/':
        current_value.set(first_num / second_num)
        input_num_ls.append(str(first_num / second_num))
    print(first_num,second_num,calculator_method)

def clear():
    global first_num,input_num_ls,calculator_method
    first_num = None
    input_num_ls = []
    calculator_method = None
    current_value.set(0)

def func():
    pass

window = tk.Tk()
window.title('计算器')
window.geometry('500x500')
screen_area = tk.Frame(width = '400',height='100',bg='#ddd')
screen_area.pack()

#数据类
current_value = tk.StringVar()
current_value.set(0)
show_screen_label = tk.Label(screen_area,textvariable=current_value,bg='white',
                             width='400', height='2', font={'黑体', 40, 'bold'}, anchor='e')
show_screen_label.pack(padx=10,pady=6)

# 按键区域
button_area = tk.Frame(width='300', height='300', bg='#ccc')
button_area.pack(padx=10, pady=5)

# 添加button
tk.Button(button_area, text='C', width='15', height='1', command=lambda: clear()).grid(row='1', column='0')
tk.Button(button_area, text='+', width='15', height='1', command=lambda: append_calculator('+')).grid(row='1', column='1')
tk.Button(button_area, text='-', width='15', height='1', command=lambda: append_calculator('-')).grid(row='1', column='2')
tk.Button(button_area, text='*', width='15', height='1', command=lambda: append_calculator('*')).grid(row='1', column='3')
tk.Button(button_area, text='7', width='15', height='1', command=lambda: append_num('7')).grid(row='2', column='0')
tk.Button(button_area, text='8', width='15', height='1', command=lambda: append_num('8')).grid(row='2', column='1')
tk.Button(button_area, text='9', width='15', height='1', command=lambda: append_num('9')).grid(row='2', column='2')
tk.Button(button_area, text='/', width='15', height='1', command=lambda: append_calculator('/')).grid(row='2', column='3')
tk.Button(button_area, text='4', width='15', height='1', command=lambda: append_num('4')).grid(row='3', column='0')
tk.Button(button_area, text='5', width='15', height='1', command=lambda: append_num('5')).grid(row='3', column='1')
tk.Button(button_area, text='6', width='15', height='1', command=lambda: append_num('6')).grid(row='3', column='2')
tk.Button(button_area, text='=', width='15', height='1', command=lambda: calculator_result()).grid(row='3', column='3')
tk.Button(button_area, text='1', width='15', height='1', command=lambda: append_num('1')).grid(row='4', column='0')
tk.Button(button_area, text='2', width='15', height='1', command=lambda: append_num('2')).grid(row='4', column='1')
tk.Button(button_area, text='3', width='15', height='1', command=lambda: append_num('3')).grid(row='4', column='2')
tk.Button(button_area, text='C', width='15', height='1', command=lambda: clear()).grid(row='4', column='3')

window.mainloop()