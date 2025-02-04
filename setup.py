#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name="tap-zendesk-chat",
      version="0.1.17",
      description="Singer.io tap for extracting data from the Zendesk Chat API",
      author="Stitch",
      url="http://singer.io",
      classifiers=["Programming Language :: Python :: 3 :: Only"],
      py_modules=["tap_zendesk_chat"],
      install_requires=[
          "python-dateutil==2.6.0",  # because of singer-python issue
          "pendulum==1.2.0",  # because of singer-python issue
          "singer-python==3.5.0",
          "requests==2.20.0",
      ],
      entry_points="""
          [console_scripts]
          tap-zendesk-chat=tap_zendesk_chat:main
      """,
      packages=["tap_zendesk_chat"],
      package_data = {
          "schemas": ["tap_zendesk_chat/schemas/*.json"]
      },
      include_package_data=True,
)
