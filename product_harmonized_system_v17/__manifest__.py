# @author Kuldeep Namdev

{
    "name": "Product Harmonized System Codes",
    "version": "1.2",
    "category": "Reporting",
    "license": "AGPL-3",
    "summary": "Base module for Product Import/Export reports",
    "author": "UNIWEDS SERVICES (OPC) PRIVATE LIMITED",
    "maintainers": ["Kuldeep Namdev"],
    "depends": ["product"],
    "excludes": ["account_intrastat"],
    "data": [
        "security/product_hs_security.xml",
        "security/ir.model.access.csv",
        "views/hs_code.xml",
        "views/product_category.xml",
        "views/product_template.xml",
    ],
    "demo": ["demo/product_demo.xml"],
    "installable": True,
}
