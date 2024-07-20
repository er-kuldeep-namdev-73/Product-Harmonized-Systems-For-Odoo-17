# @author Kuldeep Namdev

{
    "name": "Product Harmonized System (menu entry)",
    "version": "1.2",
    "category": "Reporting",
    "license": "AGPL-3",
    "summary": "Adds a menu entry for H.S. codes",
    "author": "UNIWEDS SERVICES (OPC) PRIVATE LIMITED",
    "maintainers": ["Kuldeep Namdev"],
    # "website": "https://github.com/OCA/intrastat-extrastat",
    "depends": ["product_harmonized_system_v17", "stock"],
    "data": ["views/hs_code_menu.xml"],
    "installable": True,
    "auto_install": True,
}