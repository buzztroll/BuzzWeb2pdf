from setuptools import setup

__author__ = 'bresnaha'

Version = "0.1"

setup(name='buzzweb2pdf',
      version=Version,
      description='An Open Source tool to convert HTML documentation with an index page into a single PDF.',
      author='BuzzTroll',
      author_email='buzztroll@gmail.com',
      url='http://www.buzztroll.net/',
      packages=[ 'buzzweb2pdf' ],
       entry_points = {
        'console_scripts': [
            'buzzweb2pdf = buzzweb2pdf.web2pdf:main',
        ],

      },
#      download_url ="http://www.nimbusproject.org/downloads/cloudinitd-%s.tar.gz" % (Version),
      keywords = "http html pdf index documentation convert",
      long_description="""
Convert web documentation to a pdf with a single command.  This was written specifically to fetch 'Thinking in C++
into a format that I could read on a nook.
""",
      license="Apache2",
      install_requires = ["xhtml2pdf"],

      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Topic :: System :: Clustering',
          'Topic :: System :: Distributed Computing',
          ],
     )
