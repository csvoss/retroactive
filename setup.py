from setuptools import setup

setup(
    name='retroactive',
    version='0.1',
    description='Retroactive data structures',
    long_description="Implements algorithms for various types of retroactive data structures. Retroactive data structures allow operations to be 'retroactively' performed, affecting the history of the data structure.",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering',
        'Topic :: Utilities',
        'Intended Audience :: Science/Research',
    ],
    keywords='retroactive data structures retroactivity datastructures persistence algorithms queue deque union-find stack priority-queue',
    url='http://github.com/csvoss/retroactive',
    author='Chelsea Voss',
    author_email='voss.chelsea@gmail.com',
    license='GPL',
    packages=['retroactive', 'retroactive.basic', 'retroactive.partial', 'retroactive.full'],
    install_requires=[
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=False)
