#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 22:24:50 2023

@author: remon
"""

def calculator():
    while True:
        try:
            numerator = input("Enter numerator: ")
            if numerator == "":
                break
            numerator = int(numerator)
            denominator = int(input("Enter denominator: "))
            answer = numerator / denominator
            print("Answer is", answer)
        except ValueError:
            print("Please enter a number.")
        except ZeroDivisionError:
            print("Can't divide by zero")
        except:
            print("Unknown Error")

if __name__ == '__main__':
    calculator()