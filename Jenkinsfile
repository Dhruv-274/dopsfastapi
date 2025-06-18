pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'dhruvrs/dockapp'
        DOCKER_CREDENTIALS = 'dockerhub-credentials'  // must match Jenkins credentials ID
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Dhruv-274/dopsfastapi.git',
                    credentialsId: 'github-credentials'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', DOCKER_CREDENTIALS) {
                        docker.image(DOCKER_IMAGE).push('latest')
                    }
                }
            }
        }
    }
}
