from setuptools import (
    setup,
    find_packages,
)



setup(
    name='django-app-permissions',
    version='2.2.0',
    url='https://github.com/amp89/django-app-permissions',
    download_url="https://github.com/amp89/django-app-permissions/blob/master/dist/django-app-permissions-2.2.0.tar.gz",
    license='MIT',
    description='Automatic app level authentication for django apps using django',
    long_description=open('README.rst', 'r', encoding='utf-8').read(),
    author='Alex Peterson',
    author_email='contact@alexpeterson.tech',
    install_requires=[
        'django',
        'djangorestframework',
        'django-drf-advanced-token',
    ],
    python_requires='>=3.6',
    
)
