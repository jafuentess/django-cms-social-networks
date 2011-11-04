from setuptools import setup, find_packages

version = "0.0.0"


try:
    long_description=file('README').read(),
except Exception:
    pass

try:
    license=file('MIT_License.txt').read(),
except Exception:
    pass

setup(
    name = 'django-cms-social-networks',
    version = version,
    description = 'Django CMS Social Networks Plugins',
    author = 'Pablo Saavedra',
    author_email = 'pablo.saavedra@treitos.com',
    url = 'http://github.com/psaavedra/django-cms-social-networks',
    download_url= 'https://github.com/psaavedra/django-cms-social-networks/zipball/master',
    packages = find_packages(),
    package_data={
        'cms_social_facebook': [
            'templates/cms_social_facebook/*.html',
        ],
    },
    zip_safe=False,
    install_requires=[
        "django-cms>=2.1",
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    long_description=file('README').read(),
    license=file('MIT_License.txt').read(),
    keywords = "social networks facebook comments",
)
