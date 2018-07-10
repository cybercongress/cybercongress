## Circle Ci job example

To enable auto staging-redeploy for your application you should:

1. Enable ***staging*** docker images build. For example, you can use dockerhub tag "STAGING". 

2. Add to [the repo](https://github.com/cyberFund/cybernode) you image running script.

3. Add a CircleCi job, depended on docker build&push job. It's all.



## Example: build and deploy for all commits in master
```
aliases:
 - &staging_filter
    filters:
      tags:
        only: /.*/
      branches:
        only: master
       
        
jobs:        
  build_and_push_image_staging_image:
    working_directory: ~/build
    docker:
      - image: docker:17.05.0-ce-git
    steps:
      - checkout
      - setup_remote_docker:
          version: 17.05.0-ce
      - run:
          name: Build and upload staging images
          command: |
            docker build -t build/cs-search-api -f ./devops/search-api/search-api ./
            docker login -u $DOCKER_USER -p $DOCKER_PASS
            docker tag build/cs-search-api cybernode/cs-search-api:staging
            docker push cybernode/cs-search-api:staging
            
    deploy_stagin_image:
      working_directory: ~/build
      docker:
        - image: docker:17.05.0-ce-git
      steps:
        - run:
            name: Rerun image on staging
            command: >-
              ssh mars@staging.cyber.fund -p 33322 -o "StrictHostKeyChecking no"
              'cd /cyberdata/cybernode && git pull && sh /cyberdata/cybernode/up.search.sh'
             
             
workflows:
  version: 2
  staging_cd:
    jobs:
      - build_and_push_image_staging_image:
          <<: *staging_filter
      - deploy_stagin_image:
          <<: *staging_filter
          requires:
            - build_and_push_image_staging_image
```

