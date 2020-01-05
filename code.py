#!/bin/python3

import math
import os
import random
import re
import sys

# lexical analyzer class
class lexical_analyzer():
  def __init__(self,expr):
    self.expr=expr

  # function to seperate literals from expression
  def literals(self,expr):
    lit=[]
    for i in self.expr:
      if(i.isdigit()):# check if the character is digit[0-9]
        lit.append(i)
    print("Literals:")
    for i in range(len(lit)):
      print("lit"+str(i)+"   "+str(lit[i]))
  
  # function to seperate operators
  def operators(self,expr):
    opr=[]
    oprs=["+","-","/","*","="]
    for i in self.expr:
      if(i in oprs):# check if the character is operator[+-/*=]
        opr.append(i)
    print("\nOperators:")
    for i in range(len(opr)):
      print("Opr"+str(i)+"   "+str(opr[i]))
  
  # function to seperate variables
  def variables(self,expr):
    var=[]
    for i in self.expr:
      if(i.isalpha()):# check if the character is variable[a-zA-Z]
        var.append(i)
    print("\nVariables:")
    for i in range(len(var)):
      print("id"+str(i)+"   "+str(var[i]))

  # function to analyze expression
  def analyze(self):
    self.literals(self.expr)
    self.operators(self.expr)
    self.variables(self.expr)

# predictive parsing/ recursive parsing(top-down parsing)
class predictive_parser():
  def __init__(self,expr,c,flag):
    self.expr=expr
    self.c=c
    self.flag=flag

  def print_res(self):
    self.e()
    if(self.c==len(self.expr) and self.flag==0):
      print("The expression is valid")
    else:
      print("The expression is invalid")

  def e(self):
    self.t()
    self.eprime()

  def t(self):
    self.check()
    self.tprime()

  def tprime(self):
    if(self.c!=len(self.expr)):
       if(self.expr[self.c]=="*"):
          self.c+=1
          self.check()
          self.tprime()
       elif(self.expr[self.c]=="/"):
          self.c+=1
          self.check()
          self.tprime()

  def check(self,):
    if(self.c!=len(self.expr)):
       if(self.expr[self.c].isalnum()):
          self.c+=1
       elif(self.expr[self.c]=="("):
          self.c+=1
          self.e()
          if(self.expr[self.c]==")"):
             self.c+=1
          else:
             self.flag=1
       else:
          self.flag=1
  
  def eprime(self,):
    if(self.c!=len(self.expr)):
       if(self.expr[self.c]=="+"):
          self.c+=1
          self.t()
          self.eprime()
       elif(self.expr[self.c]=="-"):
          self.c+=1
          self.t()
          self.eprime()

# class dfa(Deterministic finite automaton) to RE
class dfa_to_re():
  def __init__(self,expr):
    self.expr=expr
  # re=(a+b)*(b+c*)
  def check(self):
    end=0
    flag=1
    j=0
    l=len(self.expr)
    for i in self.expr:
      if(i=="a"):
        end=1
        j+=1
      elif(i=="c"):
        j+=1
        if(j==l):
          flag=0
          end=0
      elif(i=="b"):
        end=0
        flag=0
        j+=1
      if(i!="a" and i!="b" and i!="c"):
        print("Not Accepted")
        break
    if(end==0 and flag==0):
      print("Accepted")
    else:
      print("Not Accepted")


def menu():
  print("\n1) Lexical Analyzer")
  print("\n2) Predictive Parsing")
  print("\n3) RE to DFA")
  choice=int(input("Enter your choice:"))
  if(choice==1):
    l=list(map(str,input("Enter the expression:").rstrip().rsplit()))
    k=lexical_analyzer(l)
    k.analyze()
  elif(choice==2):
    l=list(map(str,input("Enter the algebraic expression:").rstrip().rsplit()))
    k=predictive_parser(l,0,0)
    k.print_res()
  elif(choice==3):
    l=list(map(str,input("Program for DFA of RE(a+b)*(b+c*):").rstrip().rsplit()))
    k=dfa_to_re(l)
    k.check()
  else:
    print("Incorrect input")

menu()





