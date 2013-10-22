'''
Created on Jan 19, 2011

@author: sdj
'''

from distutils.core import setup

import seq_common

setup(
      name='Sequoia Utils',
      version='.'.join(map(str, seq_common.__version__)),
      description='Utility code for Python 2.7 or higher',
      author='sdejonckheere',
      author_email='sdejonckheere@sequoia-ge.ch',
      packages=['seq_common',
                'seq_common.db',
                'seq_common.utils',
                'seq_common.decorators',
                'seq_common.network'],
)