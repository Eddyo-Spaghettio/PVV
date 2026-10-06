# WordPress scripts

One-off scripts used to update PVV's WordPress site over its REST API. They are not part of the training or Bridge Kit.

Each script reads its login from environment variables (for example `WP_APP_PASSWORD`). Nothing is stored in the repo. Never commit a `.env` file or password, since `.env` is already in `.gitignore`.
