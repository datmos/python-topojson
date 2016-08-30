from setuptools import setup

setup(name='topojson',
    version='0.2.1',
    description='An extension to GeoJSON that encodes topology.',
    url='https://github.com/osgn/python-topojson',
    download_url='https://github.com/osgn/python-topojson/archive/0.2.0.tar.gz',
    
    packages=['topojson'],
    package_dir={
      'topojson': 'src/'
    },
    
    license='BSD',
)
