def return_10():
    return 10

def add(num_first,num_second):
    sum_two=num_first+num_second
    return sum_two

def subtract( num_second,num_first):
     substract_two=num_second-num_first
     return substract_two

def  multiply(num_first,num_second):
    multiply_two=num_first*num_second
    return multiply_two

def  divide(num_first,num_second):
    divide_two=num_first/num_second
    return  divide_two

# print(len( "A string of length 21"))
def length_of_string(string):
    str_length=len(string)
    return str_length

def join_string( str_one, str_two):
    joined_str=str_one+str_two
    return joined_str

def  add_string_as_number(str_num_one,str_num_two):
    add_result=int(str_num_one)+int(str_num_two)
    return add_result
#note what if it is a float?


def number_to_full_month_name(number):
   
  list_of_months = ["a","January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

  number_to_full_month_name=list_of_months[int(number)]

  return number_to_full_month_name


def number_to_short_month_name(number):

  list_of_short_months = {
        1:"Jan", 
        2:"Feb",
        3: "Mar",
        4: "Apr",
        5: "May", 
        6:"Jun", 
        7:"Jul", 
        8:"Aug",
        9:"Sep", 
        10:"Oct", 
        11:"Nov",
        12:"Dec"
        }
  return list_of_short_months[number]
    
 
def volume_of_cube(length):
    volume = length**3
    return volume


def reverse_string(string):
    reversed_string = string[::-1]
    return reversed_string
    
def fahrenheit_to_celsius(fahrenheit):
 celsius = (fahrenheit - 32) * 5/9
 return  celsius