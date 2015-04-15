from setuptools import setup, find_packages


setup(
    name='pulp-server',
    version='2.7.0a1',
    license='GPLv2+',
    packages=find_packages(exclude=['test']),
    author='Pulp Team',
    author_email='pulp-list@redhat.com',
    entry_points={
        'console_scripts': [
            '../libexec/pulp-manage-workers = pulp.server.async.manage_workers:main',
            'pulp-manage-db = pulp.server.db.manage:main',
        ]
    },
    install_requires=[
        'blinker', 'celery >=3.1.0, <3.2.0', 'django>=1.4.0', 'httplib2', 'iniparse',
        'isodate>=0.5.0', 'm2crypto', 'mongoengine>=0.7.10', 'oauth2>=1.5.211', 'pymongo>=2.5.2',
        'setuptools', 'web.py']
)
