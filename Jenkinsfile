pipeline {
    agent any
    environment {
       DOCKER_IMAGE_NAME = "rayapallisuresh/api"
    }
    stages {
        stage('Build') {
            steps {
                echo 'Running build automation'
            }
        }
        stage('Build Docker Image') {
            when {
                branch 'master'
            }
            steps {
                script {
                    app = docker.build(DOCKER_IMAGE_NAME, "-f api/Dockerfile" )

                }
            }
        }
        stage('Push Docker Image') {
            when {
                branch 'master'
            }
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker_hub_login') {
                        app.push("${env.BUILD_NUMBER}")
                        app.push("latest")
                    }
                }
            }
        }
         stage('DeployApplication') {
            when {
                branch 'master'
            }
            steps {
                input 'Deploy to Kubernetes Cluster?'
                milestone(1)
                kubernetesDeploy(
                    kubeconfigId: 'kubeconfig',
                    configs: 'diginex_deploy.yml',
                    enableConfigSubstitution: true
                )
            }
        }
    }
}
