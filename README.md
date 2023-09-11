# git_pull_server

Set `GPS_ROOT_DIR` in a `.env` file, like the following:

```
GPS_ROOT_DIR=/var/www/
```

Run `docker compose up -d` to deploy.

Then, in your CI, run `curl https://mydomain.com/git_pull_server?target=<dir_name>` to trigger a `git pull`.
