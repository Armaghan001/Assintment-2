favorite_languages_armaghan = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
}
print("Follwing items are in the dictionary.")
for name,language in favorite_languages_armaghan.items():
 print(name.title()+"'s favorite Language is: "+language.title())
# adding new keys and values in the dictionary
favorite_languages_armaghan['Lara']='html'
favorite_languages_armaghan['Smith']='php'
print("\nFollwing items are in the dictionary after adding new keys 
and values.")
for name,language in favorite_languages_armaghan.items():
 print(name.title()+"'s favorite Language is --> 
"+language.upper())
Follwing items are in the dictionary.
Jen's favorite Language is: Python
Sarah's favorite Language is: C
Edward's favorite Language is: Ruby
Phil's favorite Language is: Python
Follwing items are in the dictionary after adding new keys and values.
Jen's favorite Language is --> PYTHON
Sarah's favorite Language is --> C
Edward's favorite Language is --> RUBY
Phil's favorite Language is --> PYTHON
Lara's favorite Language is --> HTML
Smith's favorite Language is --> PHP