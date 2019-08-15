
Welcome to Mykonos's Documentation
===================================

Introduction
############

  Mykonos is a complete test automation tools for Android Device using Robot Framework and UI Automator (Python), it easy to learn because Mykonos use BDD syntax to write the test cases.

Installation
############

     pip install mykonos

Usage
#####
 * Download and Install android emulator, base on the guidance `Genymotion <https://www.genymotion.com/>`_ or `Android Emulator <https://github.com/codepath/android_guides/wiki/Installing-Android-SDK-Tools>`_.
 * Make sure emulator is available by checking with `adb devices`, for more detail info please check the adb command on `ADB Shell <http://adbshell.com/commands/adb-devices>`_ guidance.
 * Make sure Robot Framework is able to run by execute `robot --version` and it will get Robot Framework version as a result.
 * Create a file (**sample.robot**).
 * Import **__Mykonos__** Library on the Robot Framework Test Suite.
 * Write test case base on `Robot Framework <http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#libdoc>`_ guidance.

Selector Support:
#################
  * text, textContains, textMatches, textStartsWith
  * className, classNameMatches
  * description, descriptionContains, descriptionMatches, descriptionStartsWith
  * checkable, checked, clickable, longClickable
  * scrollable, enabled,focusable, focused, selected
  * packageName, packageNameMatches
  * resourceId, resourceIdMatches
  * index, instance

.. toctree::
   :maxdepth: 2
   :caption: Detail Keywords:

   keyword.rst


Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
