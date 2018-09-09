django_db_prefix
================

Project goal
------------

Allow specification of a global, per-app or per-model database table
name prefix.

Reason for the project
----------------------

1. Some (external) projects automatically use a database prefix for 
   interaction with a database. This is particularly common in implementations
   of the Active Record pattern.

2. It is possible to define an explicit database table name in the Meta
   class on a model; however, this is not as easily accomplished when dealing
   with a third-party application. By providing a high-level interface for
   adding prefixes there is a simple, consistent way to achieve this goal other
   than forking the code or ad-hoc monkey patching.

Installation
------------

1. Install using pip:

    pip install git+https://github.com/benslavin/django-db-prefix.git

2. Add django_db_prefix at the top of your INSTALLED_APPS list. It is
   recommended that django_db_prefix is the first listed application, but it
   is essential that it be loaded before the initialization of any model you
   expect to be modified.

Configuration
-------------

Three configuration options are allowed: global, per-app or per-model. In all
cases, the specified prefix will be prepended exactly as provided -- no
delimiter will be added.

In all cases, behavior is controlled by the `DB_PREFIX` setting.

Global Prefix
=============

To add a common prefix to all models simply set `DB_PREFIX` to the string that
you want to be prepended.

    DB_PREFIX = "foo"

For example, for the model bar_app.models.Baz the default table would be:
`bar_app_baz`

By setting `DB_PREFIX` to `foo`, the table would be `foo_bar_app_baz`.

Per-Application and Per-Model Prefix
====================================

Both per-application and per-model prefixes are controlled by the use of a
dictionary as the value of `DB_PREFIX`, where the dictionary contains keys
allowing the lookup of a given model or application.

When `DB_PREFIX` is a dictionary, `django_db_prefix` will perform the following
searches to determine the prefix to use. First match wins; if no matches are
found, no prefix will be added.

1. `app_label.model_name` following the standard Django convention, where
   `model_name` is converted to lowercase before attempting to match.
2. `app_label` where `app_label` is the name of the application.
3. `None` allowing for a global default when using the dictionary specification
   format.

A sample specification:

    DB_PREFIX = {
        "foo.bar": "bar_model_prefix",
        "foo.baz": "baz_model_prefix",
        "foo": "foo_app_backup_prefix",
        "wobble": "wobble_app_prefix",
        None: "default_prefix"
    }
