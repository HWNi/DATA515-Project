import os
from setuptools import setup, find_packages
PACKAGES = find_packages()

opts = dict(name = 'Uber/Taxi',
            maintainer='Haowen Ni, Diana Chenyu Zhang, Liangzi Cong, Yawen Li, Zicong Liang',
            maintainer_email= 'uber.taxi@gmail.com',
            description = 'Visualization Tool of Uber and Taxi Traffic',
            long_description = 'This is an interactive visualizatin to compare Uber and taxi data at speicfic location, date, and time.',
            url= 'https://github.com/HWNi/DATA515-Project',
            download_url = "",                  
            license = 'MIT',
            classifiers= ["Development Status :: Alpha",
                          "Environment :: Console",
                          "Intended Audience :: General",
                          "License :: MIT License",
                          "Operating System :: OS Independent",
                          "Programming Language :: Python",
              `           "Topic :: Scientific/Engineering"],
            author='Haowen Ni, Diana Chenyu Zhang, Liangzi Cong, Yawen Li, Zicong Liang',
            author_email = 'uber.taxi@gmail.com',
            version='1.2',
            packages=['bokeh','json','pyodbc','pandas','numpy'],
            package_data="None",
            install_requires=["pyhton3","jupyter notebook"],
            requires=['bokeh','json','pyodbc','pandas','numpy'])

if __name__ == '__main__':
    setup(**opts)
