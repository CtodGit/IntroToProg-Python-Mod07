**Christian Todhunter**
**06/02/2020**
**IT FDN 100 A**
**Assignment07**

# Errors Handling Pickles???

## Introduction to Module 07
For Module 07 we learned about pickling and error handling. We learned how pickling is pretty nifty for serializing (pickling) de-serializing (unpickling) and adding persistence to a program. In addition to this, we reviewed error handling, how to catch certain errors, how to create custom error handling, and how to print out custom messages when catching an exception. Last but not least, we have begun dabbling with the Markdown language with a ‘Github Flavor’ to take the words from this document (or maybe you are on the site already) and posting them to a Github webpage. 

### The Assignment Requirements
For this assignment, we set out to learn about pickles from the web, from the assigned reading, the class videos, and/or other texts. I stuck with the course text and the class videos, but I did end up looking at some youtube videos for assistance. The mission for the scripted assignment is to come up with our own demo code to show a little bit about pickling and error handling in Python. In the process of doing this, I ended up combining the two topics because frankly, my program required it. 

## The Persistent Pickle
I spent quite a bit of time trying to decide what to do. I ended up focusing on the persistence capabilities one is granted when pickling things, so I decided to create a mini-game type script, where a user has 10 tries to guess the password. If the user can’t get it right and they exit, pickling allows my program to ‘remember’ by dumping the current value of a variable to a .dat file via the pickling.dump() method, as shown below:




You can use the [editor on GitHub](https://github.com/CtodGit/IntroToProg-Python-Mod07/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.





Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/CtodGit/IntroToProg-Python-Mod07/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
