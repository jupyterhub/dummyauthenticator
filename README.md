# Dummy JupyterHub Authenticator #

Simple authenticator for [JupyterHub](http://github.com/jupyter/jupyterhub/)
that allows all user logins regardless of password. Useful only for testing,
do not use for anything actually serious!

## Installation ##

```
pip install jupyterhub-dummyauthenticator
```

Should install it. It has no additional dependencies beyond JupyterHub.

You can then use this as your authenticator by adding the following line to
your `jupyterhub_config.py`:

```
c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'
```
