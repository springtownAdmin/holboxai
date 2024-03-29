from distutils.core import setup
setup(
  name = 'holboxai',         # How you named your package folder (MyLib)
  packages = ['holboxai'],   # Chose the same as "name"
  version = '0.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'HolboxAI package',   # Give a short description about your library
  author = 'Sahil Khatri',                   # Type in your name
  author_email = 'sahil.khatri@holbox.ai',      # Type in your E-Mail
  url = 'https://github.com/springtownAdmin/holboxai',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/springtownAdmin/holboxai/archive/refs/tags/v_04.tar.gz',    # I explain this later on
  keywords = ['GenAI', 'Custom', 'holbox'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'diffusers',
          'flask',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.8',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)