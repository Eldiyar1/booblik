
from django.utils.translation import gettext_lazy as _

JAZZMIN_SETTINGS = {
    "site_title": "Booblick",
    "site_header": "Booblick",
    "site_logo_classes": "img-circle",
    "site_brand": "Административная",
    "welcome_sign": "Добро пожаловать в Booblick",
    "copyright": "Booblick",
    "search_model": ["auth.User"],
    "show_ui_builder": True,
    "topmenu_links": [
        {"name": _("Home"), "url": "admin:index", "permissions": ["auth.view_user"]},
        {"app": "Booblick"},
        {"model": "auth.User"},
        {"name": "Support", "url": "https://t.me/elldiyar", "new_window": True},
    ],
    "default_icon_parents": "fas fa-circle",
    "default_icon_children": "fas fa-dot-circle",
    "show_sidebar": True,
    "navigation_expanded": True,
    "changeform_format": "horizontal_tabs",
    "language_chooser": True,
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    "icons": {
        "vacancy.Vacancy": "fas fa-solid fa-briefcase",
        "geolocation.Location": "fas fa-solid fa-map",
        "courses.Review": "fas fa-solid fa-comment",
        "event.News": "fas fa-solid fa-newspaper",
        "auth.Group": "fas fa-users",
        "auth.User": "fas fa-user",
    }
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-dark",
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-warning",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": False,
    "theme": "cyborg",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    },
    "actions_sticky_top": True
}
