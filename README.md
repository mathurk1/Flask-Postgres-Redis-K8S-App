# Flask-Redis-Postgres-K8S-App
a simple flask app with a postgres backend.
We have used kubernetes and helm apis to deploy the application on a local kubernetes installation (kubernetes on docker desktop)

## Run using kubernetes
to run the app using kubernetes APIs (commands):

1.  create secret for postgres admin password
    `kubectl create secret generic postgres-secrets --from-literal=password=postgres-admin-password`

2.  create secret for Azure Container Registry login
    `kubectl create secret docker-registry acrregistrykey --docker-server=link-to-registry --docker-username=username --docker-password=access-key`

3.  update:
    -  container image location at `containers.image` key in `flask.deployment.yml` file
    -  the `path` key for `postgres-init` volume in the `postgresql.deployment.yml` file to the init script (it should be to `src/database/db_create.sql` file)
    -  the `path` key for `postgrespv` in the `postgres.pv.yml` file and point to a folder to save the postgres database dumps/backups. This location can be used to restore the postgres db in case the container crashes.

4.  Apply the k8s config files
    `kubectl apply -f k8s/`


## Run using helm
1.  create a `secretvalues.yml` file at the root of the charts (`k8shlmcharts` folder)
2.  populate the secretvalues in the file as :
    ```
    postgresdb:
      password: postgres-password
      init_script_pth: "/Complete/path/to/file/src/database/db_create.sql"
      postgres_db_backup: "/Complete/path/to/folder/postgresdbvolume"

    flask-app:
      acrloginkey: "credentials to login to the docker registry where the images is loaded (dockerhub, acr etc.)"
      registryname: registry+image-name:tag
    ```
3. run command from the root (`k8shelmcharts` folder) of the helm charts directory `helm install flaskapp . -f secretvalues.yml`

## To Do:
1. setup on actual kubernetes cluster
2. setup ingress services
3. setup a cloud storage as a volume
4. setup deployment pipelines to push to kubernetes cluster
