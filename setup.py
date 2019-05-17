import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyopls',
    version='19.05',
    author='BiRG @ Wright State University',
    author_email='foose.3@wright.edu',
    description='Orthogonal Projection to Latent Structures',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/BiRG/pyopls',
    packages=setuptools.find_packages(),
    python_requires='>=3.4',
    instal_requires=[
        'numpy>=1.11.0',
        'scipy>=0.18.0',
        'scikit-learn>=0.18.0'
    ],
    classifiers=[
        'Natural Language :: English',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)