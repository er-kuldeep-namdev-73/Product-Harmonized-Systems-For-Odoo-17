===============================
Product Harmonized System Codes
===============================

This module contains the objects for Harmonised System Codes (H.S. codes). The full nomenclature is available from the `World Customs Organisation <http://www.wcoomd.org/>`. These codes are usually required on the Proforma invoices that are attached to the packages that are shipped abroad.

This module also handles the local/national extensions to the H.S. codes. The import of the full nomenclature is not provided by this module; it should be provided by localization modules.

You will also be able to configure the *country of origin* of a product, which is often required on the proforma invoice for the customs.

This module should be usefull for all companies that export physical goods abroad. This module is also used by the Intrastat modules for the European Union, cf the *intrastat_product* module.

**Table of contents**

.. contents::
   :local:

Installation
============

This module is NOT compatible with the *account_intrastat* module from Odoo Enterprise.

Usage
=====

As this module only depends on the *product* module and that module doesn't provide any menu entry, this module lacks a menu entry for H.S. Codes. A menu entry for H.S. codes is provided by the module *product_harmonized_system_stock*.

Once the H.S. codes are created, you will be able to set the H.S. code on a product (under the *Information* tab) or on a product category. On the product form, you will also be able to set the *Country of Origin* of a product (for example, if the product is *made in China*, select *China* as *Country of Origin*).

Bug Tracker
===========

.. Bugs are tracked on `GitHub Issues <https://github.com/OCA/intrastat-extrastat/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
.. `feedback <https://github.com/er-kuldeep-namdev-73/Product-Harmonized-Systems-For-Odoo-17.git>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Kuldeep Namdev

Maintainers
~~~~~~~~~~~
This module is maintained by the UNIWEDS SERVICES (OPC) PRIVATE LIMITED