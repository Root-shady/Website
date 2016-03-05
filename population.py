#! /usr/bin/python3
# Desc: Generate some sql statement to insert data into database
# DateTime: 2015-10-29 16:12
# Creator: shady

# Better for TTD
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myWeb.settings')
import django
django.setup()


from blog.models import Category, Tag

def populate():
    add_category('Linux')
    add_category('Python')
    add_category('Java')
    add_category('LifeHacking')
    add_category('ShellScript')
    add_category('Database')
    add_category('Algorithm')
    add_category('ComputerNetwork')
    add_category('Operating System')
    add_category('SoftwareEngineer')
    add_category('DataScience')

    add_tag('Linux')
    add_tag('Java')
    add_tag('Python')
    add_tag('Regex')
    add_tag('ADT')
    add_tag('CommandLine')
    add_tag('Bootstrap')
    add_tag('Jquery')
    add_tag('HTML')
    add_tag('CSS')
    add_tag('WebDevelopemnt')
    add_tag('Django')
    add_tag('Configuration')
    add_tag('Algorithm')
    add_tag('MySQL')
    add_tag('DataMining')
    add_tag('Machine Learning')
    add_tag('Hacking')
    
def add_tag(name):
    c = Tag(name=name)
    c.save()

def add_category(name):
    c = Category(name=name)
    c.save()
if __name__ == '__main__':
    populate()
