from django.test import TestCase

# Create your tests here.


from django.shortcuts import render, HttpResponse, redirect, reverse

c=reverse("userinfo:index")
print(c)