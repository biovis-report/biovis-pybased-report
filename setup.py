from setuptools import setup, find_packages

def get_version():
    return '0.5.0'

setup(
    name='biovis-base-plugins',
    version=get_version(),
    description='A set of Python-based plugins for biovis-report to draw interactive plots.',
    keywords='biovis-plugin',
    url='https://github.com/biovis-report/biovis-base-plugins',
    author='Jingcheng Yang',
    author_email='yjcyxky@163.com',
    license='MIT',
    python_requires='>=3.7',
    include_package_data=True,
    install_requires=[
        'biovis-report~=0.5',
        'multiqc'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    packages=find_packages(),
    entry_points={
        'biovis.plugins': [
            'multiqc = multiqc.multiqc:MultiqcPlugin'
        ]
    }
)
