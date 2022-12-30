from setuptools import setup

setup(
    name='voytek-dev-django',
    version='0.1.0',
    packages=['pages', 'pages.migrations', 'voytek_dev_django'],
    url='https://github.com/lvoytek/voytek_dev_django',
    license='GPLv3',
    author='Lena Voytek',
    author_email='lena@voytek.dev',
    description='voytek.dev created with Django',
    install_requires=[
        'django',
        'django-compressor',
        'django-libsass',
        'user_agents'
    ],
)
