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

### Configuration ###

If you want, you can set a static global password for all users. This provides
slightly more security, but not that much more than having no password set :)

```
c.DummyAuthenticator.password = "your strong password"
```
